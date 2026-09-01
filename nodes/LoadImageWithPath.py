# Marwan Custom Nodes
# Loads an image from the input folder and outputs the decoded tensor alpha mask, base filename, absolute file path, and parent directory string.
# -------------------------------------------------------
import os
import torch
import numpy as np
from PIL import Image, ImageOps, ImageSequence
import folder_paths
import node_helpers


class MarLoadImageWithPath:
    def __init__(self):
        pass

    DESCRIPTION = (
        "Loads an image from the input folder and outputs the decoded tensor, "
        "alpha mask, base filename, absolute file path, and parent directory string."
    )

    @classmethod
    def INPUT_TYPES(cls):
        input_dir = folder_paths.get_input_directory()
        files = []
        if os.path.exists(input_dir):
            files = [
                f for f in os.listdir(input_dir)
                if os.path.isfile(os.path.join(input_dir, f))
            ]
        return {
            "required": {
                "image": (
                    sorted(files),
                    {
                        "image_upload": True,
                        "tooltip": "Select an existing image from the input directory or upload a new file."
                    }
                )
            }
        }

    CATEGORY = "MDSNodes/image"
    RETURN_TYPES = ("IMAGE", "MASK", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("IMAGE", "MASK", "filename", "full_path", "directory")

    OUTPUT_TOOLTIPS = (
        "The decoded image tensor (RGB) formatted for VAE, ControlNet, or upscalers.",
        "The alpha transparency mask channel (inverted for inpainting).",
        "The clean file name including extension (e.g., photo.png).",
        "The full absolute file path on disk (e.g., E:\\ComfyUI\\ComfyUI\\input\\photo.png).",
        "The parent folder directory path where the image is stored."
    )

    FUNCTION = "load_image"

    @classmethod
    def VALIDATE_INPUTS(cls, image):
        # Always return True to bypass ComfyUI's pre-execution "value not available" check
        return True

    def _empty_fallback(self):
        """Returns empty placeholder image, mask, and blank path strings."""
        empty_image = torch.zeros((1, 64, 64, 3), dtype=torch.float32, device="cpu")
        empty_mask = torch.zeros((1, 64, 64), dtype=torch.float32, device="cpu")
        return (empty_image, empty_mask, "", "", "")

    def load_image(self, image):
        if not image:
            return self._empty_fallback()

        try:
            image_path = folder_paths.get_annotated_filepath(image)
        except Exception:
            return self._empty_fallback()

        # Check if the resolved file actually exists on disk
        if not image_path or not os.path.isfile(image_path):
            return self._empty_fallback()

        try:
            img = node_helpers.pillow(Image.open, image_path)
            
            output_images = []
            output_masks = []
            w, h = None, None

            for i in ImageSequence.Iterator(img):
                i = node_helpers.pillow(ImageOps.exif_transpose, i)

                if i.mode == "I":
                    i = i.point(lambda i: i * (1 / 255))
                
                image_rgb = i.convert("RGB")

                if len(output_images) == 0:
                    w = image_rgb.size[0]
                    h = image_rgb.size[1]
                
                if image_rgb.size[0] != w or image_rgb.size[1] != h:
                    continue
                
                image_tensor = np.array(image_rgb).astype(np.float32) / 255.0
                image_tensor = torch.from_numpy(image_tensor)[None,]
                
                # Extract alpha transparency mask channel
                if "A" in i.getbands():
                    mask = np.array(i.getchannel("A")).astype(np.float32) / 255.0
                    mask = 1.0 - torch.from_numpy(mask)
                else:
                    mask = torch.zeros((64, 64), dtype=torch.float32, device="cpu")
                
                output_images.append(image_tensor)
                output_masks.append(mask.unsqueeze(0))

            if not output_images:
                return self._empty_fallback()

            if len(output_images) > 1:
                output_image = torch.cat(output_images, dim=0)
                output_mask = torch.cat(output_masks, dim=0)
            else:
                output_image = output_images[0]
                output_mask = output_masks[0]

            filename = os.path.basename(image_path)
            directory = os.path.dirname(image_path)
            full_path = os.path.abspath(image_path)

            return (output_image, output_mask, str(filename), str(full_path), str(directory))

        except Exception:
            return self._empty_fallback()

    @classmethod
    def IS_CHANGED(cls, image):
        try:
            image_path = folder_paths.get_annotated_filepath(image)
            if os.path.isfile(image_path):
                m = node_helpers.pillow(Image.open, image_path)
                return float("nan")
        except Exception:
            pass
        return ""