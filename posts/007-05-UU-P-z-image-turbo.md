# 007 · Z-Image-Turbo

**Main source:** https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
**Paper:** https://arxiv.org/abs/2511.22699 (Z-Image Team, v1 27 Nov 2025)
**License:** Apache 2.0
**Consulted:** 2026-11-10
**Code:** 05-UU-P-007 (catalogue 05 Image, video and 3D · UU · Paradox)
**Origin:** candidate queue of `indice.md`, taken from the vault catalogue `IA_Agentica/HuggingFace` (entry "Z-Image-Turbo / Qwen-Image 2.1 (image)"). Chosen as the first candidate of the queue; it is the first image model of the series.
**Families:** Paradox · UU · Diffusion transformer (DiT) · distilled variant of Z-Image (see the "Families" section)

---

## LinkedIn text

A 6-billion-parameter image model that draws in 8 steps, where its base version needs 50.

Z-Image-Turbo is a text-to-image model from Alibaba's Tongyi-MAI team. It is a distilled version of Z-Image: the same model, trained to reach the result in far fewer steps. It is open-source, under the Apache 2.0 license.

🔧 **Type and technology:** text-to-image diffusion transformer, single-stream design called S3-DiT, with a Qwen3-4B text encoder and a Flux VAE (paper summary, see Pending). Distilled to 8 steps. Python, on Hugging Face Diffusers.
📏 **Size:** 6.15 B parameters, bilingual prompts (English and Chinese), 1024 × 1024 in the card's example. Distributed as safetensors.
💻 **Minimum hardware:** about **16 GB of VRAM** on a consumer GPU, as the card states (BF16). The transformer alone is about 12.3 GB in BF16 *(estimate: 6.15 B × 2 bytes; the 16 GB figure is the card's)*. A quantized Q4 version runs on CPU on the reference laptop, with about 6.2 GB of weights in RAM; see article 009.
🛠️ **Interfaces:** Python with `ZImagePipeline` from `diffusers`, installed from the latest release. Apps such as Draw Things and DiffusionBee, and hosted inference through fal. ComfyUI is not mentioned in the card.
👥 **Who uses it and for what:** the card names no companies or projects. It has 723,026 downloads and 5,583 likes (as of 2026-11-10), and both the Hugging Face and ModelScope demos let anyone try it.
💡 **Why it matters:** 8 steps instead of 50 means an image in a few seconds on one consumer GPU, which makes local image generation practical for individuals. The card claims 16 GB of VRAM is enough; we have not measured that *(our reading of the card)*.
🏢 **Behind the model:** the Tongyi-MAI organization, part of Alibaba Group. The paper is by the "Z-Image Team" with 23 named co-authors.
🤓 **Curiosity:** the model was distilled from a 50-step base model with guidance, and the Turbo version runs with guidance scale 0. The card's "8 NFEs" (network evaluations) corresponds to 9 steps in the code, which perform 8 forward passes of the transformer.

Model card: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo

#ImageGeneration #AI #OpenSource

---

## What it is

Z-Image-Turbo is a **text-to-image model**. It takes a written description and returns an image. It does not edit existing images in this release. Its card describes it as "an efficient image generation foundation model with Single-Stream Diffusion Transformer", and it is the distilled, fast version of the Z-Image model.

Image generation with diffusion works by starting from random noise and removing it step by step, guided by the text. A model that needs fewer steps is faster, but the quality has to be kept, which is what distillation is for (see the glossary).

## Type and technology

- **Task:** text-to-image generation (`pipeline_tag` in the API: text-to-image).
- **Architecture:** a diffusion transformer (DiT). The card calls it "Scalable Single-Stream Diffusion Transformer (S3-DiT)": text tokens and image tokens go through the same transformer stream. `transformer/config.json` gives 30 layers, hidden size 3840 and 30 attention heads. The paper summary said 32 heads; the config contradicts it, so the config is used. The FFN size (10240, from the paper summary) is not in the config and stays pending.
- **Text encoder:** `text_encoder/config.json` describes a Qwen3 model with 36 layers and hidden size 2560. Its three safetensors files add up to about 8 GB in BF16, which matches a model of about 4 B parameters. The card does not name it; the name Qwen3-4B comes from the paper summary.
- **VAE:** `vae/config.json` is an `AutoencoderKL` with 16 latent channels, four down-sampling blocks (8x spatial compression) and `_name_or_path: flux-dev`, so it is a Flux-style VAE.
- **Distillation:** the card says Turbo is "a distilled version of Z-Image" that needs "only 8 NFEs". The model zoo in the card gives 50 steps with CFG for the base Z-Image and 8 steps without CFG for Turbo. The methods (Decoupled-DMD and DMDR) are cited in the paper summary, not confirmed in the card *(pending)*.
- **Implementation language:** Python, with the Hugging Face `diffusers` library (class `ZImagePipeline`).

## Size

- **Parameters:** 6 B according to the card; 6,154,908,736 according to the API (safetensors metadata, F32 tensors). The paper's table also gives 6.15 B.
- **Context:** not applicable; the input is a text prompt.
- **Resolution:** the card's example uses 1024 × 1024. The supported range was not found.
- **Format:** safetensors only. No GGUF file is in the repository (106 third-party quantizations are linked from the page, not reviewed here).
- **Repository storage:** 53,980,522,390 bytes according to the API (about 54 GB). Per-file sizes are not given by the API.

## Minimum hardware

| Configuration | Memory | Calculation | Recommended |
|---------------|--------|-------------|-------------|
| BF16 weights, transformer only | ≈ 12.3 GB | 6.15 B × 2 bytes | — |
| BF16 weights, transformer + text encoder | ≈ 20.4 GB | 6.15 B × 2 + ≈ 4 B × 2 bytes | — |
| As stated by the card | 16 GB VRAM | Card: "fits comfortably within 16G VRAM consumer devices" | Consumer NVIDIA GPU |
| FP32 weights (safetensors as stored) | ≈ 24.6 GB | 6.15 B × 4 bytes | Does not fit in 16 GB |

The 16 GB figure is the card's claim. Our own estimate of 12.3 GB covers the weights only; the text encoder, the VAE and the activations add memory, which is why the card's figure is higher. None of these values has been measured on the reference machine.

The paper also reports sub-second generation on H800 GPUs. Its footnote says FlashAttention-3 and `torch.compile` are needed for that speed. This is a data-centre result, not a laptop figure.

**Reference machine:** 15.7 GB of RAM, integrated Intel graphics, no CUDA. The BF16 model does not fit there. The Q4 GGUF version runs on it (article 009).

## Interfaces

- **Python with Diffusers:** `from diffusers import ZImagePipeline`. The card says to install `diffusers` from source; the card also says two pull requests (#12703 and #12715) are merged into the latest official release. The minimum version number was not found.
- **Guidance:** the card says `guidance_scale=0.0` for the Turbo models, and the example runs `num_inference_steps=9`.
- **Desktop apps:** Draw Things and DiffusionBee are listed on the card or its tags.
- **Hosted inference:** a fal inference provider, and public demos on Hugging Face and ModelScope.
- **ComfyUI:** not found in the card.

## Who uses it and for what

- The card names no companies, products or research projects that use the model.
- Popularity (as of 2026-11-10): 723,026 downloads and 5,583 likes on Hugging Face (API). Downloads are cumulative, so they measure reach, not quality.
- The card lists the demos on Hugging Face and ModelScope and the Alibaba AI Arena as places to try the model.

## Why it matters

It is one of the few text-to-image models of this size that is released under a permissive license and is designed to run in a few steps on a single consumer GPU. Compared with a 50-step base model, the time per image falls roughly six-fold *(our reading from the step counts on the card, not a benchmark)*. Image quality against larger models was not checked here.

## Behind the model

- **Organization:** Tongyi-MAI, part of Alibaba Group.
- **Authors:** the paper is credited to the "Z-Image Team" with 23 named co-authors. The model card does not name the authors individually.
- **Dates:** the repository was created on 2025-11-25 and last modified on 2026-01-30 (API). The paper's first version (arXiv v1) is dated 27 November 2025.
- **Related models:** the card's model zoo lists Z-Image-Omni-Base and Z-Image-Edit as "to be released". They are not available at the consultation date.

## Curiosities

- The Turbo model runs without classifier-free guidance: the guidance scale is 0. The base model needs guidance, so the distilled model removes that second pass and saves more time.
- The card's count of "8 NFEs" is not the same as the number of steps in the code (9, which the card says "actually results in 8 DiT forwards"). The card does not explain the difference in detail; we report both figures as stated.

---

## Families

| Family | Value | Reason |
|--------|-------|--------|
| Group (architecture) | Diffusion (diffusion transformer, DiT) | Generates the image by removing noise in steps, with a transformer as the denoiser. |
| Category | Paradox | Distilled variant of a known model (Z-Image). The test card in `carta/pruebas/` had "Starter"; that is changed here, following the rule in `CLAUDE.md`. |
| Tier (parameters) | UU (4–14 B) | 6.15 B parameters. |
| Type (modality) | Image | Text input, image output. |
| Evolutionary line | Z-Image → Z-Image-Turbo | Turbo is the distilled version of the base Z-Image. Z-Image-Omni-Base and Z-Image-Edit are announced as siblings, not released. |
| Ditto | Not assigned | The card presents it as a finished model for generation. |

---

## How to run it

**Status: not run.** The lab is in `lab-img/` (not versioned, like `lab-llm/` and `lab-tts/`). The script is written and compiles, but the model has not been loaded: the reference machine has no CUDA and cannot hold the weights in RAM (see "Lab record" below).

### a. Prerequisites
- NVIDIA GPU with about 16 GB of VRAM or more (the card's claim; not verified on hardware).
- Windows 11 with Python 3.12 (the reference machine has Python 3.12.10).
- About 54 GB of free disk space for the Hugging Face cache.

### b. Virtual environment
In `lab-img/`: `python -m venv .venv`, then upgrade pip, as described in `lab-img/README.md`.

### c. Installation
- PyTorch with CUDA. The CPU build is not useful for this test.
- `diffusers` from the GitHub source (the card's instruction), with `transformers` and `accelerate`. The minimum version is not confirmed (see Pending).

### d. Minimal example
`lab-img/test_z_image_turbo.py`, with these defaults: prompt `a red circle on a white background`, 512 × 512, 9 steps, guidance 0.0, seed 42, BF16. It writes `lab-img/out/z_image_turbo_prueba.png`. If CUDA is not available, it prints a message and exits before loading anything. Run it from `lab-img/` with the lab's virtual environment: `.\.venv\Scripts\python.exe test_z_image_turbo.py`.

### e. Check
Expected result: a 512 × 512 PNG with a red circle on a white background. Not yet checked.

### f. Warnings
- **Download:** about 54 GB into the Hugging Face cache (`%USERPROFILE%\.cache\huggingface`).
- **Hardware on the reference machine:** it does not fit. BF16 weights: DiT ≈ 12.3 GB (6.15 B × 2 bytes) and Qwen3-4B text encoder ≈ 8 GB (from `text_encoder/config.json` and the file sizes), so more than 20 GB against 15.7 GB of RAM. Forcing CPU execution (`FORZAR_CPU = True`) would page the weights from disk: extremely slow, and it can freeze the system. Not recommended.
- **Safety:** the weights are in safetensors, which does not run code when loaded. The script does not use `trust_remote_code`. The code that does run is the `diffusers` library, installed from GitHub.
- **License:** Apache 2.0, no access restriction.
- **Diffusers arguments:** `torch_dtype` and `guidance_scale` follow the card's example; they have not been checked against the installed version.

### Lab record

| Date | Machine | Result |
|------|---------|--------|
| 2026-11-12 | Reference machine (no CUDA, 15.7 GB RAM) | Not run: the weights do not fit in memory. The script stops before loading. |

## Card illustration

The card for this model uses the simplest drawing of the image subtype: one sun over a horizon line, instead of the category 05 landscape with mountains. It is a choice for the series' card, not a property of the model.

## Verification notes

| Data | Value | Source | Verified? |
|------|-------|--------|-----------|
| Parameters | 6 B (card); 6,154,908,736 (API) | Model card; HF API `safetensors` | Yes |
| License | Apache 2.0 | Model card metadata and API tags | Yes |
| Official name and organization | Z-Image-Turbo, Tongyi-MAI (Alibaba Group) | Model card; paper | Yes |
| Architecture (S3-DiT) | Single-stream diffusion transformer | Model card | Yes |
| Layers, hidden size, heads | 30, 3840, 30 | `transformer/config.json` | Yes |
| FFN size | 10240 | Paper summary only | **No**, see Pending |
| Text encoder (Qwen3, 36 layers, hidden 2560, ≈ 4 B) | 3 safetensors files, ≈ 8 GB BF16 | `text_encoder/config.json`, repository tree | Yes (name Qwen3-4B: paper summary) |
| VAE (AutoencoderKL, 16 latent channels, flux-dev) | Config | `vae/config.json` | Yes |
| Distilled from Z-Image, 8 NFEs | Stated | Model card | Yes |
| 9 steps in the code | Stated | Model card example | Yes |
| Base model: 50 steps with CFG | Stated | Model card model zoo | Yes |
| Guidance scale 0 | Stated | Model card | Yes |
| Interfaces: Diffusers `ZImagePipeline` | Stated | Model card | Yes |
| Minimum Diffusers version | Not found | — | **No**, see Pending |
| Languages: English and Chinese | Stated | Model card | Yes |
| Hardware: 16 GB VRAM | Stated | Model card ("fits comfortably within 16G VRAM") | Yes (as the card's claim) |
| Hardware: BF16 weights ≈ 12.3 GB | Calculation: 6.15 B × 2 bytes | Own calculation | **Estimate** |
| Sub-second on H800 | Stated | Paper | Yes (data-centre figure) |
| Repository storage | 53,980,522,390 bytes | HF API `usedStorage` | Yes (snapshot) |
| Downloads / likes | 723,026 / 5,583 | HF API, 2026-11-10 | Yes (snapshot) |
| Creation / last modified | 2025-11-25 / 2026-01-30 | HF API | Yes |
| Paper v1 date | 27 Nov 2025 | arXiv | Yes |
| Gated access | No | HF API `gated: false` | Yes |
| Paradox category | Series criterion (`CLAUDE.md`) | Own classification | Proposal |
| UU tier | 4–14 B according to `CLAUDE.md` | Own classification | Yes |

## Pending

- **FFN size and distillation names:** the FFN size (10240) and the names Decoupled-DMD and DMDR come from the paper summary, not from the repository. Verify them in the paper (section 4.1 and the distillation sections) before stating them as fact.
- **Distillation methods:** the names Decoupled-DMD and DMDR are in the paper summary. Verify them in the paper before stating them as fact.
- **Minimum Diffusers version:** the card gives PR numbers, not a version. The repository was saved with `diffusers` 0.36.0.dev0 (`model_index.json`), so the release needed is at or after that; check the release notes.
- **ComfyUI support:** not in the Tongyi card. Comfy-Org's repackaged files (`Comfy-Org/z_image_turbo`, Apache 2.0) describe themselves as "Repackaged model files for ComfyUI", so ComfyUI use is documented there.
- **Supported resolutions:** the card gives 1024 × 1024 as an example only.
- **Text encoder and VAE in the 6 B count:** resolved. The transformer's three safetensors files total 24.6 GB, which is 6.15 B parameters at 4 bytes each, so the 6.15 B figure covers the transformer only. The text encoder (about 4 B) and the VAE are separate.
- **Measured hardware:** the BF16 model has not been run on the reference machine (no CUDA). The Q4 GGUF version has been run there; its timings are in article 009. The BF16 figures are the card's claim and our estimate.
- **Users and projects:** the card names none. Any claim about specific users needs an outside source.
- **Release date:** the card does not state one. Only the repository and paper dates above are known.
