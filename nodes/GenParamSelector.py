# Marwan Custom Nodes
# Central parameter hub that configures and routes checkpoint, steps, refiner steps, CFG, sampler algorithm, scheduler curve, and denoise values across workflows.
# --------------------------------------------------------------
import folder_paths
import comfy.samplers

class MarGenParamSelector:
    # 1. Main Node Description (Shows in Node Search and "Node Info" panel)
    DESCRIPTION = "Central parameter hub that configures and routes checkpoint, steps, refiner steps, CFG, sampler algorithm, scheduler curve, and denoise values across workflows."

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "ckpt_name": (folder_paths.get_filename_list("checkpoints"), {
                    "tooltip": "Select the base checkpoint diffusion model file from your models/checkpoints folder."
                }),
                "steps": ("INT", {
                    "default": 20, 
                    "min": 1, 
                    "max": 10000, 
                    "step": 1, 
                    "tooltip": "The total number of sampling/denoising steps for base generation."
                }),
                "step_refiner": ("INT", {
                    "default": 10, 
                    "min": 0, 
                    "max": 10000, 
                    "step": 1, 
                    "tooltip": "Target step count for refiner passes or the step transition threshold for multi-pass pipelines."
                }),
                "cfg": ("FLOAT", {
                    "default": 7.0, 
                    "min": 0.0, 
                    "max": 100.0, 
                    "step": 0.1, 
                    "round": 0.01, 
                    "tooltip": "Classifier-Free Guidance (CFG) scale. Controls how strictly the model adheres to your prompt."
                }),
                "sampler_name": (comfy.samplers.SAMPLER_NAMES, {
                    "tooltip": "The mathematical sampling algorithm used to generate or denoise the image (e.g., euler, dpmpp_2m)."
                }),
                "scheduler": (comfy.samplers.SCHEDULER_NAMES, {
                    "tooltip": "The noise scheduling rate/curve across the steps (e.g., normal, karras, sgm_uniform, simple)."
                }),
                "denoise": ("FLOAT", {
                    "default": 1.0, 
                    "min": 0.0, 
                    "max": 1.0, 
                    "step": 0.01, 
                    "tooltip": "Denoise strength. Set to 1.0 for initial txt2img generation, or 0.20-0.60 for img2img / upscaling."
                }),
            }
        }

    # Return data types matching native ComfyUI slots
    RETURN_TYPES = (
        folder_paths.get_filename_list("checkpoints"),  # ckpt_name (COMBO)
        "INT",                                          # steps
        "INT",                                          # step_refiner
        "FLOAT",                                        # cfg
        comfy.samplers.SAMPLER_NAMES,                   # sampler_name (COMBO)
        comfy.samplers.SCHEDULER_NAMES,                 # scheduler (COMBO)
        "FLOAT",                                        # denoise
        "STRING",                                       # ckpt_name_str
        "STRING",                                       # sampler_str
        "STRING",                                       # scheduler_str
    )
    
    # Names for each output socket
    RETURN_NAMES = (
        "ckpt_name",
        "steps",
        "step_refiner",
        "cfg",
        "sampler_name",
        "scheduler",
        "denoise",
        "ckpt_name_str",
        "sampler_str",
        "scheduler_str",
    )

    # 2. Output Socket Tooltips (Shows when hovering over individual output pins)
    OUTPUT_TOOLTIPS = (
        "The selected checkpoint filename (COMBO slot for Checkpoint Loaders).",
        "Base generation step count (INT).",
        "Refiner step count or threshold (INT).",
        "Classifier-Free Guidance scale (FLOAT).",
        "Sampler algorithm name (COMBO slot for KSampler / SamplerSelect).",
        "Scheduler curve type (COMBO slot for KSampler / BasicScheduler).",
        "Denoise strength multiplier (FLOAT).",
        "Checkpoint filename exported as a clean plain text string (for metadata/file naming).",
        "Sampler algorithm name exported as a plain text string.",
        "Scheduler type exported as a plain text string.",
    )

    FUNCTION = "get_params"
    CATEGORY = "MDSNodes/sampling"

    def get_params(self, ckpt_name, steps, step_refiner, cfg, sampler_name, scheduler, denoise):
        return (
            ckpt_name,
            steps,
            step_refiner,
            cfg,
            sampler_name,
            scheduler,
            denoise,
            str(ckpt_name),
            str(sampler_name),
            str(scheduler),
        )