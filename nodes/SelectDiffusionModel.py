# Marwan Custom Nodes
# Select Diffusion Model (Outputs CKPT_NAME & UNET_NAME)
# -------------------------------------------------------
class MarSelectDiffusionModel:
    # Main Node Description (Shows in search dialog and "Node Info" panel)
    DESCRIPTION = "Select a diffusion/UNET model and output its filename as CKPT_NAME and UNET_NAME (e.g. for RGTHREE_CONTEXT)."
    # --------------------------
    @classmethod
    def INPUT_TYPES(cls):
        import folder_paths
        return {
            "required": {
                "unet_name": (
                    folder_paths.get_filename_list("diffusion_models"),
                    {
                        "tooltip": "Select the diffusion / UNET model file whose filename you want to extract."
                    }
                ),
            }
        }

    RETURN_TYPES = ("*", "*")
    RETURN_NAMES = ("CKPT_NAME", "UNET_NAME")
    
    OUTPUT_TOOLTIPS = (
        "The selected model filename passed forward as CKPT_NAME (wildcard/string).",
        "The selected model filename passed forward as UNET_NAME (wildcard/string)."
    )
    
    FUNCTION = "get_name"
    CATEGORY = "MDSNodes/text"

    def get_name(self, unet_name):
        return (unet_name, unet_name)


# -------------------------------------------------------
# Node Registration
# -------------------------------------------------------
NODE_CLASS_MAPPINGS = {
    "MarSelectDiffusionModel": MarSelectDiffusionModel
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MarSelectDiffusionModel": "Select Diffusion Model"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]