# 008 · Stable Diffusion 1.5

**Main source:** https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5 (mirror of the deprecated `runwayml/stable-diffusion-v1-5` repository)
**Runtime used:** stable-diffusion.cpp, release `master-1091-b9d7176`, https://github.com/leejet/stable-diffusion.cpp (MIT)
**License:** CreativeML OpenRAIL-M (model); MIT (runtime)
**Consulted:** 2026-11-12
**Code:** 05-NU-S-008 (catalogue 05 Image, video and 3D · NU · Starter)
**Origin:** chosen by the author for the first CPU test of the series' image models. It is not in the vault candidate queue; it is the reference model for a small, CPU-friendly text-to-image test.
**Families:** Starter · NU · Diffusion (U-Net, latent diffusion) · Stable Diffusion line (see the "Families" section)

---

## LinkedIn text

The model that made local image generation popular, run on a laptop with no graphics card: one image took 7 minutes.

Stable Diffusion 1.5 is a text-to-image model with about 0.9 billion parameters. It turns a written description into a picture by removing noise step by step in a compressed space. It is open-source, under the CreativeML OpenRAIL-M license, which has use restrictions.

🔧 **Type and technology:** latent diffusion: a U-Net denoiser, a CLIP text encoder and a VAE decoder. Run here with stable-diffusion.cpp, a C/C++ runtime.
📏 **Size:** about 0.9 B parameters; the file we used (`v1-5-pruned-emaonly.safetensors`) weighs 4.27 GB. Output 512 × 512 pixels.
💻 **Minimum hardware:** the runtime reported 2.78 GB of weights in RAM, and it ran on CPU with no GPU. Our test machine has 15.7 GB of RAM and no CUDA.
🛠️ **Interfaces:** the `sd-cli.exe` command line of stable-diffusion.cpp, the `sd-server` HTTP server in the same release, and Python (`diffusers`, not tested here).
👥 **Who uses it and for what:** the card names no users. It has 1,019,121 downloads last month and 1.36k likes (as of 2026-11-12), so it is one of the most used image models on the Hub.
💡 **Why it matters:** it is the cheapest way to see a real text-to-image model working on a normal laptop. Our run took 429 s for one image of 20 steps: slow, but it runs. Newer models give better images, but they need more memory *(our measurement on this machine)*.
🏢 **Behind the model:** the card's organization is the `stable-diffusion-v1-5` namespace, a mirror of the deprecated `runwayml` repository; the original authors and paper are not checked yet *(see Pending)*.
🤓 **Curiosity:** the image on this run came out as a red ring on a dark textured background. The prompt asked for a white background, so the model followed "red circle" and not the rest.

Model card: https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5

#ImageGeneration #AI #OpenSource

---

## What it is

Stable Diffusion 1.5 is a **text-to-image model**. It does not edit images. It takes a prompt and returns a picture, starting from random noise and removing it step by step. The denoising happens in a compressed "latent" space, which is what made the model practical on consumer hardware in its time.

## Type and technology

- **Task:** text-to-image generation.
- **Architecture:** latent diffusion: a text encoder (CLIP, see Pending for the exact model), a U-Net that predicts the noise at each step, and a VAE that decodes the final latent into pixels. The file we used is a single safetensors checkpoint with all the parts.
- **Sampler:** the runtime reports "Euler A" (the log line `sampling using Euler A method`), used by default.
- **Implementation:** the model is distributed for PyTorch/`diffusers`. Our test ran it through stable-diffusion.cpp, a C/C++ runtime with a CPU backend (AVX, AVX2 and AVX512 on x86, per its README).

## Size

- **Parameters:** 0.9B (card metadata, stored as F32).
- **Output resolution:** 512 × 512 in the test (the runtime default).
- **Weight file:** `v1-5-pruned-emaonly.safetensors`, 4.27 GB. The repository holds several other files (a second, larger checkpoint, pickle `.ckpt` files and `diffusers` subfolders); the repository total is about 47 GB.

