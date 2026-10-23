# Marwan Custom Nodes
# -----------------------------------------------------------------------------
class MarInteger:
    DESCRIPTION = "Outputs a fixed integer constant."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "int_val": ("INT", {
                    "default": 0,
                    "min": -0xffffffffffffffff,
                    "max": 0xffffffffffffffff,
                    "step": 1,
                    "tooltip": "Integer value (whole number)."
                }),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("Integer",)
    OUTPUT_TOOLTIPS = ("The fixed integer value.",)
    FUNCTION = "get_value"
    CATEGORY = "MDSNodes/Constants"

    def get_value(self, int_val):
        return (int(int_val),)
# -----------------------------------------------------------------------------
class MarFloatNoDec:
    DESCRIPTION = "Outputs a fixed float constant with no decimal places."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_val": ("FLOAT", {
                    "default": 0.0,
                    "min": -1e15,
                    "max": 1e15,
                    "step": 1.0,        # Increases/decreases by whole numbers
                    "round": 1.0,       # Snaps dragged values to whole numbers
                    "precision": 0,     # Suppresses decimal places in the UI
                    "tooltip": "Float with no decimal places."
                }),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT",)
    FUNCTION = "get_value"
    CATEGORY = "MDSNodes/Constants"

    def get_value(self, float_val):
        # Enforce an integer conversion in Python before converting to float
        return (float(int(round(float_val))),)
# -----------------------------------------------------------------------------
class MarFloatOneDec:
    DESCRIPTION = "Outputs a fixed float constant with one decimal place."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_val": ("FLOAT", {
                    "default": 0.0,
                    "min": -0xffffffffffffffff,
                    "max": 0xffffffffffffffff,
                    "step": 0.1,
                    "tooltip": "Float with one decimal place."
                }),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT",)
    OUTPUT_TOOLTIPS = ("The float value with 1 decimal.",)
    FUNCTION = "get_value"
    CATEGORY = "MDSNodes/Constants"

    def get_value(self, float_val):
        return (float(float_val),)
# -----------------------------------------------------------------------------
class MarFloatTwoDec:
    DESCRIPTION = "Outputs a fixed float constant with two decimal places."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_val": ("FLOAT", {
                    "default": 0.00,
                    "min": -0xffffffffffffffff,
                    "max": 0xffffffffffffffff,
                    "step": 0.01,
                    "tooltip": "Float with two decimal places."
                }),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("FLOAT",)
    OUTPUT_TOOLTIPS = ("The float value with 2 decimals.",)
    FUNCTION = "get_value"
    CATEGORY = "MDSNodes/Constants"

    def get_value(self, float_val):
        return (float(float_val),)
# -----------------------------------------------------------------------------
class MarGuideSize:
    DESCRIPTION = "Outputs a guide size constant for sizing bounding boxes/crops."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "guide_size": ("INT", {
                    "default": 512,
                    "min": 64,
                    "max": 8192,
                    "step": 8,
                    "tooltip": "Target guide resolution/size."
                }),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("guide_size",)
    OUTPUT_TOOLTIPS = ("The guide size integer value.",)
    FUNCTION = "get_value"
    CATEGORY = "MDSNodes/Constants"

    def get_value(self, guide_size):
        return (int(guide_size),)
# -----------------------------------------------------------------------------
class MarDenoise:
    DESCRIPTION = "Outputs a denoise strength constant (0.0 to 1.0)."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "denoise": ("FLOAT", {
                    "default": 0.50,
                    "min": 0.00,
                    "max": 1.00,
                    "step": 0.01,
                    "round": 0.01,
                    "tooltip": "Denoising strength factor."
                }),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("denoise",)
    OUTPUT_TOOLTIPS = ("The denoise float value.",)
    FUNCTION = "get_value"
    CATEGORY = "MDSNodes/Constants"

    def get_value(self, denoise):
        return (round(float(denoise), 2),)
# -----------------------------------------------------------------------------
class MarFeather:
    DESCRIPTION = "Outputs a mask feathering/blend radius constant."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "feather": ("INT", {
                    "default": 10,
                    "min": 0,
                    "max": 100,
                    "step": 1,
                    "tooltip": "Feather radius in pixels for blending."
                }),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("feather",)
    OUTPUT_TOOLTIPS = ("The feather radius integer value.",)
    FUNCTION = "get_value"
    CATEGORY = "MDSNodes/Constants"

    def get_value(self, feather):
        return (int(feather),)
# -----------------------------------------------------------------------------
class MarBBoxCropFactor:
    DESCRIPTION = "Outputs a bounding box padding/expansion crop factor multiplier."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "bbox_crop_factor": ("FLOAT", {
                    "default": 1.50,
                    "min": 1.0,
                    "max": 10.0,
                    "step": 0.1,
                    "round": 0.1,
                    "tooltip": "Multiplier for bounding box crop context/expansion."
                }),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("bbox_crop_factor",)
    OUTPUT_TOOLTIPS = ("The bbox crop factor float value.",)
    FUNCTION = "get_value"
    CATEGORY = "MDSNodes/Constants"

    def get_value(self, bbox_crop_factor):
        return (round(float(bbox_crop_factor), 2),)
# -----------------------------------------------------------------------------