# Marwan Custom Nodes
# -------------------------------------------------------
class MarRatioCombobox:
    # Main Node Description (Shows in search dialog and "Node Info" panel)
    DESCRIPTION = "Provides an easy way to select from predefined aspect ratios or scaling percentages and output them as a float."
    
    @classmethod
    def INPUT_TYPES(cls):
        options = ["10%", "15%", "25%", "50%", "75%", "85%", "100%"]
        return {
            "required": {
                # Added tooltip dictionary to the ratio dropdown widget
                "ratio": (
                    options, 
                    {
                        "default": "50%",
                        "tooltip": "Select a predefined percentage option from the list."
                    }
                ),
            }
        }

    # This sets the header title of the node
    TITLE = "Ratio Combobox"
    
    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("ratio_float",)
    
    # Tooltips for the output slots
    OUTPUT_TOOLTIPS = (
        "The selected percentage converted into a decimal float value (e.g., 50% becomes 0.5).",
    )

    FUNCTION = "make"
    CATEGORY = "MDSNodes/FLOAT"

    # The argument here MUST match the key "ratio" exactly
    def make(self, ratio):
        # Convert the selected string to a float
        numeric_value = float(ratio.replace("%", "")) / 100.0
        return (numeric_value,)