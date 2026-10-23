# ComfyUI-MDSNodes
# ---------------------------------------------------
import logging
version_code = [1, 8, 0]
version_str = f"V{version_code[0]}.{version_code[1]}" + (f'.{version_code[2]}' if len(version_code) > 2 else '')
logging.info(f"### Loading: ComfyUI-MDSNodes ({version_str})")
# ---------------------------------------------------
from .nodes.RatioCombobox import MarRatioCombobox                       # First Node
from .nodes.UNetNameToCKPTName import MarUNetNameToCKPTName
from .nodes.ControlNetSelect import MarControlNetSelect
from .nodes.LoadImageWithPath import MarLoadImageWithPath               # Added v1.0.9 8/18/26
from .nodes.SelectDiffusionModel import MarSelectDiffusionModel         # Added v1.0.9
from .nodes.TopUpscaleModelsSelector import MarTopUpscaleModelsSelector # Added v1.0.9
from .nodes.GenParamSelector import MarGenParamSelector                 # Added v1.0.9
from .nodes.LoadCheckpointHubPro import MarLoadCheckpointHubPro         # Added v1.0.14 8/23/26; Updated v1.8.0 
from .nodes.LoadDiffusionHubPro import MarLoadDiffusionHubPro           # Added v1.0.14; Updated v1.8.0
from .nodes.MergeTwoStrings import MarMergeTwoStrings                   # Added v1.1.0 8/25/26 
from .nodes.CStr import MarCStr                                         # Added v1.1.0
# -------------------MetaData-----------------------       
from .nodes.MetaData import MarMetaDataAppend                           # Added v1.3.0 8/26/26 
from .nodes.MetaData import MarMetaDataRemove                           # Added v1.8.0
from .nodes.MetaDataExtract import MarMetaDataExtract                   # Added v1.3.0
from .nodes.MetaDataToJSON import MarMetaDataToJSON                     # Added v1.3.0
from .nodes.UnloadAllModels import MarUnloadAllModels                   # Added v1.3.0
from .nodes.UMTWComboCustomPromptSelector import MarUMTWComboCustomPromptSelector # Added v1.5.0 9/03/26 
from .nodes.ModelShortHashExtractor import MarModelShortHashExtractor   # Added v1.6.0 9/03/26 
from .nodes.MetaDataCheckKeyValue import MarMetaDataCheckKeyValue       # Added v1.7.0 9/07/26 
from .nodes.IntSwitch import MarIntSwitch                               # Added v1.7.0  
from .nodes.MetaDataAppendSwitch import MarMetaDataAppendSwitch         # Added v1.8.0 9/15/26 
from .nodes.StrSwitch import MarStrSwitch                               # Added v1.8.0  
from .nodes.StrMultilineSwitch import MarStrMultilineSwitch             # Added v1.8.0  
from .nodes.Float2Switch import MarFloat2Switch                         # Added v1.8.0  
from .nodes.IsEmpty import MarIsEmpty                                   # Added v1.8.0  
from .nodes.SetGetValue import MarSetValue                              # Added v1.8.0  
from .nodes.SetGetValue import MarGetValue                              # Added v1.8.0  
from .nodes.EmptyVariables import MarEmptyVariables                     # Added v1.8.0  
from .nodes.TextMultilineDual import MarTextMultilineDual               # Added v1.8.0  
from .nodes.KeyValueSelector8 import MarKeyValueSelector8               # Added v1.8.0
from .nodes.ModelSwitch import MarModelSwitch                           # Added v1.8.0    
from .nodes.StrTrimFallback import MarStrTrimFallback                   # Added v1.8.0    
# -------------String Replace------------------------
from .nodes.StrReplace import MarStrReplaceMultiple                     # Added v1.8.0
from .nodes.StrReplace import MarStrReplaceSingle                       # Added v1.8.0
# -------------Variables-----------------------------
from .nodes.Variables import MarInteger                                 # Added v1.8.0
from .nodes.Variables import MarFloatNoDec                              # Added v1.8.0  
from .nodes.Variables import MarFloatOneDec                             # Added v1.8.0  
from .nodes.Variables import MarFloatTwoDec                             # Added v1.8.0
from .nodes.Variables import MarGuideSize                               # Added v1.8.0
from .nodes.Variables import MarDenoise                                 # Added v1.8.0
from .nodes.Variables import MarFeather                                 # Added v1.8.0
from .nodes.Variables import MarBBoxCropFactor                          # Added v1.8.0

