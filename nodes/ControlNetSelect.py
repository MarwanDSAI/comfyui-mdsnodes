# Marwan Custom Nodes
# To get control_net_name as STRING
# -------------------------------------------------------
import os

class MarControlNetSelect:
    # Main Node Description (Shows in search dialog and "Node Info" panel)
    DESCRIPTION = "Allows you to easily select a ControlNet model name and connect it directly to the Load ControlNet Model node."

    @classmethod
    def INPUT_TYPES(cls):
        import folder_paths
        return {
            "required": {
                "control_net_name": (
                    folder_paths.get_filename_list("controlnet"),
                    {
                        "tooltip": "Select a ControlNet model file from your models/controlnet directory."
                    }
                ),
            }
        }

    # COMBO allows nodes expecting a dropdown selection list to accept it
    RETURN_TYPES = ("*", "STRING", "STRING",)
    RETURN_NAMES = ("control_net_name", "control_net_name (STRING)", "control_net_name_no_ext (STRING)",)
    
    # Tooltips for the output slots
    OUTPUT_TOOLTIPS = (
        "Passes the raw combo selection to nodes expecting a ControlNet name.",
        "The full filename as a standard STRING (e.g. 'control_v11p_sd15_canny.pth').",
        "The filename without the file extension as a STRING (e.g. 'control_v11p_sd15_canny')."
    )

    FUNCTION = "get_name"
    CATEGORY = "MDSNodes/utils/"

    def get_name(self, control_net_name):
        # Extract the base filename without its extension
        control_net_name_no_ext = os.path.splitext(control_net_name)[0]
        
        # Returns COMBO, full string, and string without extension
        return (control_net_name, str(control_net_name), control_net_name_no_ext)