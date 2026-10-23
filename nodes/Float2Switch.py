# Marwan Custom Nodes
# Outputs either the first or second float depending on the boolean switch.
# -------------------------------------------------------
class MarFloat2Switch:
    DESCRIPTION = "Outputs either the first or second float depending on the boolean switch."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # The True/False toggle checkbox
                "switch": ("BOOLEAN", {
                    "default": True,
                    "tooltip": "True outputs the First Float, False outputs the Second Float."
                }),
                # Native number text box for the first float
                "true_switch_float": ("FLOAT", {
                    "default": 1.00,
                    "min": -0xffffffffffffffff,
                    "max": 0xffffffffffffffff,
                    "step": 0.01,
                    "tooltip": "Value returned when the switch is True."
                }),
                # Native number text box for the second float
                "false_switch_float": ("FLOAT", {
                    "default": 0.00,
                    "min": -0xffffffffffffffff,
                    "max": 0xffffffffffffffff,
                    "step": 0.01,
                    "tooltip": "Value returned when the switch is False."
                }),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT",)
    OUTPUT_TOOLTIPS = ("The selected float.",)

    FUNCTION = "select_float"
    CATEGORY = "MDSNodes/logic"

    def select_float(self, switch, true_switch_float, false_switch_float):
        # Python routing to determine what data gets sent downstream based on the switch
        chosen = true_switch_float if switch else false_switch_float
        return (float(chosen),)