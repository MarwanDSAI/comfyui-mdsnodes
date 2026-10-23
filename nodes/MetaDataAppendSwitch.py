# Marwan Custom Nodes
# Appends MetaData with structure Key1 [Value1]; Key2 [Value2]; Key3 [Value3];...; chosen the value based on a toggle switch. Skips appending if the value is empty.
# -------------------------------------------------------
class MarMetaDataAppendSwitch:
    DESCRIPTION = "Appends a key and chosen value to metadata based on a toggle switch. Skips appending if the value is empty."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # The True/False toggle checkbox
                "switch": ("BOOLEAN", {
                    "default": True,
                    "tooltip": "True appends value_true, False appends value_false."
                }),
                # Single-line textbox entry for the key
                "key": ("STRING", {
                    "default": "my_key", 
                    "multiline": False,
                    "tooltip": "The key name you type into the textbox."
                }),
                # Textbox entry passed when switch is ON
                "value_true": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "The text value to insert when the switch is True."
                }),
                # Textbox entry passed when switch is OFF
                "value_false": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "The text value to insert when the switch is False."
                }),
            },
            "optional": {
                # Placing this in 'optional' ensures it gracefully defaults to None if unhooked[cite: 20]
                "metadata": ("STRING", {
                    "default": "", 
                    "forceInput": True,
                    "tooltip": "The original base string. If disconnected, treated as empty."
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("METADATA",)
    OUTPUT_TOOLTIPS = ("The combined output string with the appended key and value.",)
    
    FUNCTION = "append_data"
    CATEGORY = "MDSNodes/MetaData"

    def append_data(self, switch=True, key="", value_true="", value_false="", metadata=None):
        # Safely treat None or missing inputs as empty strings[cite: 20]
        in_str = str(metadata).strip() if metadata is not None else ""
        k_str = str(key) if key is not None else ""

        # Python routing to determine which value is active based on the switch[cite: 20]
        chosen_value = value_true if switch else value_false
        val_str = str(chosen_value).strip() if chosen_value is not None else ""

        # If the chosen value is completely empty, do not append anything and return the original string
        if val_str == "":
            return (in_str,)

        # Construct the requested addition formatting[cite: 20]
        addition = f"; {k_str} [{val_str}]"

        # Add delimiter only if the base string contains text to keep things clean[cite: 20]
        if in_str:
            result = f"{in_str}{addition}"
        else:
            result = f"{k_str} [{val_str}]"

        return (result,)