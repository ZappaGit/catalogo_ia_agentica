<!-- Publishable summary. Full article (Spanish): posts/008-05-NU-S-stable-diffusion-1-5.md. Keep in sync. -->

The model that made local image generation popular, run on a laptop with no graphics card: one image took 7 minutes.

Stable Diffusion 1.5 is a text-to-image model with about 0.9 billion parameters. It turns a written description into a picture by removing noise step by step in a compressed space. It is open-source, under the CreativeML OpenRAIL-M license, which has use restrictions.

🔧 **Type:** latent diffusion (U-Net denoiser, CLIP text encoder, VAE decoder). Run with stable-diffusion.cpp, a C/C++ runtime.
📏 **Size:** about 0.9B parameters, 4.27 GB weight file, 512 × 512 output.
💻 **Minimum hardware:** 2.78 GB of weights in RAM, CPU only, no GPU needed (measured on a 15.7 GB laptop).
🛠️ **Interfaces:** `sd-cli.exe` command line, `sd-server` HTTP server, Python with `diffusers` (not tested here).
🏢 **Behind it:** the `stable-diffusion-v1-5` account on Hugging Face, a mirror of the deprecated `runwayml` repository. It has 1,019,121 downloads last month (as of 2026-11-12).

Our families for this one: Starter · NU tier · Diffusion · Stable Diffusion 1.x line.

Model card: https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5

#ImageGeneration #AI #OpenSource
