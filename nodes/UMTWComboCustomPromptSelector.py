# Marwan Custom Nodes
# -------------------------------------------------------
class MarUMTWComboCustomPromptSelector:
    # Main Node Description
    DESCRIPTION = "Designed for UMTW Custom Test Prompt Selection after ComfyUI v0.30+ update. Note: ComfyUI v0.30+ (V2 / Nodes 2.0 schema) tightened boundary socket type enforcement, rejecting raw combo objects across subgroup boundaries. This node outputs standard primitive strings to ensure seamless routing."
    
    @classmethod
    def INPUT_TYPES(cls):
        # 1. Define your custom options list (add or remove items here)
        combo_options = [
            "1: Runway Portrait", "2: Glamorous Night in Leather", 
            "3: Prone Elegance", "4: Arched All-Fours Gaze", 
            "5: Gym Overhead Portrait","6: Women garden  relax time", 
            "7: Confident Curvy Woman in in Black", "8: Daenerys with Dragon", 
            "9: Snowy Peak Reverie", "10: Lakeside Terrace Elegance",
            "11: Egypt Desert Goddess",

        ]

        # 2. Automatically generate optional inputs matching the options
        optional_inputs = {
            str(i): (
                "STRING", 
                {
                    "forceInput": True, 
                    "default": "", 
                }
            )
            for i, _ in enumerate(combo_options, start=1)           
        }

        return {
            "required": {
                "test_prompt": (
                    combo_options, 
                    {
                        "default": combo_options[0] if combo_options else "",
                    }
                ),
            },
            "optional": optional_inputs
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("CUSTOM PROMPT",)
    OUTPUT_TOOLTIPS = ("The Prompt selected via the combo box.",)

    FUNCTION = "select_string"
    CATEGORY = "MDSNodes/text"

    def select_string(self, test_prompt, **kwargs):
        # Extract the index number from the combo string (e.g., "1: Runway Portrait" -> "1")
        slot_key = test_prompt.split(":", 1)[0].strip() if ":" in test_prompt else "1"
        
        # Retrieve the string from kwargs matching the numbered slot
        val = kwargs.get(slot_key, "")
        
        # Safely convert to string and prevent None crashes
        return (str(val) if val is not None else "",)