## Minimum hardware

| Configuration | Memory | Source | Recommended |
|---------------|--------|--------|-------------|
| CPU, runtime weights in RAM | 2.78 GB | Measured: the runtime's own memory report in our log | Any PC with 8 GB of RAM *(estimate for the rest of the system)* |
| GPU, FP16 | ≈ 2 GB VRAM | Estimate from the size of the weights | Consumer GPU |

The 2.78 GB is the sum of the text encoder (469 MB), the diffusion model (2,155 MB) and the VAE (160 MB), as the runtime reports it. The process's total RAM use was not measured.

**Our machine (15.7 GB RAM, integrated graphics, no CUDA):** it runs. Timings from our run are in "How to run it".

## Interfaces

- `sd-cli.exe`: the command-line tool used here. Flags used: `-m` (model), `-p` (prompt), `-W` and `-H` (size), `--steps`, `--cfg-scale`, `-s` (seed), `-o` (output).
- `sd-server.exe`: a server in the same release, not tested.
- Desktop front ends: not tested here.
- Python: `test_sd15_sdcpp.py` (in `lab-img/`) calls `sd-cli.exe` and records its log. The `diffusers` route is not tested here.

## Who uses it and for what

- The card names no companies, products or research projects that use the model.
- Popularity (2026-11-12): 1,019,121 downloads in the last month and 1.36k likes on the Hugging Face page. Downloads measure reach, not quality.

## Why it matters

