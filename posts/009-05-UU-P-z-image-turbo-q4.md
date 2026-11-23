# 009 · Z-Image-Turbo Q4 (GGUF, stable-diffusion.cpp)

**Main source (quantized model):** https://huggingface.co/leejet/Z-Image-Turbo-GGUF
**Base model:** https://huggingface.co/Tongyi-MAI/Z-Image-Turbo (see article 007)
**Text encoder:** https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF (Q4_K_M)
**VAE:** `ae.safetensors` from https://huggingface.co/Comfy-Org/z_image_turbo (see Pending)
**Runtime:** stable-diffusion.cpp, release `master-1091-b9d7176`, https://github.com/leejet/stable-diffusion.cpp (MIT)
**License:** Apache 2.0 (base model, quantized files and text encoder; the VAE repository is also Apache 2.0)
**Consulted:** 2026-11-12
**Code:** 05-UU-P-009 (catalogue 05 Image, video and 3D · UU · Paradox: a quantized variant of a known model)
**Origin:** follow-up of article 007 (Z-Image-Turbo). Chosen to test whether the 6 B model runs on this laptop once it is quantized.
**Families:** Paradox · UU · Diffusion transformer (DiT) · quantized (GGUF Q4_K) version of Z-Image-Turbo (see the "Families" section)

---

## Summary

The same 6-billion-parameter image model as article 007, quantized to 4 bits, now draws on a laptop with no graphics card: 8 minutes per image.

This is the quantized version of Z-Image-Turbo. The diffusion model is compressed from 16-bit to about 4 bits per weight, so it fits in the laptop's 16 GB of RAM. It is run with stable-diffusion.cpp, a C/C++ program, under the Apache 2.0 license.

🔧 **Type and technology:** text-to-image diffusion transformer, GGUF Q4_K quantization, with a Qwen3-4B text encoder (Q4_K_M) and the FLUX-style VAE. Run with the C/C++ runtime stable-diffusion.cpp on the CPU.
📏 **Size:** diffusion model 3.86 GB (Q4_K), text encoder 2.50 GB, VAE 0.34 GB. Output 512 × 512 pixels.
💻 **Minimum hardware:** **about 6.2 GB of RAM** for the weights, measured on CPU with no GPU. Our test machine has 15.7 GB of RAM and no CUDA.
🛠️ **Interfaces:** the `sd-cli.exe` command line of stable-diffusion.cpp, and its `sd-server` HTTP server. ComfyUI: not tested here.
👥 **Who uses it and for what:** the quantized repository has 265,885 downloads in the last month (as of 2026-11-12); the card names no companies or projects.
💡 **Why it matters:** it is the first 6-billion-parameter image model in this series that runs on this laptop. The cost is time: one image of 8 steps took 480 s. The base model, which needs a GPU, is faster *(our measurement; the base model was not run here)*.
🏢 **Behind the model:** Tongyi-MAI (Alibaba Group) made the base model. The GGUF quantization is by `leejet`, the author of stable-diffusion.cpp.
🤓 **Curiosity:** the image on this run is a clean red ring on a white background, which is closer to the prompt than the dark, textured result of Stable Diffusion 1.5 in article 008.

Model card: https://huggingface.co/leejet/Z-Image-Turbo-GGUF

---

## What it is

Z-Image-Turbo Q4 is the **same model as article 007**, stored with 4-bit weights in GGUF format. It is a text-to-image model: it takes a prompt and returns an image. The quantization reduces the memory the model needs; it does not change what the model does.

The full run also needs a text encoder (Qwen3-4B, which turns the prompt into numbers the model can use) and a VAE (which turns the final latent into pixels). Those two parts are separate files.

## Type and technology

- **Task:** text-to-image generation.
- **Architecture:** a diffusion transformer (DiT) with 30 layers, hidden size 3840 and 30 attention heads (from `transformer/config.json` of the base model, see article 007).
- **Quantization:** `z_image_turbo-Q4_K.gguf`, Q4_K (4-bit with the K-quant scheme of llama.cpp). The repository also lists Q2_K, Q3_K, Q4_0, Q5_0, Q6_K and Q8_0; only Q4_K was tested.
- **Text encoder:** Qwen3-4B-Instruct-2507, quantized to Q4_K_M in GGUF (2.50 GB).
- **VAE:** `ae.safetensors`, 16 latent channels, the FLUX-style autoencoder (see article 007).
- **Sampler:** Euler, the runtime's default in this run; 8 steps, CFG 1.0 (the runtime's example; the base model card uses guidance 0.0 in diffusers).
- **Implementation:** stable-diffusion.cpp, C/C++, with a CPU backend (AVX, AVX2, AVX512 on x86, per its README).

