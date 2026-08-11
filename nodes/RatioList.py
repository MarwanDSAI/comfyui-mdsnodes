# Marwan Custom Nodes
# -------------------------------------------------------
class MarwanRatioListNode:
    @classmethod
    def INPUT_TYPES(cls):
        options = ["10%", "15%", "25%", "50%", "75%",  "85%", "100%"]
        return {
            "required": {
                # Use an underscore instead of a space for the dictionary key
                "ratio": (options, {"default": "50%"}),
            }
        }

    # This sets the header title of the node
    TITLE = "Marwan Ratio List"
    
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "make"
    CATEGORY = "MarNodes"

    # The argument here MUST match the key "ratio" exactly
    def make(self, ratio):
        # Convert the selected string to a float
        numeric_value = float(ratio.replace("%", "")) / 100.0
        return (numeric_value,)

        