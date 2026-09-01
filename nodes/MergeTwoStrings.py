# Marwan Custom Nodes
# Merge Two Strings
# -------------------------------------------------------
class MarMergeTwoStrings:
    DESCRIPTION = "Merges two strings with an optional delimiter if both strings are not empty. Handles None or missing inputs as empty string."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "string_a": ("STRING", {
                    "default": "", 
                    "forceInput": True,
                    "tooltip": "First input string. If disconnected or None, treated as empty."
                }),
                "string_b": ("STRING", {
                    "default": "", 
                    "forceInput": True,
                    "tooltip": "Second input string. If disconnected or None, treated as empty."
                }),
                "delimiter": ("STRING", {
                    "default": " ", 
                    "multiline": False,
                    "tooltip": "Delimiter added between string_a and string_b only when both contain text."
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("merged_string",)
    OUTPUT_TOOLTIPS = ("The merged output string, or an empty string if both inputs are empty.",)
    
    FUNCTION = "merge"
    CATEGORY = "MDSNodes/text"

    def merge(self, string_a=None, string_b=None, delimiter=" "):
        # Sanitize inputs: Treat None or non-string inputs safely as strings
        str_a = str(string_a).strip() if string_a is not None else ""
        str_b = str(string_b).strip() if string_b is not None else ""
        delim = str(delimiter) if delimiter is not None else ""

        # Delimiter logic: add delimiter only if both sides contain text
        if str_a and str_b:
            result = f"{str_a}{delim}{str_b}"
        elif str_a:
            result = str_a
        elif str_b:
            result = str_b
        else:
            result = ""

        return (result,)