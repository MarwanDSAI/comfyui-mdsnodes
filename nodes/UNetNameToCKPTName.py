# Marwan Custom Nodes
# UNET Name to CKPT_NAME
# -------------------------------------------------------
class UNetNameToCKPTName:
    @classmethod
    def INPUT_TYPES(cls):
        import folder_paths
        return {
            "required": {
                "unet_name": (folder_paths.get_filename_list("diffusion_models"),),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("CKPT_NAME",)
    FUNCTION = "get_name"
    CATEGORY = "MarNodes/utils/text"

    def get_name(self, unet_name):
        return (unet_name,)