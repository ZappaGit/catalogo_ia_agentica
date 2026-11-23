# IA 365 models

A series of LinkedIn posts explaining generative models: one about every day.

> Spanish copy of the full repository: [`es/`](es/README.md)

## Goal

Explain what each model is, with verified data, so that anyone can understand it and decide whether it is useful to them. Each post comes from a full article in this folder.

## What is covered for each model

1. **What it is**: type (text, image, video, audio, multimodal, embeddings) and main task.
2. **Technology**: architecture (transformer, diffusion, MoE…), implementation language and libraries.
3. **Size**: parameters, maximum context and weight format.
4. **Minimum hardware**: approximate RAM/VRAM needed to run it, with the calculation method stated.
5. **Interfaces**: how it is used (API, Python, UI, CLI, ComfyUI…).
6. **Who uses it and for what**: real cases or known projects.
7. **Why it matters**: what it offers compared with alternatives.
8. **Who is behind it**: organization and authors.
9. **Curiosities**.
10. **Pokémon**: association used for the visual hook (see the conventions below).

## Conventions

- **Verification**: every data point comes from the model card on Hugging Face or another official source, cited in the article. Anything that is an estimate is marked as such. Anything not verified is listed as pending.
- **License**: stated explicitly, because it determines commercial use.
- **Snapshot date**: download and popularity figures change; the consultation date is recorded.
- **Language**: English. The full article in `posts/` is the source of truth; `catalogue/` holds the LinkedIn summaries.
- **Pokémon**: each model is given a Pokémon whose type or trait fits what the model does (for example, a TTS model can be a "voice" Pokémon). The association is an educational resource; it does not imply any official relationship with The Pokémon Company or Nintendo. Pokémon is a registered trademark of its owners: no sprites or official artwork are used in the posts, only the name and the idea.
- **LinkedIn format**: a hook on the first line, 4–6 short blocks, one highlighted hardware figure and a link to the model card. No more than 3 hashtags.

## Identification code

Each model has a short code, `CC-TIER-FAM-NNN`, which is written in the header of the article, in the template and in `indice.md`:

- **CC** (catalogue, two digits): category of the vault catalogue, from `01` to `08` (01 Text and LLMs, 02 Embeddings and RAG, 03 Classic NLP, 04 Voice and audio, 05 Image, video and 3D, 06 Multimodal, 07 Time series, 08 Unlabeled).
- **TIER** (parameters): `UB` ≥ 100 B, `OU` 14–100 B, `UU` 4–14 B, `RU` 1–4 B, `NU` < 1 B.
- **FAM** (family): `S` Starter, `L` Legendary, `M` Mythical, `B` Ultra Beast, `P` Paradox.
- **NNN**: article number. The file name starts with NNN, followed by the code and the model slug.

Example: `01-UU-S-002` is Qwen3-8B (text, 8.2 B, Starter).

## Structure

- `README.md`: this document.
- `plantilla.md`: template for each article.
- `indice.md`: schedule and status of each model.
- `posts/`: one file per model, named `NNN-CC-TIER-FAM-model-slug.md`.
- `catalogue/`: English LinkedIn summaries, one per model, ready to publish.
- `carta/`: LaTeX model cards (one per model; `carta/pruebas/` holds test cards).
- `glosario.md`: glossary of technical terms.
- `es/`: complete Spanish copy of the repository, for reading.

## Origin of the models

The series starts from the vault catalogue (`IA_Agentica/HuggingFace`), which lists the most downloaded models on the Hub. Models for the series can be chosen from there or from other sources; each article states where it came from.

## Glossary

`glosario.md` explains the technical terms that appear in the articles (TTS, ISTFTNet, GQA, KV cache, quantization…), with links to the articles where they are used. It must be kept up to date when a new article is added.

## Language

- Full article (`posts/`): English, source of truth.
- Publishing version (`catalogue/`): English, summary of the full article.
- Spanish copy: [`es/`](es/).

## Work environment

Machine where the tests for the series are run (`lab-tts/` and the following labs):

| Component | Detail |
|-----------|--------|
| Machine | Windows 11 Home (10.0.26200) laptop |
| CPU | Intel Core i7-1355U (13th generation), 10 cores and 12 threads |
| RAM | 16 GB (15.7 GB usable), 3200 MHz |
| GPU | Integrated Intel UHD Graphics, no CUDA. Shares memory with system RAM |
| Disk | C: 952.5 GB, 528.8 GB free (figure as of the consultation date) |
| Python | 3.12.10 (installed on the system) |
| Git | 2.46.0 |

Consequences for the articles:

- All series models tested here run on CPU. Models with more than a few billion parameters do not fit in the available RAM in BF16.
- Minimum hardware cited in an article must be marked as an **estimate** if it has not been measured on this machine.
- For large models (for example, Qwen3-8B), testing will be done with a smaller or quantized version, or on another machine with an NVIDIA GPU.

## License

The content of this repository (articles, summaries, glossary, notes and cards) is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You may reuse and adapt it, including commercially, as long as you give credit. See [LICENSE](LICENSE).

This license does not cover the models described in the series: each model has its own license, stated in its article.
