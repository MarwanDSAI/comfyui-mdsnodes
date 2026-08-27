# Marwan Custom Nodes
# Appends MetaData with structure Key1 [Value1]; Key2 [Value2]; Key3 [Value3];...
# -------------------------------------------------------
class MarMetaDataAppend:
    DESCRIPTION = "Appends a key and value to metadata in the format: Key1 [Value1]; Key2 [Value2]; Key3 [Value3];..."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Force this to be a connected input wire rather than a text box
                "metadata": ("STRING", {
                    "default": "", 
                    "forceInput": True,
                    "tooltip": "The original base string. If disconnected, treated as empty."
                }),
                # Wildcard type "*" allows connection from any node output slot (INT, FLOAT, STRING, etc.)
                "value": ("*", {
                    "tooltip": "The dynamic value to insert inside the brackets. Accepts any data type."
                }),
                # Multiline set to False creates a simple single-line text entry box for the key
                "key": ("STRING", {
                    "default": "my_key", 
                    "multiline": False,
                    "tooltip": "The key name you type into the textbox."
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("METADATA",)
    OUTPUT_TOOLTIPS = ("The combined output string with the appended key and value.",)
    
    FUNCTION = "append_data"
    CATEGORY = "MDSNodes/text"

    def append_data(self, metadata=None, value=None, key=""):
        # Safely treat None or missing inputs as empty strings
        in_str = str(metadata).strip() if metadata is not None else ""
        val_str = str(value) if value is not None else ""
        k_str = str(key) if key is not None else ""

        # Construct the requested addition formatting
        addition = f"; {k_str} [{val_str} ]"

        # Add delimiter only if the base string contains text to keep things clean
        if in_str:
            result = f"{in_str}{addition}"
        else:
            result = f"{k_str} [{val_str} ]"

        return (result,)