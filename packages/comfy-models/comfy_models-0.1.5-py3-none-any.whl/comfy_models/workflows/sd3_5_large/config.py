from comfy_models.base.comfy_utils import Config

config = Config(
    id="sd3-5-large",
    name="SD3.5 (Large)",
    models_to_cache=[
        "checkpoints/sd3.5_large.safetensors",
        "clip/clip_l.safetensors",
        "clip/clip_g.safetensors",
        "clip/t5xxl_fp16.safetensors",
    ],
    warmup_workflow=True,
    preview_image="https://comfy-deploy-output.s3.amazonaws.com/outputs/runs/36febfce-3cb6-4220-9447-33003e58d381/ComfyUI_00001_.png",
)
