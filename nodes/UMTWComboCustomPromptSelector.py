# Marwan Custom Nodes
# This node was designed for The Ultimate Model Tester Workflow Custom Test for Prompt Selection after ComfyUI v0.30+ update.
# since  ComfyUI v0.30+ (V2 / Nodes 2.0 schema) tightened boundary socket type enforcement, 
# rejecting raw combo objects across subgroup boundaries. 
# This node outputs standard primitive strings to ensure seamless routing."
# can be edited and used for predetermined combo text seclection. 
# -------------------------------------------------------
# v1.7.0: 12 items total
# v1.8.0: expanding the list and editing items,  adding index/combo text output  
# -------------------------------------------------------
class MarUMTWComboCustomPromptSelector:
    # Main Node Description
    DESCRIPTION = "Designed for UMTW Custom Test Prompt Selection after ComfyUI v0.30+ update. Note: ComfyUI v0.30+ (V2 / Nodes 2.0 schema) tightened boundary socket type enforcement, rejecting raw combo objects across subgroup boundaries. This node outputs standard primitive strings to ensure seamless routing."
    
    @classmethod
    def INPUT_TYPES(cls):
        # 1. Define your custom options list (add or remove items here)
        combo_options = [
            "1: Runway Portrait", "2: Paris Night in Leather", 
            "3: Blonde and Brunette Sydney Love", "4: Black Gloves and White Heels", 
            "5: Gym Blonde in Olive Camo","6: Women garden relax time", 
            "7: Confident woman - mirror test", "8: Daenerys with Dragon", 
            "9: Snowy Peak Reverie", "10: Lakeside Terrace Elegance",
            "11: Egypt Desert Goddess", "12: Lara Croft",
            "13: Rose-Gold Glamour on the Sofa","14: Blond in Black on Park Bench",
            "15: Woman in Black at Grand Piano","16: Yellow Mermaid Night Portrait",
            "17: Spiked Catgirl","18: Summer Hug by the Silent Pool",
            "19: Studded Boots and Soft Light","20: Red Hair Against Blue Rails",
            "21: ","22: ",
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

    RETURN_TYPES = ("STRING", "INT", "STRING")
    RETURN_NAMES = ("CUSTOM PROMPT", "INDEX", "COMBO TEXT")
    OUTPUT_TOOLTIPS = (
        "The Prompt selected via the combo box.", 
        "1-based integer index of the selection.", 
        "The exact text of the selected combo option."
    )

    FUNCTION = "select_string"
    CATEGORY = "MDSNodes/UMTW"

    def select_string(self, test_prompt, **kwargs):
        # Extract the index number from the combo string (e.g., "1: Runway Portrait" -> "1")
        slot_key = test_prompt.split(":", 1)[0].strip() if ":" in test_prompt else "1"
        
        # Retrieve the string from kwargs matching the numbered slot
        val = kwargs.get(slot_key, "")
        
        # Convert slot_key to a 1-based integer index
        try:
            index_val = int(slot_key)
        except ValueError:
            index_val = 0
            
        # Safely convert to string and return all three outputs
        return (str(val) if val is not None else "", index_val, test_prompt)