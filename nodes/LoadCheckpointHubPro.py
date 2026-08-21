# Marwan Custom Nodes
# Central parameter hub that loads a checkpoint and routes MODEL, CLIP, VAE, 
# sampling settings, prompts, and metadata across workflows.
# --------------------------------------------------------------
import folder_paths
import comfy.sd
import comfy.samplers

class MarLoadCheckpointHubPro:
    DESCRIPTION = "Central parameter hub that loads a checkpoint and routes MODEL, CLIP, VAE, steps, refiner steps, CFG, sampler algorithm, scheduler curve, denoise values, positive/negative prompts, and metadata across workflows."

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
                "positive_prompt": ("STRING", {
                    "default": "", 
                    "multiline": True,
                    "dynamicPrompts": True,
                    "tooltip": "Enter positive prompt text. Expanding the node will enlarge this text box."
                }),
                "negative_prompt": ("STRING", {
                    "default": "", 
                    "multiline": True,
                    "dynamicPrompts": True,
                    "tooltip": "Enter negative prompt text. Expanding the node will enlarge this text box."
                }),
                "metadata": ("STRING", {
                    "default": "", 
                    "multiline": False, 
                    "tooltip": "Single-line metadata text or workflow tags to pass downstream."
                }),
            }
        }

    # Output data types
    RETURN_TYPES = (
        "MODEL",
        "CLIP",
        "VAE",
        "INT",                                          # steps
        "INT",                                          # step_refiner
        "FLOAT",                                        # cfg
        folder_paths.get_filename_list("checkpoints"),  # ckpt_name (COMBO)
        comfy.samplers.SAMPLER_NAMES,                   # sampler_name (COMBO)
        comfy.samplers.SCHEDULER_NAMES,                 # scheduler (COMBO)
        "FLOAT",                                        # denoise
        "STRING",                                       # positive_prompt
        "STRING",                                       # negative_prompt
        "STRING",                                       # metadata
    )
    
    # Output pin labels
    RETURN_NAMES = (
        "MODEL",
        "CLIP",
        "VAE",
        "steps",
        "step_refiner",
        "cfg",
        "ckpt_name",
        "sampler_name",
        "scheduler",
        "denoise",
        "positive_prompt",
        "negative_prompt",
        "metadata",
    )

    # Hover tooltips for output pins
    OUTPUT_TOOLTIPS = (
        "The loaded diffusion model.",
        "The loaded CLIP model for text encoding.",
        "The loaded VAE model for image encoding/decoding.",
        "Base generation step count (INT).",
        "Refiner step count or threshold (INT).",
        "Classifier-Free Guidance scale (FLOAT).",
        "The selected checkpoint filename (COMBO slot for external Checkpoint Loaders).",
        "Sampler algorithm name (COMBO slot for KSampler / SamplerSelect).",
        "Scheduler curve type (COMBO slot for KSampler / BasicScheduler).",
        "Denoise strength multiplier (FLOAT).",
        "Positive prompt string (connect to CLIP Text Encode).",
        "Negative prompt string (connect to CLIP Text Encode).",
        "Passthrough metadata string.",
    )

    FUNCTION = "load_and_get_params"
    CATEGORY = "MDSNodes/sampling"

    def load_and_get_params(
        self, 
        ckpt_name, 
        steps, 
        step_refiner, 
        cfg, 
        sampler_name, 
        scheduler, 
        denoise, 
        positive_prompt, 
        negative_prompt, 
        metadata
    ):
        # Resolve full path and load checkpoint components
        ckpt_path = folder_paths.get_full_path("checkpoints", ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(
            ckpt_path, 
            output_vae=True, 
            output_clip=True, 
            embedding_directory=folder_paths.get_folder_paths("embeddings")
        )
        
        # Unpack loaded components (MODEL, CLIP, VAE)
        model = out[0]
        clip = out[1]
        vae = out[2]

        return (
            model,
            clip,
            vae,
            steps,
            step_refiner,
            cfg,
            ckpt_name,
            sampler_name,
            scheduler,
            denoise,
            str(positive_prompt),
            str(negative_prompt),
            str(metadata),
        )


# Registration Mappings
NODE_CLASS_MAPPINGS = {
    "MarLoadCheckpointHubPro": MarLoadCheckpointHubPro
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MarLoadCheckpointHubPro": "Load Checkpoint Hub Pro"
}