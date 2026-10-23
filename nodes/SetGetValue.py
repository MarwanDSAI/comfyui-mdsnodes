# Marwan Custom Nodes
# Store any value to be reused in ComfyUI, 
# MarGetValue node should be wired after excution of MarSetValue otherwise will not work
# ----------------------------------------------------------------------------------------------------------------------
# A special class to allow connections to any socket type in ComfyUI
class AnyType(str):
    def __eq__(self, _) -> bool:
        return True
    def __ne__(self, _) -> bool:
        return False

# Create the wildcard type
any_type = AnyType("*")

# Global dictionary to store variables
GLOBAL_SHARED_STATE = {}

class MarSetValue:
    DESCRIPTION = "Stores any value globally into a variable that can be retrieved later by MarGetValue. This node executes even if the output is unconnected."
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {
                    "default": "my_variable", 
                    "tooltip": "The unique name/key to store the value under."
                }),
                "value": (any_type, {
                    "tooltip": "The data or connection you want to store. Accepts any type."
                }),
            }
        }
    
    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ("value_passthrough",)
    FUNCTION = "set_value"
    CATEGORY = "MDSNodes/Routing"
    OUTPUT_NODE = True # Ensures the node executes even if the output isn't connected

    def set_value(self, key, value):
        GLOBAL_SHARED_STATE[key] = value
        return (value,)

class MarGetValue:
    DESCRIPTION = "Retrieves a globally stored value set by MarSetValue. Wire the trigger_order to ensure this node waits for the value to be set first."
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {
                    "default": "my_variable", 
                    "tooltip": "The unique name/key of the stored variable to retrieve."
                }),
            },
            "optional": {
                "trigger_order": (any_type, {"tooltip": "Connect the passthrough from MarSetValue here to force ComfyUI to wait."}),
                "pass_value": ("BOOLEAN", {
                    "default": True,
                    "forceInput": True,
                    "tooltip": "If True, outputs the retrieved value. If False, outputs the fallback_value (or None)."
                }),
                "fallback_value": (any_type, {
                    "tooltip": "Optional: Connect an empty variable (e.g., empty string, empty latent) here to be output when pass_value is False."
                }),
            }
        }
    
    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_value"
    CATEGORY = "MDSNodes/Routing"

    def get_value(self, key, trigger_order=None, pass_value=True, fallback_value=None):
        # If the boolean wire receives False, return the fallback value (defaults to None if unconnected)
        if not pass_value:
            return (fallback_value,)
            
        # Retrieve the value, or return None if it hasn't been set yet
        value = GLOBAL_SHARED_STATE.get(key, None)
        return (value,)