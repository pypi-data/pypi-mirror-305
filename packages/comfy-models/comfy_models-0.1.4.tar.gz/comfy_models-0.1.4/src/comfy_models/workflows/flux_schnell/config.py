from comfy_models.base.comfy_utils import Config

config = Config(
    id="flux_schnell",
    name="Flux (Schnell)",
    # memroy snspshot
    models_to_cache=[
        "unet/flux1-schnell.sft",
        "clip/clip_l.safetensors",
        "clip/clip_g.safetensors",
        "clip/t5xxl_fp16.safetensors",
        "vae/ae.sft",
    ],
    warmup_workflow=True,
    preview_image="https://comfy-deploy-output-dev.s3.us-east-2.amazonaws.com/outputs/runs/b5afa7eb-a15f-4c45-a95c-d5ce89cb537f/image.jpeg",
)
