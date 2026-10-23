# Marwan Custom Nodes
# return second string if first one is empty.
# --------------------------------------------------------------------------------------------------
class MarStrTrimFallback:
    DESCRIPTION = "Trims the primary string (string_a). If it is empty after trimming, it outputs the trimmed fallback string (fallback_b). Otherwise, it outputs the trimmed primary string."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "string_a": ("STRING", {"forceInput": True}),
                "fallback_b": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    FUNCTION = "process_strings"
    CATEGORY = "MDSNodes/text"

    def process_strings(self, string_a: str = "", fallback_b: str = ""):
        trimmed_a = (string_a or "").strip()
        trimmed_b = (fallback_b or "").strip()
        
        result = trimmed_a if trimmed_a != "" else trimmed_b
        return (result,)