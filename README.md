## ComfyUI-MDSNodes V1.0.9

the following custom nodes was build to use with my Ultimate Model Tester Workflow. They may also be useful for your own workflows.

## Nodes:

- **Load Image (With Path)** 
  Loads an image and outputs its decoded IMAGE, MASK, filename, full_path, and directory.

- **Top Upscale Models Selector (Auto-DL)** 
  Selects top upscale models (e.g., 4x-UltraSharp, 4xRealWebPhoto) and auto-downloads missing files when queued.

- **ControlNet Select** 
  Selects a ControlNet model and outputs its filename as both a standard string and a wildcard/combo connection.

- **Select Diffusion Model** 
  Selects a UNET/Diffusion model and passes its filename as CKPT_NAME and UNET_NAME (useful for context routing).

- **UNet Name to CKPT Name** 
  Routes a UNET model filename into nodes expecting CKPT_NAME (such as rgthree context nodes).

- **Ratio Combobox**
  Dropdown of common percentage presets (10%, 25%, 50%, 100%) converted directly into decimal FLOAT values (e.g., 0.5).


## Requirements:
No extra packages required. Works out-of-the-box with standard ComfyUI dependencies.

## How To Install?
Install via ComfyUI Node Manager: Search 'ComfyUI-MDSNodes' in ComfyUI Node Manager and click Install button.
