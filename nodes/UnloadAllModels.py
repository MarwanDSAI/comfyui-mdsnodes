# Marwan Custom Nodes
# Passthrough node that strips LoRA patches, unloads all models from VRAM, and flushes PyTorch CUDA cache..
# ----------------------------------------------------------------------------------------------------------------------
import gc
import torch
import comfy.model_management


class MarUnloadAllModels:
    DESCRIPTION = "Passthrough node that strips LoRA patches, unloads all models from VRAM, and flushes PyTorch CUDA cache."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Wildcard passthrough wire
                "passthrough": ("*", {"tooltip": "Connect the data stream you want to pass through."}),
            },
            "optional": {
                "model_to_unpatch": ("MODEL", {
                    "tooltip": "Optional: Connect your MODEL stream to forcefully detach/unpatch all applied LoRAs."
                }),
                "clip_to_unpatch": ("CLIP", {
                    "tooltip": "Optional: Connect your CLIP stream to forcefully detach/unpatch all applied LoRAs."
                }),
                "force_gc": ("BOOLEAN", {
                    "default": True, 
                    "tooltip": "Force Python garbage collection and CUDA cache empty."
                }),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("passthrough",)
    OUTPUT_TOOLTIPS = ("The untouched input data passed forward.",)
    
    FUNCTION = "unload_models"
    CATEGORY = "MDSNodes/utils"

    def unload_models(self, passthrough, model_to_unpatch=None, clip_to_unpatch=None, force_gc=True):
        # 1. Strip and detach LoRA patches from MODEL / CLIP if connected
        if model_to_unpatch is not None:
            try:
                if hasattr(model_to_unpatch, "unpatch_model"):
                    model_to_unpatch.unpatch_model(unpatch_weights=True)
                if hasattr(model_to_unpatch, "detach"):
                    model_to_unpatch.detach()
            except Exception as e:
                print(f"[MarNodes] Warning unpatching model: {e}")

        if clip_to_unpatch is not None:
            try:
                if hasattr(clip_to_unpatch, "unpatch_model"):
                    clip_to_unpatch.unpatch_model(unpatch_weights=True)
                if hasattr(clip_to_unpatch, "detach"):
                    clip_to_unpatch.detach()
            except Exception as e:
                print(f"[MarNodes] Warning unpatching clip: {e}")

        # 2. Unload all models (Base models + LoRAs) managed by ComfyUI
        comfy.model_management.unload_all_models()
        comfy.model_management.soft_empty_cache()

        # 3. Force garbage collection & CUDA cache clearing
        if force_gc:
            gc.collect()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
                torch.cuda.ipc_collect()

        return (passthrough,)