from comfy_models.base.comfy_utils import Config

config = Config(
    id="flux-dev",
    name="Flux (Dev)",
    # memroy snspshot
    models_to_cache=[
        "unet/flux1-dev.sft",
        "clip/clip_l.safetensors",
        "clip/clip_g.safetensors",
        "clip/t5xxl_fp16.safetensors",
        "vae/ae.sft",
    ],
    # run_twice=True,
    # nodes to preload during comfyui cold start
    # nodes_to_preload=["UNETLoader", "VAELoader", "DualCLIPLoader"],
    warmup_workflow=True,
    preview_image="https://comfy-deploy-output-dev.s3.us-east-2.amazonaws.com/outputs/runs/b5afa7eb-a15f-4c45-a95c-d5ce89cb537f/image.jpeg",
)
