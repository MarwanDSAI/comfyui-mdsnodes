# Marwan Custom Nodes Version 1.1.1
# ComfyUI Custom Nodes for The Ultimate Model Tester Workflow
# -------------------------------------------------------
# Central node registration for the package.
# -------------------------------------------------------
from .nodes.UNetNameToCKPTName import UNetNameToCKPTName
from .nodes.ControlNetSelect import MarControlNetSelect
from .nodes.RatioCombobox import MarRatioCombobox
# -------------------------------------------------------
# Map internal unique string IDs to Python classes
NODE_CLASS_MAPPINGS = {
    "UNetNameToCKPTName": UNetNameToCKPTName,
    "MarControlNetSelect": MarControlNetSelect,
    "MarRatioCombobox": MarRatioCombobox,
}
# -------------------------------------------------------
# Map internal string IDs to the friendly titles shown on the canvas
NODE_DISPLAY_NAME_MAPPINGS = {
    "UNetNameToCKPTName": "UNET To CKPT Converter",
    "MarControlNetSelect": "ControlNet Select",
    "MarRatioCombobox": "Ratio Combobox",
}
# -------------------------------------------------------
# Expose the mappings so ComfyUI can register the nodes upon server startup
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
