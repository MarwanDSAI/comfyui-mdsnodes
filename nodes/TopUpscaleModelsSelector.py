# Marwan Custom Nodes
# Top Upscale Models Selector with Auto-Download & Status. to be connected to the model_name of the Load Upscale Model
# --------------------------------------------------------------
import os
import re
import urllib.request
from tqdm import tqdm
import folder_paths

# Updated exact registry with verified direct download URLs
UPSCALE_MODELS_REGISTRY = {
    "4x-UltraSharp.safetensors": {
        "url": "https://huggingface.co/Kim2091/UltraSharp/resolve/main/4x-UltraSharp.safetensors",
        "directory": "upscale_models"
    },
    "4xRealWebPhoto_v4_dat2.safetensors": {
        "url": "https://huggingface.co/Phips/4xRealWebPhoto_v4_dat2/resolve/main/4xRealWebPhoto_v4_dat2.safetensors",
        "directory": "upscale_models"
    },
    "4xNomos8kDAT.safetensors": {
        "url": "https://huggingface.co/Phips/4xNomos8kDAT/resolve/main/4xNomos8kDAT.safetensors",
        "directory": "upscale_models"
    },
    "4xNomos8k_atd_jpg.safetensors": {
        "url": "https://huggingface.co/Phips/4xNomos8k_atd_jpg/resolve/main/4xNomos8k_atd_jpg.safetensors",
        "directory": "upscale_models"
    },
    "4x_NMKD-Siax_200k.pth": {
        "url": "https://huggingface.co/gemasai/4x_NMKD-Siax_200k/resolve/main/4x_NMKD-Siax_200k.pth",
        "directory": "upscale_models"
    },
    "4x-AnimeSharp.safetensors": {
        "url": "https://huggingface.co/Kim2091/AnimeSharp/resolve/main/4x-AnimeSharp.safetensors",
        "directory": "upscale_models"
    }
    
}


def download_file_with_headers(url, dest_path, filename):
    """Downloads a file with proper browser headers and chunking to avoid blocks/redirect errors."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "*/*"
    }
    req = urllib.request.Request(url, headers=headers)
    
    temp_path = dest_path + ".tmp"
    with urllib.request.urlopen(req) as response:
        total_size = int(response.info().get('Content-Length', 0))
        chunk_size = 1024 * 1024  # 1MB chunks
        
        with open(temp_path, 'wb') as out_file, tqdm(
            desc=f"Downloading {filename}",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024
        ) as bar:
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
                bar.update(len(chunk))
                
    if os.path.exists(dest_path):
        os.remove(dest_path)
    os.rename(temp_path, dest_path)


class MarTopUpscaleModelsSelector:
    DESCRIPTION = "Selects an upscale model, displays availability status at the end, auto-downloads if missing, and outputs the clean filename. To be connected to the model_name of the Load Upscale Model"

    @classmethod
    def get_upscale_dir(cls):
        folder_list = folder_paths.get_folder_paths("upscale_models")
        if folder_list:
            return folder_list[0]
        return os.path.join(folder_paths.models_dir, "upscale_models")

    @classmethod
    def INPUT_TYPES(cls):
        save_dir = cls.get_upscale_dir()
        existing_files = set(os.listdir(save_dir)) if os.path.exists(save_dir) else set()

        dropdown_options = []
        for model_name in UPSCALE_MODELS_REGISTRY.keys():
            status = "[AVAILABLE]" if model_name in existing_files else "[DOWNLOADABLE]"
            # Format: Model name - [STATUS]
            dropdown_options.append(f"{model_name} - {status}")

        return {
            "required": {
                "model_name": (
                    dropdown_options,
                    {
                        "default": dropdown_options[0],
                        "tooltip": "Select an upscale model. If ending in [DOWNLOADABLE], clicking 'Queue Prompt' will auto-download it."
                    }
                ),
            }
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("MODEL_NAME",)
    OUTPUT_NODE = True
    OUTPUT_TOOLTIPS = ("The clean model filename passed forward as a string/universal stream. to be connected to the model_name of the Load Upscale Model",)

    FUNCTION = "get_name"
    CATEGORY = "MDSNodes/utils"

    def get_name(self, model_name):
        # Strip suffix " - [AVAILABLE]" or " - [DOWNLOADABLE]"
        clean_model_name = re.sub(r"\s*-\s*\[.*?\]$", "", str(model_name)).strip()
        # Fallback for old prefix format if already placed in a workflow
        clean_model_name = re.sub(r"^\[.*?\]\s*", "", clean_model_name).strip()
        
        save_dir = self.get_upscale_dir()
        os.makedirs(save_dir, exist_ok=True)
        target_path = os.path.join(save_dir, clean_model_name)
        
        model_info = UPSCALE_MODELS_REGISTRY.get(clean_model_name)
        downloaded = False

        # Download if file is not present in upscale_models
        if not os.path.exists(target_path):
            if not model_info:
                raise FileNotFoundError(f"[MarNodes] Model '{clean_model_name}' not found and has no download configuration.")
            
            url = model_info["url"]
            print(f"\n[MarNodes] Model '{clean_model_name}' is missing. Starting download from: {url}")
            
            try:
                download_file_with_headers(url, target_path, clean_model_name)
                downloaded = True
                print(f"[MarNodes] Download complete: saved to {target_path}\n")
            except Exception as e:
                temp_path = target_path + ".tmp"
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                raise RuntimeError(f"[MarNodes] Failed to download {clean_model_name}: {e}")

        status_text = f"Status: Downloaded successfully" if downloaded else f"Status: Model exists locally ({clean_model_name})"

        return {
            "ui": {"text": [status_text]},
            "result": (clean_model_name,)
        }