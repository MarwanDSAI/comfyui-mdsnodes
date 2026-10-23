# Marwan Custom Nodes
# Appends MetaData with structure Key1 [Value1]; Key2 [Value2]; Key3 [Value3];...
# Changed value to textbox 9/3/26 v1.4.0
# --------------------------------------------------------------------------------
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
                # Single-line textbox entry for the key
                "key": ("STRING", {
                    "default": "my_key", 
                    "multiline": False,
                    "tooltip": "The key name you type into the textbox."
                }),
                # Single-line textbox entry for the value
                "value": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "The single-line text value to insert inside the brackets."
                }),

            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("METADATA",)
    OUTPUT_TOOLTIPS = ("The combined output string with the appended key and value.",)
    
    FUNCTION = "append_data"
    CATEGORY = "MDSNodes/MetaData"

    def append_data(self, metadata=None, value="", key=""):
        # Safely treat None or missing inputs as empty strings
        in_str = str(metadata).strip() if metadata is not None else ""
        val_str = str(value) if value is not None else ""
        k_str = str(key) if key is not None else ""

        # Construct the requested addition formatting
        addition = f"; {k_str} [{val_str}]"

        # Add delimiter only if the base string contains text to keep things clean
        if in_str:
            result = f"{in_str}{addition}"
        else:
            result = f"{k_str} [{val_str}]"

        return (result,)
# --------------------------------------------------------------------------------
# Removes a key from MetaData with structure Key1 [Value1]; Key2 [Value2]; Key3 [Value3];...
# --------------------------------------------------------------------------------
class MarMetaDataRemove:
    DESCRIPTION = "Removes a key and its bracketed value from metadata formatted as: Key1 [Value1]; Key2 [Value2];..."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "metadata": ("STRING", {
                    "default": "", 
                    "forceInput": True,
                    "tooltip": "The metadata string to remove the entry from."
                }),
                "key": ("STRING", {
                    "default": "", 
                    "multiline": False,
                    "tooltip": "The key name to find and remove."
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("METADATA",)
    OUTPUT_TOOLTIPS = ("The metadata string with the specified key removed.",)
    
    FUNCTION = "remove_data"
    CATEGORY = "MDSNodes/MetaData"

    def remove_data(self, metadata=None, key=""):
        if not metadata:
            return ("",)

        target_key = str(key).strip()
        if not target_key:
            return (str(metadata).strip(),)

        # Split metadata into individual "Key [Value]" tokens
        entries = str(metadata).split(";")
        remaining_entries = []

        prefix = f"{target_key} ["

        for item in entries:
            clean_item = item.strip()
            # If the item doesn't start with the target key, keep it
            if clean_item and not clean_item.startswith(prefix):
                remaining_entries.append(clean_item)

        # Re-join remaining items with standard delimiter
        result = "; ".join(remaining_entries)
        return (result,)
# --------------------------------------------------------------------------------