It is small enough to run on a laptop CPU, and it still shows the full text-to-image pipeline: prompt in, image out, with the sampler, seed and step count visible. In our run, a 512 × 512 image with 20 steps took 429 s on this machine. Newer models such as Z-Image-Turbo give better quality, but they need more memory *(our reading of the runs, see the series' articles 007 and 009)*.

## Behind the model

- **Organization:** the `stable-diffusion-v1-5` account on Hugging Face, which mirrors the original `runwayml` repository (now deprecated).
- **Authors:** to be checked in the model's paper (see Pending).
- **License:** CreativeML OpenRAIL-M. It allows use and redistribution with restrictions on some uses; read the full text before commercial use.

## Curiosities

- The first image on this machine had the right main object, a red circle, but the background was a dark brown texture and not the white background the prompt asked for. We keep that result as it came out.
- The VAE decode took 54 s, about one seventh of the sampling time (372.9 s), so decoding the final image is not negligible on CPU.

---

## Families

| Family | Value | Reason |
|--------|-------|--------|
| Group (architecture) | Diffusion (latent U-Net) | Denoises a latent over steps, then decodes it with a VAE. |
| Category | Starter | Small model that runs on a laptop CPU, which makes it a good first image model to test. |
| Tier (parameters) | NU (< 1 B) | About 0.9 B parameters. |
| Type (modality) | Image | Text input, image output. |
| Evolutionary line | Stable Diffusion 1.x → 1.5 | Version 1.5 of the first Stable Diffusion line. Later lines (SDXL, SD3) are separate models in this series. |
| Ditto | Not assigned | Used as a finished model in this article; it is also a common base for fine-tuning, which we did not test. |

---

## How to run it

**Status: tested on the machine (CPU, stable-diffusion.cpp, one image).** Script: `lab-img/test_sd15_sdcpp.py`. Log: `lab-img/out/sd15_prueba.log`. Image: `lab-img/out/sd15_prueba.png`.

### a. Prerequisites
- Windows 11 with a CPU that supports AVX2 (the release's `cpu` build selects the best instruction set at run time).
- About 5 GB free for the model file.
- Python 3.12 (only the standard library is used by the script).

### b. Runtime
Download the Windows CPU build `sd-master-b9d7176-bin-win-cpu-x64.zip` from the release `master-1091-b9d7176`. Its SHA-256 is `7e881e3c95d7ec9bf4b46e87fda37c156da9b38d18fa2439d18f29915750acbb`, which matches the digest published on the release page. Extract it to `lab-img/sdcpp/bin/`.

### c. Model
Download `v1-5-pruned-emaonly.safetensors` (4.27 GB) from the repository above into `lab-img/models/`.

### d. Minimal example
`lab-img/test_sd15_sdcpp.py`, with the defaults: prompt `a red circle on a white background`, 512 × 512, 20 steps, CFG 7.0, seed 42. Run from `lab-img/`: `python test_sd15_sdcpp.py`.

### e. Check
The script reports the exit code, the total time and the paths. Exit code 0 means the image was saved.

### f. Warnings
- **Download:** 4.27 GB for the model.
- **Time:** about 7 minutes per image on this machine. Plan it as a batch job, not an interactive one.
- **License:** CreativeML OpenRAIL-M, with use restrictions; see the license text.

### Results on the machine (2026-11-12)

| Measure | Value | Source |
|---------|-------|--------|
| Exit code | 0 | Script output |
| Total time, one image | 429.0 s | Script (includes model load) |
| Model load and tensors | ≈ 7.8 s | Runtime log (0.01 + 0.53 + 7.05 + 0.22 s across the load steps) |
| Sampling (20 steps, Euler A) | 372.9 s | Runtime log |
| VAE decode | 54.3 s | Runtime log |
| Weights in RAM | 2,784.45 MB | Runtime log (text encoder 469.44 MB, diffusion model 2,155.33 MB, VAE 159.68 MB) |
| Output | 512 × 512, a red ring around a white circle on a dark textured background | Viewed image |

The prompt asked for a red circle on a white background. The model drew the circle with a red ring and a white center, but the background is dark and textured. This is a partial match, recorded as it came out.

## Verification notes

| Data | Value | Source | Verified? |
|------|-------|--------|-----------|
| Parameters | 0.9B | HF card metadata (F32) | Yes |
| License | CreativeML OpenRAIL-M | HF card | Yes |
| Model file size | 4.27 GB (`v1-5-pruned-emaonly.safetensors`) | HF tree listing | Yes |
| Repository total | 47.3 GB | HF tree listing | Yes (snapshot) |
| Downloads last month / likes | 1,019,121 / 1.36k | HF page, 2026-11-12 | Yes (snapshot) |
| Runtime release | `master-1091-b9d7176`, MIT | GitHub release page and repository | Yes |
| Runtime SHA-256 | `7e881e3c…` | Downloaded zip and release digest | Yes |
| Weights in RAM | 2,784.45 MB | Runtime log on this machine | Yes (measured) |
| Timings | 429 s total; 372.9 s sampling; 54.3 s decode | Runtime log on this machine | Yes (measured) |
| Process RAM | Not measured | — | **No**, see Pending |
| GPU VRAM | ≈ 2 GB | Estimate from file size | **Estimate** |
| Authors and original paper | Not checked | — | **No**, see Pending |
| CLIP text encoder version | Not checked | — | **No**, see Pending |

## Pending

- **Authors and paper:** the model card's authors and the original paper have not been read. Check them before stating the organization history in the LinkedIn text.
- **Text encoder:** the exact CLIP model is not named here; check the repository's `text_encoder` folder before naming it.
- **Process memory:** the 2.78 GB is the weights in the runtime's report. Measure the peak RAM of the process (for example with Task Manager during the run) before giving a total.
- **Sampler default:** the log says Euler A; verify the default in `sd-cli -h` before writing it as a fixed setting.
- **Background of the mirror:** the `runwayml` repository is deprecated; the mirror's card gives the history. Confirm the exact dates before writing them.
- **Comparison with a GPU:** no GPU figure for SD 1.5 has been measured or verified. The GPU numbers found in the search were for SDXL at 1024 × 1024, a different model and resolution.
