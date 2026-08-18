# Marwan Custom Nodes
# Like known Loadimage but with image file name output  
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

    # 1. Main Node Description (Shows in Node Search and "Node Info" panel)
    DESCRIPTION = (
        "Loads an image from the input folder and outputs the decoded tensor, "
        "alpha mask, base filename, absolute file path, and parent directory string."
    )

    @classmethod
    def INPUT_TYPES(cls):
        input_dir = folder_paths.get_input_directory()
        files = [
            f for f in os.listdir(input_dir)
            if os.path.isfile(os.path.join(input_dir, f))
        ]
        return {
            "required": {
                # 2. Input Parameter / Widget Tooltip
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

    # 3. Output Pin Tooltips (Shows when hovering over individual output pins)
    OUTPUT_TOOLTIPS = (
        "The decoded image tensor (RGB) formatted for VAE, ControlNet, or upscalers.",
        "The alpha transparency mask channel (inverted for inpainting).",
        "The clean file name including extension (e.g., photo.png).",
        "The full absolute file path on disk (e.g., E:\\ComfyUI\\ComfyUI\\input\\photo.png).",
        "The parent folder directory path where the image is stored."
    )

    FUNCTION = "load_image"

    def load_image(self, image):
        # Resolve full annotated path
        image_path = folder_paths.get_annotated_filepath(image)
        
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

        if len(output_images) > 1:
            output_image = torch.cat(output_images, dim=0)
            output_mask = torch.cat(output_masks, dim=0)
        else:
            output_image = output_images[0]
            output_mask = output_masks[0]

        # Extract file naming and directory strings
        filename = os.path.basename(image_path)
        directory = os.path.dirname(image_path)
        full_path = os.path.abspath(image_path)

        return (output_image, output_mask, str(filename), str(full_path), str(directory))

    @classmethod
    def IS_CHANGED(cls, image):
        image_path = folder_paths.get_annotated_filepath(image)
        m = node_helpers.pillow(Image.open, image_path)
        return float("nan")


# Registration Mappings
NODE_CLASS_MAPPINGS = {
    "MarLoadImageWithPath": MarLoadImageWithPath
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MarLoadImageWithPath": "Load Image (With Path)"
}