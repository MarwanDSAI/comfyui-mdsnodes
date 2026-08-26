# Marwan Custom Nodes
# Anything to String
# -------------------------------------------------------
class MarCStr:
    DESCRIPTION = "Converts any incoming data type safely into a standard string."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Wildcard type "*" allows connection from any node output slot
                "any_input": ("*", {"tooltip": "Connect any data type (INT, FLOAT, COMBO, MODEL, etc.) here."}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    OUTPUT_TOOLTIPS = ("The input data converted into a clean text string.",)
    FUNCTION = "convert"
    CATEGORY = "MDSNodes/text"

    def convert(self, any_input=None):
        if any_input is None:
            return ("",)
        return (str(any_input),)


# Registration Mappings
NODE_CLASS_MAPPINGS = {
    "MarCStr": MarCStr
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MarCStr": "Convert to String"
}