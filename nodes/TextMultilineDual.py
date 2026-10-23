# Marwan Custom Nodes
# Dual Multiline Text Input Node
# -------------------------------------------------------
class MarTextMultilineDual:
    DESCRIPTION = "Provides two independent multiline text boxes and outputs both strings."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_a": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "First multiline text input."
                }),
                "text_b": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Second multiline text input."
                }),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("text_a", "text_b")
    OUTPUT_TOOLTIPS = (
        "Output of the first multiline text.",
        "Output of the second multiline text."
    )

    FUNCTION = "process"
    CATEGORY = "MDSNodes/text"

    def process(self, text_a="", text_b=""):
        return (str(text_a), str(text_b))