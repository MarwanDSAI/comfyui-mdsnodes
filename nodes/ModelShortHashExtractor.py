# Marwan Custom Nodes
# -------------------------------------------------------
import hashlib
import os
import folder_paths

class MarModelShortHashExtractor:
    DESCRIPTION = "Calculates a 10-character short hash from a checkpoint or diffusion model filename."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_filename": ("STRING", {
                    "forceInput": True, 
                    "tooltip": "The model filename string."
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("short_hash",)
    OUTPUT_TOOLTIPS = ("The 10-character model hash.",)
    
    FUNCTION = "get_short_hash"
    CATEGORY = "MDSNodes/utils"

    def get_short_hash(self, model_filename):
        if not model_filename or model_filename == "None":
            return ("",)

        clean_name = str(model_filename).strip()

        # Attempt to resolve the path from the checkpoints folder first
        model_path = folder_paths.get_full_path("checkpoints", clean_name)
        
        # If not found, attempt to resolve from the diffusion_models (UNET) folder
        if not model_path or not os.path.exists(model_path):
            model_path = folder_paths.get_full_path("diffusion_models", clean_name)

        # If the file still does not exist on disk, return an error string
        if not model_path or not os.path.exists(model_path):
            return (f"Error: {clean_name} not found",)

        # Fast hashing logic: read a specific chunk instead of the entire multi-GB file
        sha256 = hashlib.sha256()
        try:
            with open(model_path, "rb") as f:
                # Read the entire file in 4MB chunks to prevent memory crashes
                for chunk in iter(lambda: f.read(4194304), b""):
                    sha256.update(chunk)
            
            # Civitai AutoV2 format uses the first 10 characters of the full SHA256
            calculated_hash = sha256.hexdigest()[:10]
            return (calculated_hash,)
        except Exception as e:
            return (f"Error: {str(e)}",)