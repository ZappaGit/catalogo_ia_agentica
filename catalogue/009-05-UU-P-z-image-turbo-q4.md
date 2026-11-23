<!-- Publishable summary. Full article (Spanish): posts/009-05-UU-P-z-image-turbo-q4.md. Keep in sync. -->

The same 6-billion-parameter image model as article 007, quantized to 4 bits, now draws on a laptop with no graphics card: 8 minutes per image.

This is the quantized version of Z-Image-Turbo. The diffusion model is compressed from 16-bit to about 4 bits per weight, so it fits in the laptop's 16 GB of RAM. It runs with stable-diffusion.cpp, a C/C++ program, under the Apache 2.0 license.

🔧 **Type:** text-to-image diffusion transformer, GGUF Q4_K quantization, Qwen3-4B text encoder. Run on the CPU with stable-diffusion.cpp.
📏 **Size:** 3.86 GB diffusion model, 2.50 GB text encoder, 0.34 GB VAE. 512 × 512 output.
💻 **Minimum hardware:** about **6.2 GB of RAM** for the weights, measured on CPU with no GPU.
🛠️ **Interfaces:** `sd-cli.exe` command line and `sd-server` HTTP server of stable-diffusion.cpp.
🏢 **Behind it:** Tongyi-MAI (Alibaba Group) made the base model; the GGUF quantization is by `leejet`, the author of stable-diffusion.cpp. The quantized repository has 265,885 downloads last month (as of 2026-11-12).

Our families for this one: Paradox · UU tier · Image · Diffusion transformer.

Model card: https://huggingface.co/leejet/Z-Image-Turbo-GGUF

#ImageGeneration #AI #OpenSource
