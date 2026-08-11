# Marwan Custom Nodes
# To get ontrol_net_name as STRING
# -------------------------------------------------------
import os
class MarControlNetSelect:
    @classmethod
    def INPUT_TYPES(cls):
        import folder_paths
        return {
            "required": {
                "control_net_name": (folder_paths.get_filename_list("controlnet"),),
            }
        }

    #COMBO allows nodes expecting a dropdown selection list to accept it
    RETURN_TYPES = ("*", "STRING", "STRING",)
    RETURN_NAMES = ("control_net_name", "control_net_name (STRING)", "control_net_name_no_ext (STRING)",)
    FUNCTION = "get_name"
    CATEGORY = "utils/MarNodes"

    def get_name(self, control_net_name):
        # Extract the base filename without its extension
        control_net_name_no_ext = os.path.splitext(control_net_name)[0]
        
        # Returns COMBO, full string, and string without extension
        return (control_net_name, str(control_net_name), control_net_name_no_ext)
        