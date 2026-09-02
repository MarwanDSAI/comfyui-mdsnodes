# ComfyUI-MDSNodes
# -----------------------------------------------------------
import logging
version_code = [1, 3, 1]
version_str = f"V{version_code[0]}.{version_code[1]}" + (f'.{version_code[2]}' if len(version_code) > 2 else '')
logging.info(f"### Loading: ComfyUI-MDSNodes ({version_str})")
# -----------------------------------------------------------
from .nodes.UNetNameToCKPTName import MarUNetNameToCKPTName
from .nodes.ControlNetSelect import MarControlNetSelect
from .nodes.RatioCombobox import MarRatioCombobox
from .nodes.LoadImageWithPath import MarLoadImageWithPath
from .nodes.SelectDiffusionModel import MarSelectDiffusionModel
from .nodes.TopUpscaleModelsSelector import MarTopUpscaleModelsSelector
from .nodes.GenParamSelector import MarGenParamSelector
from .nodes.LoadCheckpointHubPro import MarLoadCheckpointHubPro
from .nodes.LoadDiffusionHubPro import MarLoadDiffusionHubPro
from .nodes.MergeTwoStrings import MarMergeTwoStrings               # Added 8/25/26 v1.1.0
from .nodes.CStr import MarCStr                                     # Added 8/25/26 v1.1.0
from .nodes.MetaDataAppend import MarMetaDataAppend                 # Added 8/26/26 v1.3.0
from .nodes.MetaDataExtract import MarMetaDataExtract               # Added 8/31/26 v1.3.0
from .nodes.MetaDataToJSON import MarMetaDataToJSON                 # Added 8/31/26 v1.3.0
from .nodes.UnloadAllModels import MarUnloadAllModels               # Added 8/31/26 v1.3.0
# -----------------------------------------------------------
# Map internal unique string IDs to Python classes
NODE_CLASS_MAPPINGS = {
    "MarUNetNameToCKPTName": MarUNetNameToCKPTName,
    "MarControlNetSelect": MarControlNetSelect,
    "MarRatioCombobox": MarRatioCombobox,
    "MarLoadImageWithPath": MarLoadImageWithPath,
    "MarSelectDiffusionModel": MarSelectDiffusionModel,
    "MarTopUpscaleModelsSelector": MarTopUpscaleModelsSelector,
    "MarGenParamSelector": MarGenParamSelector,
    "MarLoadCheckpointHubPro": MarLoadCheckpointHubPro,
    "MarLoadDiffusionHubPro": MarLoadDiffusionHubPro,
    "MarMergeTwoStrings": MarMergeTwoStrings,
    "MarCStr": MarCStr,
    "MarMetaDataAppend": MarMetaDataAppend,
    "MarMetaDataExtract": MarMetaDataExtract,
    "MarMetaDataToJSON": MarMetaDataToJSON,
    "MarUnloadAllModels": MarUnloadAllModels
}
# -----------------------------------------------------------
# Map internal string IDs to the friendly titles shown on the canvas
NODE_DISPLAY_NAME_MAPPINGS = {
    "MarUNetNameToCKPTName": "UNET To CKPT Converter",
    "MarControlNetSelect": "ControlNet Select",
    "MarRatioCombobox": "Ratio Combobox",
    "MarLoadImageWithPath": "Load Image (With Path)",
    "MarSelectDiffusionModel": "Select Diffusion Model",
    "MarTopUpscaleModelsSelector": "Top Upscale Models Selector (Auto-DL)",
    "MarGenParamSelector": "Generation Parameters Hub",
    "MarLoadCheckpointHubPro": "Load Checkpoint Hub Pro",
    "MarLoadDiffusionHubPro": "Load Diffusion Model Hub Pro",
    "MarMergeTwoStrings": "Merge Two Strings",
    "MarCStr": "Convert to String",
    "MarMetaDataAppend": "Metadata Append",
    "MarMetaDataExtract": "MetaData Extract",
    "MarMetaDataToJSON": "MetaData Convert to EXTRA_METADATA",
    "MarUnloadAllModels": "Unload All Models"
}
# -----------------------------------------------------------
# Points ComfyUI to frontend folder 
WEB_DIRECTORY = "./web"
# -----------------------------------------------------------
# Expose the mappings so ComfyUI can register the nodes upon server startup
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
