<!-- Publishable summary. Full article (Spanish): posts/007-05-UU-P-z-image-turbo.md. Keep in sync. -->

A 6-billion-parameter image model that draws in 8 steps, where its base version needs 50.

Z-Image-Turbo is a text-to-image model from Alibaba's Tongyi-MAI team. It is a distilled version of Z-Image: the same model, trained to reach the result in far fewer steps. It is open-source, under the Apache 2.0 license.

🔧 **Type:** text-to-image diffusion transformer, distilled to 8 steps. Used from Python with Hugging Face Diffusers.
📏 **Size:** 6.15B parameters, bilingual prompts (English and Chinese), safetensors weights.
💻 **Minimum hardware:** about **16 GB of VRAM** on a consumer GPU, as the model card states (our estimate of the weights alone: about 12.3 GB in BF16).
🛠️ **Interfaces:** Python with `ZImagePipeline` in Diffusers, desktop apps such as Draw Things and DiffusionBee, and hosted inference through fal.
🏢 **Behind it:** the Tongyi-MAI organization at Alibaba Group. Its 723,000 downloads (as of 2026-11-10) show wide reach.

Our families for this one: Paradox · UU tier · Image · Diffusion transformer.

Model card: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