## Size

- **Diffusion model:** `z_image_turbo-Q4_K.gguf`, 3,864,250,304 bytes (3.86 GB). The base model in BF16 is about 12.3 GB for the transformer; the Q4 file is roughly a third of that.
- **Text encoder:** `Qwen3-4B-Instruct-2507-Q4_K_M.gguf`, 2,497,281,120 bytes (2.50 GB).
- **VAE:** `ae.safetensors`, 335,304,388 bytes (0.34 GB).
- **Output:** 512 × 512 in the test.

## Minimum hardware

| Configuration | Memory | Source | Recommended |
|---------------|--------|--------|-------------|
| CPU, all three parts in RAM | **6,221.12 MB** | Measured: the runtime's memory report (text encoder 2,375.91 MB, diffusion model 3,685.21 MB, VAE 160.00 MB) | Any PC with 8 GB of RAM *(estimate for the rest of the system)* |
| BF16 base model (article 007) | ≈ 20 GB | Calculation (not run here) | GPU |

The process's total RAM use was not measured; the 6.2 GB is the weights in the runtime's report.

**Our machine (15.7 GB RAM, integrated graphics, no CUDA):** the run completed with `--offload-to-cpu`. The weights stayed in RAM; no GPU was used.

## Interfaces

- `sd-cli.exe`: the command used here, with `--diffusion-model`, `--vae`, `--llm` (the Qwen3 encoder), `-p`, `-W`, `-H`, `--steps`, `--cfg-scale`, `-s`, `--offload-to-cpu` and `-o`.
- `sd-server.exe`: the same release, not tested.
- Python: `test_zimage_gguf_sdcpp.py` (in `lab-img/`) calls `sd-cli.exe` and records its log.
- ComfyUI: not tested here. The base model's repackaged files are documented for ComfyUI (see article 007).

## Who uses it and for what

- The quantized repository has 265,885 downloads in the last month and 63 likes (as of 2026-11-12). Downloads measure reach, not quality.
- The card names no companies or projects that use the model.

## Why it matters

It is the first model in this series that generates an image with a 6-billion-parameter model on this laptop. Quantization makes the memory fit; the cost is time. One image of 8 steps took 480 s, and sampling alone took 439 s, which is about 55 s per step *(our measurement)*. A GPU would be much faster. Of the series' 6-billion-parameter tests, this is the only one that ran on the reference machine.

## Behind the model

- **Base model:** Tongyi-MAI (Alibaba Group), see article 007.
- **Quantization:** `leejet`, the author of stable-diffusion.cpp. The card links to the base model and states that the quantized files follow the base model's license, Apache 2.0.
- **Text encoder:** the unsloth repository; the Qwen3 model is by Alibaba's Qwen team.

## Curiosities

- The prompt asked for "a red circle on a white background". This run drew a red ring with a white centre on a white background, and no texture. The same prompt on SD 1.5 (article 008) gave a dark textured background.
- The base model's card says guidance 0.0; the runtime's example uses CFG 1.0. Both leave out the second pass per step, but the value is not the same, and we used the runtime's value.

---

## Families

| Family | Value | Reason |
|--------|-------|--------|
| Group (architecture) | Diffusion (diffusion transformer, DiT) | Same architecture as article 007. |
| Category | Paradox | Quantized variant (GGUF Q4_K) of a known model, following the rule in `CLAUDE.md`. |
| Tier (parameters) | UU (4–14 B) | 6.15 B parameters in the transformer; quantization does not change the tier. |
| Type (modality) | Image | Text input, image output. |
| Evolutionary line | Z-Image → Z-Image-Turbo → Z-Image-Turbo Q4 | Quantized version of article 007's model. |
| Ditto | Not assigned | Used as a finished model. |

---

## How to run it

**Status: tested on the machine (CPU, stable-diffusion.cpp, one image).** Script: `lab-img/test_zimage_gguf_sdcpp.py`. Log: `lab-img/out/zimage_gguf_prueba.log`. Image: `lab-img/out/zimage_gguf_prueba.png`.

### a. Prerequisites
- Windows 11 with a CPU that supports AVX2.
- About 7 GB of free disk space for the three model files.
- Python 3.12 (only the standard library is used by the script).

### b. Runtime
Download `sd-master-b9d7176-bin-win-cpu-x64.zip` from the release `master-1091-b9d7176` (SHA-256 `7e881e3c95d7ec9bf4b46e87fda37c156da9b38d18fa2439d18f29915750acbb`). Extract it to `lab-img/sdcpp/bin/`. The same build is used for article 008.

