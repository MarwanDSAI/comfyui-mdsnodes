# Marwan Custom Nodes
# Outputs either the first or second integer depending on the boolean switch.
# -------------------------------------------------------
class MarIntSwitch:
    DESCRIPTION = "Outputs either the first or second integer depending on the boolean switch."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # The True/False toggle checkbox
                "switch": ("BOOLEAN", {
                    "default": True,
                    "tooltip": "True outputs the First Int, False outputs the Second Int."
                }),
                # Native number text box for the first integer
                "true_switch_int": ("INT", {
                    "default": 1,
                    "min": -0xffffffffffffffff,
                    "max": 0xffffffffffffffff,
                    "step": 1,
                    "tooltip": "Value returned when the switch is True."
                }),
                # Native number text box for the second integer
                "falce_switch_int": ("INT", {
                    "default": 0,
                    "min": -0xffffffffffffffff,
                    "max": 0xffffffffffffffff,
                    "step": 1,
                    "tooltip": "Value returned when the switch is False."
                }),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("INT",)
    OUTPUT_TOOLTIPS = ("The selected integer.",)

    FUNCTION = "select_int"
    CATEGORY = "MDSNodes/logic"

    def select_int(self, switch, true_switch_int, falce_switch_int):
        # Python routing to determine what data gets sent downstream based on the switch
        chosen = true_switch_int if switch else falce_switch_int
        return (int(chosen),)