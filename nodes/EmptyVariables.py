# Marwan Custom Nodes
# Outputs a completely empty variables
# ----------------------------------------------------------------------------------------------------------------------
import torch

class MarEmptyVariables:
    DESCRIPTION = "Outputs a completely empty string and a blank latent."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {
                    "default": 512, 
                    "min": 16, 
                    "max": 16384, 
                    "step": 8,
                    "tooltip": "Width of the empty latent image."
                }),
                "height": ("INT", {
                    "default": 512, 
                    "min": 16, 
                    "max": 16384, 
                    "step": 8,
                    "tooltip": "Height of the empty latent image."
                }),
                "batch_size": ("INT", {
                    "default": 1, 
                    "min": 1, 
                    "max": 4096,
                    "tooltip": "Number of latents in the batch."
                })
            }
        }

    RETURN_TYPES = ("STRING", "LATENT")
    RETURN_NAMES = ("empty_string", "empty_latent")
    FUNCTION = "generate_empty"
    CATEGORY = "MDSNodes/Routing"

    def generate_empty(self, width, height, batch_size):
        # 1. Generate the empty string
        empty_str = ""
        
        # 2. Generate the empty latent
        # ComfyUI latents are structured as a dictionary with a "samples" key
        # The tensor shape is [batch_size, channels (4), height // 8, width // 8]
        latent_tensor = torch.zeros([batch_size, 4, height // 8, width // 8])
        empty_latent = {"samples": latent_tensor}

        return (empty_str, empty_latent)