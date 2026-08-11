# Marwan Custom Nodes
# ComfyUI Custom Nodes for The Ultimate Model Tester Workflow
# -------------------------------------------------------
# Central node registration for the Marwan Custom Nodes package.
# -------------------------------------------------------
from .nodes.UNetNameToCKPTName import (UNetNameToCKPTName)
from .nodes.ControlNetSelect import (MarControlNetSelect)
from .nodes.RatioList import (MarwanRatioListNode)

NODE_CLASS_MAPPINGS = {
    "UNETNameToCkptName": UNetNameToCKPTName,
    "MarControlNetSelect": MarControlNetSelect,
    "MarwanRatioListNode": MarwanRatioListNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UNETNameToCkptName": "UNET To CKPT Converter",
    "MarControlNetSelect": "ControlNet Select",
    "MarwanRatioListNode": "Ratio List Node",
}


# Expose the mappings so ComfyUI can register the nodes upon server startup
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']