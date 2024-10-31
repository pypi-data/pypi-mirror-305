import json
from typing import List

import torch
import tqdm

from mergekit.architecture import ConfiguredArchitectureInfo, get_architecture_info
from mergekit.common import ModelReference
from mergekit.io import LazyTensorLoader, TensorWriter

source_ref = ModelReference.model_validate("mistral-community/Mixtral-8x22B-v0.1")
loader = LazyTensorLoader(source_ref.tensor_index())

source_cfg = source_ref.config()
arch = ConfiguredArchitectureInfo(
    info=get_architecture_info(source_cfg), config=source_cfg
)

writer = TensorWriter("/workspace/demixtral-22b")

INTERMEDIATE_SIZE = 14336 * 2

for weight_info in tqdm.tqdm(arch.all_weights(), desc="Copying weights"):
    name = weight_info.name
    if ".block_sparse_moe." in name:
        continue
    writer.save_tensor(
        weight_info.name,
        loader.get_tensor(weight_info.name, aliases=weight_info.aliases),
    )


def svd_approx(tensors: List[torch.Tensor], svd_ratio: float = 0.9) -> torch.Tensor:
    tensors = torch.stack(tensors, dim=0)
    u, s, vh = torch.linalg.svd(tensors.float(), full_matrices=False)

    # Compute mask for singular values
    s_cumsum = torch.cumsum(s, dim=-1)
    s_mask = s_cumsum / s_cumsum[-1] > svd_ratio
    s_p = s * s_mask

    # Combine across batch dimension and compute final approximation
    u_p = torch.cat([u.squeeze(0) for u in u], dim=-1)
    vh_p = torch.cat([v.squeeze(0) for v in vh], dim=-2)
    s_p = torch.diag_embed(torch.cat([s for s in s_p], dim=-1))
    return (u_p @ s_p @ vh_p).to(tensors.dtype)


for layer_idx in tqdm.tqdm(range(source_cfg.num_hidden_layers), desc="SVD approx"):
    for out_name, template in [
        (
            f"model.layers.{layer_idx}.mlp.up_proj.weight",
            f"model.layers.{layer_idx}.block_sparse_moe.experts.{{expert_idx}}.w3.weight",
        ),
        (
            f"model.layers.{layer_idx}.mlp.down_proj.weight",
            f"model.layers.{layer_idx}.block_sparse_moe.experts.{{expert_idx}}.w2.weight",
        ),
        (
            f"model.layers.{layer_idx}.mlp.gate_proj.weight",
            f"model.layers.{layer_idx}.block_sparse_moe.experts.{{expert_idx}}.w1.weight",
        ),
    ]:
        tensors = [
            loader.get_tensor(
                template.format(expert_idx=expert_idx),
                device="cuda",
            )
            for expert_idx in range(source_cfg.num_local_experts)
        ]
        approx = svd_approx(tensors)
        writer.save_tensor(out_name, approx)

writer.finalize()
out_cfg = source_cfg.to_dict()
del out_cfg["num_local_experts"]
del out_cfg["num_experts_per_tok"]
if "output_router_logits" in out_cfg:
    del out_cfg["output_router_logits"]
if "router_aux_loss_coef" in out_cfg:
    del out_cfg["router_aux_loss_coef"]
out_cfg["model_type"] = "mistral"
out_cfg["architectures"] = ["MistralForCausalLM"]

with open("/workspace/demixtral-22b/config.json", "w", encoding="utf-8") as f:
    json.dump(out_cfg, f, indent=4)
