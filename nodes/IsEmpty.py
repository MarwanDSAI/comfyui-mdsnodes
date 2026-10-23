# Marwan Custom Nodes
# Checks if an incoming input is empty, None, or disconnected. Outputs True if empty, False if it contains data.
# ----------------------------------------------------------------------------------------------------------------------
class MarIsEmpty:
    DESCRIPTION = "Checks if an incoming input is empty, None, or disconnected. Outputs True if empty, False if it contains data."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                # The "*" wildcard allows you to plug any data type into this slot.
                # Placing it in "optional" ensures it gracefully defaults to None if left disconnected.
                "any_input": ("*", {
                    "tooltip": "The input to evaluate. If disconnected or an empty string, the node outputs True."
                })
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("is_empty",)
    OUTPUT_TOOLTIPS = ("True if the input is empty/None, False otherwise.",)
    
    FUNCTION = "evaluate"
    CATEGORY = "MDSNodes/logic"

    def evaluate(self, any_input=None):
        # 1. Check if the input is completely disconnected (None)
        if any_input is None:
            return (True,)
        
        # 2. Check if the input is a string and is completely blank
        if isinstance(any_input, str) and any_input.strip() == "":
            return (True,)
        
        # 3. If it has any other data, it is not empty
        return (False,)