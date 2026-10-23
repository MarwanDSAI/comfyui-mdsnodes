# Marwan Custom Nodes
# Performs up to 8 sequential search and replace operations on a main text string.
# --------------------------------------------------------------------------------------------------
class MarStrReplaceMultiple:
    DESCRIPTION = "Performs up to 8 sequential search and replace operations on a main text string."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Changed to False so the main text box renders as a single line
                "main_text": (
                    "STRING",
                    {
                        "default": "",
                        "multiline": True,
                        "tooltip": "The main text block to be modified."
                    }
                ),
                "search_1": ("STRING", {"default": "", "multiline": False}),
                "replace_1": ("STRING", {"default": "", "multiline": False}),
                
                "search_2": ("STRING", {"default": "", "multiline": False}),
                "replace_2": ("STRING", {"default": "", "multiline": False}),
                
                "search_3": ("STRING", {"default": "", "multiline": False}),
                "replace_3": ("STRING", {"default": "", "multiline": False}),
                
                "search_4": ("STRING", {"default": "", "multiline": False}),
                "replace_4": ("STRING", {"default": "", "multiline": False}),
                
                "search_5": ("STRING", {"default": "", "multiline": False}),
                "replace_5": ("STRING", {"default": "", "multiline": False}),

                "search_6": ("STRING", {"default": "", "multiline": False}),
                "replace_6": ("STRING", {"default": "", "multiline": False}),
                
                "search_7": ("STRING", {"default": "", "multiline": False}),
                "replace_7": ("STRING", {"default": "", "multiline": False}),
                
                "search_8": ("STRING", {"default": "", "multiline": False}),
                "replace_8": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result_text",)
    OUTPUT_TOOLTIPS = ("The final string after all replacements have been applied.",)
    
    FUNCTION = "process_text"
    CATEGORY = "MDSNodes/text"

    def process_text(self, main_text, search_1, replace_1, search_2, replace_2, search_3, replace_3, search_4, replace_4, search_5, replace_5, search_6, replace_6, search_7, replace_7, search_8, replace_8):
        # Cast the main input to a string to ensure safe manipulation
        result = str(main_text)
        
        # Sequentially execute search and replace for each pair
        if search_1:
            result = result.replace(search_1, replace_1)
        if search_2:
            result = result.replace(search_2, replace_2)
        if search_3:
            result = result.replace(search_3, replace_3)
        if search_4:
            result = result.replace(search_4, replace_4)
        if search_5:
            result = result.replace(search_5, replace_5)
        if search_6:
            result = result.replace(search_6, replace_6)
        if search_7:
            result = result.replace(search_7, replace_7)
        if search_8:
            result = result.replace(search_8, replace_8)
            
        return (result,)
# --------------------------------------------------------------------------------------------------
# Performs a single search and replace operation on a main text string.
# --------------------------------------------------------------------------------------------------
class MarStrReplaceSingle:
    DESCRIPTION = "Performs a single search and replace operation on a string."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Renamed from "main_text" to "string"
                "string": (
                    "STRING",
                    {
                        "forceInput": True,
                        "tooltip": "The text block to be modified."
                    }
                ),
                "search": ("STRING", {"default": "", "multiline": False}),
                "replace": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    OUTPUT_TOOLTIPS = ("The final string after the replacement has been applied.",)
    
    FUNCTION = "process_text"
    CATEGORY = "MDSNodes/text"

    # Updated function arguments to match the new input name
    def process_text(self, string, search, replace):
        # Cast the input to a string to ensure safe manipulation
        result = str(string)
        
        # Execute search and replace
        if search:
            result = result.replace(search, replace)
            
        return (result,)
# --------------------------------------------------------------------------------------------------
