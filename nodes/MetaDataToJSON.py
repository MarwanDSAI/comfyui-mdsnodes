# Marwan Custom Nodes
# Converts MetaData with structure Key1 [Value1]; Key2 [Value2]; Key3 [Value3];... into a mapping/dict for EXTRA_METADATA.
# ----------------------------------------------------------------------------------------------------------------------
import re

class MarMetaDataToJSON:
    DESCRIPTION = "Converts MetaData with structure Key1 [Value1]; Key2 [Value2]; Key3 [Value3];... into a dictionary for EXTRA_METADATA."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "metadata": ("STRING", {
                    "default": "",
                    "forceInput": True,
                    "tooltip": "The appended metadata string from MetaDataAppend format Key1 [Value1]; Key2 [Value2]; Key3 [Value3];..."
                }),
            }
        }

    RETURN_TYPES = ("EXTRA_METADATA",)
    RETURN_NAMES = ("EXTRA_METADATA",)
    OUTPUT_TOOLTIPS = ("The metadata formatted as a dictionary/mapping.",)
    
    FUNCTION = "convert"
    CATEGORY = "MDSNodes/text"

    def convert(self, metadata=""):
        # Safely treat None or missing inputs as empty strings
        in_str = str(metadata).strip() if metadata is not None else ""
        
        if not in_str:
            return ({},)

        meta_dict = {}
        # Split by semicolon to separate individual key-value pairs
        pairs = in_str.split(';')
        
        for pair in pairs:
            pair = pair.strip()
            if not pair:
                continue
            
            # Leverage regular expressions to extract key and value
            match = re.search(r"^(.*?)\s*\[(.*?)\]$", pair)
            if match:
                key = match.group(1).strip()
                val = match.group(2).strip()
                meta_dict[key] = val

        # Return the dictionary directly instead of serializing to a JSON string
        return (meta_dict,)