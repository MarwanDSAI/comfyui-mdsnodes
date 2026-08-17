# Marwan Custom Nodes
# ComfyUI Custom Nodes for The Ultimate Model Tester Workflow
# -------------------------------------------------------
"""
@author: Marwan
@title: ComfyUI-MDSNodes
@nickname: ComfyUI-MDSNodes
@description: Custom Nodes for The Ultimate Model Tester Workflow
"""
# -------------------------------------------------------
version_code = [1, 0, 0]
version_str = f"V{version_code[0]}.{version_code[1]}" + (f'.{version_code[2]}' if len(version_code) > 2 else '')
logging.info(f"### Loading: ComfyUI-MDSNodes ({version_str})")
# -------------------------------------------------------
from .nodes.UNetNameToCKPTName import MarUNetNameToCKPTName
from .nodes.ControlNetSelect import MarControlNetSelect
from .nodes.RatioCombobox import MarRatioCombobox
# -------------------------------------------------------
# Map internal unique string IDs to Python classes
NODE_CLASS_MAPPINGS = {
    "MarUNetNameToCKPTName": MarUNetNameToCKPTName,
    "MarControlNetSelect": MarControlNetSelect,
    "MarRatioCombobox": MarRatioCombobox,
}
# -------------------------------------------------------
# Map internal string IDs to the friendly titles shown on the canvas
NODE_DISPLAY_NAME_MAPPINGS = {
    "MarUNetNameToCKPTName": "UNET To CKPT Converter",
    "MarControlNetSelect": "ControlNet Select",
    "MarRatioCombobox": "Ratio Combobox",
}
# -------------------------------------------------------
# Expose the mappings so ComfyUI can register the nodes upon server startup
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
