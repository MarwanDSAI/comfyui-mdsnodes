# Marwan Custom Nodes
# UNET Name to CKPT_NAME
# -------------------------------------------------------
class UNetNameToCKPTName:
    # Main Node Description (Shows in search dialog and "Node Info" panel)
    DESCRIPTION = "allows to use a UNET model name as a ckpt_name input for RGTHREE_CONTEXT."
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

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("CKPT_NAME",)
    
    # Fixed Output pin tooltip with proper quotes
    OUTPUT_TOOLTIPS = ("The selected model filename passed forward as a string/universal data stream.",)
    
    FUNCTION = "get_name"
    CATEGORY = "MDSNodes/utils/text"

    def get_name(self, unet_name):
        return (unet_name,)