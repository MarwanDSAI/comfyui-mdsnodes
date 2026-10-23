# Marwan Custom Nodes
# Look up a Key and return value from up to 8 key/value slots.
# -------------------------------------------------------
class MarKeyValueSelector8:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "forceInput": True,
                    "tooltip": "Lookup name.",
                }),
            },
            "optional": {
                "key1": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "Slot 1 name. Match this against the key input.",
                }),
                "value1": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Slot 1 text. Returned on value when key matches key1.",
                }),
                "key2": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "Slot 2 name. Match this against the key input.",
                }),
                "value2": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Slot 2 text. Returned on value when key matches key2.",
                }),
                "key3": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "Slot 3 name. Match this against the key input.",
                }),
                "value3": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Slot 3 text. Returned on value when key matches key3.",
                }),
                "key4": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "Slot 4 name. Match this against the key input.",
                }),
                "value4": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Slot 4 text. Returned on value when key matches key4.",
                }),
                "key5": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "Slot 5 name. Match this against the key input.",
                }),
                "value5": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Slot 5 text. Returned on value when key matches key5.",
                }),
                "key6": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "Slot 6 name. Match this against the key input.",
                }),
                "value6": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Slot 6 text. Returned on value when key matches key6.",
                }),
                "key7": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "Slot 7 name. Match this against the key input.",
                }),
                "value7": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Slot 7 text. Returned on value when key matches key7.",
                }),
                "key8": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "tooltip": "Slot 8 name. Match this against the key input.",
                }),
                "value8": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Slot 8 text. Returned on value when key matches key8.",
                }),
                "default": ("STRING", {
                    "default": "",
                    "multiline": True,
                    "tooltip": "Fallback text. Returned on value when key matches none of key1 to key8. Slot output is 0.",
                }),
                "case_sensitive": ("BOOLEAN", {
                    "default": False,
                    "tooltip": "Off: case and surrounding spaces are ignored.",
                }),
            },
        }

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("value", "slot")
    OUTPUT_TOOLTIPS = (
        "Matched multiline text from the selected slot, or default if nothing matched.",
        "Matched slot number 1 to 8. 0 means no match and default was used.",
    )
    FUNCTION = "select"
    CATEGORY = "MDSNodes/text"
    DESCRIPTION = (
        "Select one multiline string from 8 named slots. "
         "The first slot whose key matches is returned on value, with the slot number on slot. "
        "Empty slot keys are skipped. If nothing matches, default is returned and slot is 0. "
    )

    def select(
        self,
        key,
        key1="",
        value1="",
        key2="",
        value2="",
        key3="",
        value3="",
        key4="",
        value4="",
        key5="",
        value5="",
        key6="",
        value6="",
        key7="",
        value7="",
        key8="",
        value8="",
        default="",
        case_sensitive=False,
    ):
        needle = key if case_sensitive else key.strip().lower()
        slots = (
            (1, key1, value1),
            (2, key2, value2),
            (3, key3, value3),
            (4, key4, value4),
            (5, key5, value5),
            (6, key6, value6),
            (7, key7, value7),
            (8, key8, value8),
        )

        for slot, slot_key, slot_val in slots:
            if not (slot_key or "").strip():
                continue
            compare = slot_key if case_sensitive else slot_key.strip().lower()
            if compare == needle:
                return (slot_val, slot)

        return (default, 0)