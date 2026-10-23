# Marwan Custom Nodes
# Math
# --------------------------------------------------------------------------
class MarRound:
    DESCRIPTION = "Rounds an incoming float to a chosen number of decimal places (0-5) and outputs both FLOAT and STRING."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_val": ("FLOAT", {
                    "forceInput": True, 
                    "tooltip": "The floating-point number to round."
                }),
                "decimals": ([0, 1, 2, 3, 4, 5], {
                    "default": 0,
                    "tooltip": "Number of decimal places to round to."
                }),
            }
        }

    RETURN_TYPES = ("FLOAT", "STRING")
    RETURN_NAMES = ("FLOAT", "STRING")
    OUTPUT_TOOLTIPS = (
        "The rounded number as a float.",
        "The rounded number formatted as a string."
    )
    FUNCTION = "round_float"
    CATEGORY = "MDSNodes/Math"

    def round_float(self, float_val, decimals):
        rounded_val = round(float_val, decimals)
        
        # When decimals is 0, format cleanly as an integer string if desired, or keep as standard float string
        if decimals == 0:
            str_val = f"{int(rounded_val)}"
        else:
            str_val = f"{rounded_val:.{decimals}f}"

        return (float(rounded_val), str_val)
# --------------------------------------------------------------------------