### c. Model files (into `lab-img/models/`)

| File | Source | Size | SHA-256 |
|------|--------|------|---------|
| `z_image_turbo-Q4_K.gguf` | `leejet/Z-Image-Turbo-GGUF` | 3.86 GB | `14b375ab4f226bc5378f68f37e899ef3c2242b8541e61e2bc1aff40976086fbd` |
| `Qwen3-4B-Instruct-2507-Q4_K_M.gguf` | `unsloth/Qwen3-4B-Instruct-2507-GGUF` | 2.50 GB | `3605803b982cb64aead44f6c1b2ae36e3acdb41d8e46c8a94c6533bc4c67e597` |
| `ae.safetensors` | `Comfy-Org/z_image_turbo` (`split_files/vae/`) | 0.34 GB | `afc8e28272cd15db3919bacdb6918ce9c1ed22e96cb12c4d5ed0fba823529e38` |

The hashes are the local file hashes; they were not compared with the publishers' published checksums, which were not read.

### d. Minimal example
`lab-img/test_zimage_gguf_sdcpp.py`, with the defaults: prompt `a red circle on a white background`, 512 × 512, 8 steps, CFG 1.0, seed 42, `--offload-to-cpu`. Run from `lab-img/`: `python test_zimage_gguf_sdcpp.py`.

### e. Check
The script reports the exit code, the total time and the paths. Exit code 0 means the image was saved.

### f. Warnings
- **Download:** about 6.4 GB for the three files.
- **Time:** about 8 minutes per image on this machine. Plan it as a batch job.
- **License:** Apache 2.0 for the model and the text encoder. The VAE comes from a repackaging repository; see Pending.

### Results on the machine (2026-11-12)

| Measure | Value | Source |
|---------|-------|--------|
| Exit code | 0 | Script output |
| Total time, one image | 480.4 s | Runtime log (`generate_image completed in 480.42s`) |
| Text encoder computation | 2.2 s | Runtime log (`get_learned_condition`) |
| Sampling (8 steps, Euler) | 439.3 s, about 55 s per step | Runtime log |
| VAE decode | 39.0 s | Runtime log |
| Weights in RAM | 6,221.12 MB | Runtime log (text encoder 2,375.91 MB, diffusion model 3,685.21 MB, VAE 160.00 MB) |
| Output | 512 × 512, a red ring on a white background | Viewed image |

## Verification notes

| Data | Value | Source | Verified? |
|------|-------|--------|-----------|
| Base model parameters | 6.15 B (transformer) | Article 007 | Yes |
| Architecture | 30 layers, hidden 3840, 30 heads | `transformer/config.json` (base model) | Yes |
| Quantization used | Q4_K, 3.86 GB | `leejet/Z-Image-Turbo-GGUF` file listing | Yes |
| Quantization license | Apache 2.0 | Repository tag and card | Yes |
| Text encoder | Qwen3-4B-Instruct-2507, Q4_K_M, 2.50 GB, Apache 2.0 | `unsloth` repository tag and file size | Yes |
| VAE | `ae.safetensors`, 0.34 GB | `Comfy-Org/z_image_turbo` file listing | Yes (file size); original not verified (see Pending) |
| Runtime | `master-1091-b9d7176`, MIT | GitHub release | Yes |
| Runtime SHA-256 | `7e881e3c…` | Downloaded zip and release digest | Yes |
| Weights in RAM | 6,221.12 MB | Runtime log on this machine | Yes (measured) |
| Timings | 480.4 s total, 439.3 s sampling, 39.0 s decode | Runtime log on this machine | Yes (measured) |
| BF16 base model timing | Not run | — | — |
| Downloads (quantized repo) | 265,885, last month | HF API, 2026-11-12 | Yes (snapshot) |

## Pending

- **VAE provenance:** the `ae.safetensors` file comes from `Comfy-Org/z_image_turbo`, a public repackaging. The original FLUX.1 VAE in `black-forest-labs/FLUX.1-schnell` requires accepting a license (HTTP 401 without a login), so it was not used. The Comfy-Org file has not been checked against the original; check its hash before stating it is identical.
- **Quality compared with BF16:** the base model was not run on this machine, so the image cannot be compared with article 007's BF16 result.
- **Process memory:** the 6.2 GB is the runtime's report. Measure the peak RAM of the process before giving a total.
- **Quantization types:** only Q4_K was tested. Q4_0 and Q8_0 are listed in the repository but not measured.
- **Guidance:** the runtime example uses CFG 1.0 and the card uses guidance 0.0 in diffusers. The difference was not tested.
