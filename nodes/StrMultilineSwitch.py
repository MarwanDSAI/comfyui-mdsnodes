# Marwan Custom Nodes
# Outputs either the first or second multiline string depending on the boolean switch.
# -------------------------------------------------------
class MarStrMultilineSwitch:
    DESCRIPTION = "Outputs either the first or second multiline string depending on the boolean switch."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # The True/False toggle checkbox
                "switch": ("BOOLEAN", {
                    "default": True,
                    "tooltip": "True outputs the First String, False outputs the Second String."
                }),
                # Multiline text box for the first string
                "true_switch_string": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Text returned when the switch is True."
                }),
                # Multiline text box for the second string
                "false_switch_string": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Text returned when the switch is False."
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    OUTPUT_TOOLTIPS = ("The selected multiline string.",)

    FUNCTION = "select_string"
    CATEGORY = "MDSNodes/logic"

    def select_string(self, switch, true_switch_string, false_switch_string):
        # Python routing to determine what data gets sent downstream based on the switch
        chosen = true_switch_string if switch else false_switch_string
        return (chosen,)