# -------------Math----------------------------------
from .nodes.Math import MarRound                                        # Added v1.8.0     
# ---------------------------------------------------
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
    #----MetaData--------------------------------------
    "MarMetaDataAppend": MarMetaDataAppend,
    "MarMetaDataRemove": MarMetaDataRemove,
    "MarMetaDataExtract": MarMetaDataExtract,
    "MarMetaDataToJSON": MarMetaDataToJSON,
    # -------------------------------------------------
    "MarUnloadAllModels": MarUnloadAllModels,
    "MarUMTWComboCustomPromptSelector": MarUMTWComboCustomPromptSelector,
    "MarModelShortHashExtractor": MarModelShortHashExtractor,
    "MarMetaDataCheckKeyValue": MarMetaDataCheckKeyValue,
    "MarIntSwitch": MarIntSwitch,
    "MarMetaDataAppendSwitch": MarMetaDataAppendSwitch,
    "MarStrSwitch": MarStrSwitch,
    "MarStrMultilineSwitch": MarStrMultilineSwitch,
    "MarFloat2Switch": MarFloat2Switch,
    "MarIsEmpty": MarIsEmpty,
    "MarSetValue": MarSetValue,
    "MarGetValue": MarGetValue,
    "MarEmptyVariables": MarEmptyVariables,
    "MarTextMultilineDual": MarTextMultilineDual,
    "MarStrTrimFallback": MarStrTrimFallback,
    # -------------String Replace-----------
    "MarStrReplaceMultiple": MarStrReplaceMultiple,
    "MarStrReplaceSingle": MarStrReplaceSingle,
    # -------------Variables----------------
    "MarInteger": MarInteger,
    "MarFloatNoDec": MarFloatNoDec,
    "MarFloatOneDec": MarFloatOneDec,
    "MarFloatTwoDec": MarFloatTwoDec,
    "MarGuideSize": MarGuideSize,
    "MarDenoise": MarDenoise,
    "MarFeather": MarFeather,
    "MarBBoxCropFactor": MarBBoxCropFactor,
    # --------------------------------------
    "MarRound": MarRound,
    "MarKeyValueSelector8": MarKeyValueSelector8,
    "MarModelSwitch": MarModelSwitch,
    
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
    #----MetaData--------------------------------------
    "MarMetaDataAppend": "Metadata Append",
    "MarMetaDataRemove": "MetaData Remove",
    "MarMetaDataExtract": "MetaData Extract",
    "MarMetaDataToJSON": "MetaData Convert to EXTRA_METADATA",
    "MarUnloadAllModels": "Unload All Models",
    "MarUMTWComboCustomPromptSelector": "UMTW Custom Prompt Selector",
    "MarModelShortHashExtractor": "Model Short Hash Extractor",
    "MarMetaDataCheckKeyValue": "MetaData Check Key & Value",
    "MarIntSwitch": "Integer Switch",
    "MarMetaDataAppendSwitch": "MetaData Append (Switch)",
    "MarStrSwitch": "String Switch",
    "MarStrMultilineSwitch": "String Switch (Multiline)",
    "MarFloat2Switch": "Float Switch (2 decimal)",
    "MarIsEmpty": "Is Empty",
    "MarSetValue": "Set Value (Global)",
    "MarGetValue": "Get Value (Global)",
    "MarEmptyVariables": "Empty",
    "MarTextMultilineDual": "Text (Multiline) Dual",
    "MarStrTrimFallback": "String Trim Fallback",
    # --------------------------------------
    "MarStrReplaceMultiple": "String Replace (Multiple)",
    "MarStrReplaceSingle": "String Replace",
    "MarInteger": "Integer",
    "MarFloatNoDec": "Float (No Dec)",
    "MarFloatOneDec": "Float (1 Dec)",
    "MarFloatTwoDec": "Float (2 Dec)",
    "MarGuideSize": "Guide Size",
    "MarDenoise": "Denoise",
    "MarFeather": "Feather Radius",
    "MarBBoxCropFactor": "BBox Crop Factor",
    "MarRound": "Round",
    "MarKeyValueSelector8": "String Selector by Key (8 Strings)",
    "MarModelSwitch": "Model Switch",  
}
# -----------------------------------------------------------
# Points ComfyUI to frontend folder 
# WEB_DIRECTORY = "./web"
# -----------------------------------------------------------
# Expose the mappings so ComfyUI can register the nodes upon server startup
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
