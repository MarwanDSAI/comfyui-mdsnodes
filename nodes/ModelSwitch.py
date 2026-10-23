# Marwan Custom Nodes
# Outputs either the first or second integer depending on the boolean switch.
# -------------------------------------------------------
class MarModelSwitch:
    """
    A switch node to alternate between Model A and Model B using a boolean toggle.
    - switch = True (ON)   -> outputs Model A
    - switch = False (OFF)  -> outputs Model B
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_a": ("MODEL",),
                "model_b": ("MODEL",),
                "switch_on": ("BOOLEAN", {
                    "default": True, 
                    "label_on": "Model A (ON)", 
                    "label_off": "Model B (OFF)"
                }),
            }
        }

    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("MODEL",)
    FUNCTION = "switch_models"
    CATEGORY = "utils/logic"

    def switch_models(self, model_a, model_b, switch_on):
        selected_model = model_a if switch_on else model_b
        return (selected_model,)