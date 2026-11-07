# 001 · Kokoro-82M

**Main source:** https://huggingface.co/hexgrad/Kokoro-82M
**License:** Apache 2.0
**Consulted:** 2026-11-06
**Code:** 04-NU-S-001 (catalogue 04 Voice and audio · NU · Starter)
**Associated Pokémon:** Jigglypuff — the Pokémon that sings people to sleep; a model that "speaks" with 82 million parameters fits that idea of light, recognizable voice.

---

## LinkedIn text

A model that speaks with 82 million parameters. It fits on your laptop.

Kokoro is an open-source text-to-speech (TTS) model, with weights published under the Apache 2.0 license, which also allows it to be used in commercial projects.

🔧 **Type and technology:** TTS based on StyleTTS 2 with an ISTFTNet decoder. Decoder only: it does not use diffusion. Used from Python, with the `kokoro` package and the `misaki` grapheme-to-phoneme converter.
📏 **Size:** 82 million parameters. Version 1.0, released on 27 January 2025, trained on a few hundred hours of audio.
💻 **Minimum hardware:** CPU and RAM of a regular laptop. The weights take up about 330 MB in fp32 *(estimate: 82 M × 4 bytes; not stated on the model card)*.
🛠️ **Interfaces:** Python API (`KPipeline`), with audio output at 24 kHz. There is a demo on Hugging Face Spaces and a Google Colab notebook.
👥 **Who uses it and for what:** voice assistants, text reading and prototypes. The model card says it has already been deployed in many projects and commercial APIs.
💡 **Why it matters:** according to the model card itself, its API price was under $1 per million characters in April 2025. It shows that a small model can sound very good if it is trained on good data.
🏢 **Behind the model:** the architecture comes from StyleTTS 2 (Li et al., with code on GitHub). The model was trained independently by the developer known as rzvzn, at a cost of about $1,000 in A100 GPUs.
🤓 **Curiosity:** "kokoro" means "heart" or "spirit" in Japanese, and it is also the name of an AI in the Terminator saga.

Model card and demo: https://huggingface.co/hexgrad/Kokoro-82M

#AI #TTS #GenerativeAI

---

## Verification notes

| Data | Value | Source | Verified? |
|------|-------|--------|-----------|
| Parameters | 82 M | HF model card | Yes |
| License | Apache 2.0 | Model card metadata | Yes |
| Architecture | StyleTTS 2 + ISTFTNet, decoder only | HF model card ("Model Facts") | Yes |
| Language / libraries | Python, `kokoro` ≥0.9.2, `misaki`, `espeak-ng` | HF model card (usage) | Yes |
| Version and date | v1.0, 27 Jan 2025 | "Releases" table | Yes |
| Training data | A few hundred hours, permissive and synthetic audio from closed providers | HF model card | Yes |
| Training cost | ~$1,000 (1,000 h on A100 80 GB) | HF model card | Yes (declared by the author) |
| API price | < $1 per million characters (April 2025) | HF model card, cites third parties | Yes, but the figure is from 2025 |
| Languages and voices | v1.0: 8 languages and 54 voices | "Releases" table (link to VOICES.md) | Yes |
| Minimum hardware | ~330 MB of weights in fp32 | Own calculation | **Estimate** |
| Meaning of the name | "heart/spirit" in Japanese | HF model card | Yes |
| Local test (English) | Load, synthesis and RTF 1.08 on CPU; exit code 0 | `lab-tts/test_kokoro.py`, run on the machine | Yes (one run) |
| Local test (Spanish) | Synthesis with `ef_dora`, espeak-ng 1.52.0; RTF 0.66 | `lab-tts/test_kokoro_es.py`, run on the machine | Yes (one run) |
| Languages (VOICES.md) | The releases table says 8; VOICES.md lists 9 language blocks | HF model card, VOICES.md | Discrepancy, pending |

## Local lab (lab-tts)

Tested on the work machine: Windows 11, Python 3.12.10, Intel UHD GPU (no CUDA, everything on CPU) and 15.7 GB of RAM. Code, README and steps in [lab-tts/README.md](../lab-tts/README.md).

Commands used (PowerShell, from `lab-tts`):

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install "kokoro>=0.9.4" soundfile
.\.venv\Scripts\python.exe test_kokoro.py
```

Result of the first run in English:

| Measure | Value |
|---------|-------|
| Versions | kokoro 0.9.4, torch 2.15.0+cpu |
| Model load (includes weight download) | 58.6 s |
| Audio generated | 8.40 s in one segment |
| Synthesis time | 9.0 s |
| RTF | 1.08 |

Spanish test (`test_kokoro_es.py`, with espeak-ng 1.52.0 installed):

| Measure | Value |
|---------|-------|
| Audio generated | 6.90 s with the voice `ef_dora` |
| Synthesis time | 4.6 s |
| RTF | 0.66 (model already cached) |

The first run downloads the weights (~330 MB) and `en_core_web_sm` (~13 MB) for misaki. PyTorch deprecation warnings and Windows symlink warnings appear; they do not prevent execution.

## Settings: language, voice and speed

- **Language:** set when the pipeline is created, `KPipeline(lang_code=...)`. Codes in the repo: `a` American English, `b` British English, `e` Spanish, `f` French, `i` Italian, `p` Brazilian Portuguese, `h` Hindi. `j` (Japanese) needs `misaki[ja]` and `z` (Chinese) needs `misaki[zh]`. Spanish requires espeak-ng; it is already installed on the machine (1.52.0).
- **Voice:** chosen when calling the pipeline, `pipeline(text, voice="...")`. The voice prefix must match the language. Spanish voices according to VOICES.md: `ef_dora` (female), `em_alex` and `em_santa` (male).
- **Speed:** the `speed` parameter (float or function) speeds up or slows down the audio. I have tested it on the samples in the play section. VOICES.md recommends using it for very long texts to prevent the model from speeding up.
- **Mixed sentences:** the test used one Spanish sentence and one English sentence with `lang_code="a"`. The Spanish part is pronounced with an English accent, so one language per run is advisable.

## Available voices

v1.0 includes 54 voices in 9 languages, according to VOICES.md. The prefix indicates the language (`a`, `b`, `e`, `f`, `h`, `i`, `j`, `p`, `z`) and the second letter the sex (`f` female, `m` male). Each voice has an overall grade from A to F, which reflects its quality and the amount of training data; the model card warns that the grade is subjective.

| Language | Voices (F / M) | Names |
|----------|----------------|-------|
| American English (`a`) | 11 / 9 | af_heart (A), af_bella (A-), af_nicole, af_aoede, af_kore, af_sarah, af_alloy, af_nova, af_jessica, af_river, af_sky · am_fenrir, am_michael, am_puck, am_adam, am_echo, am_eric, am_liam, am_onyx, am_santa |
| British English (`b`) | 4 / 4 | bf_emma (B-), bf_isabella, bf_alice, bf_lily · bm_george, bm_fable, bm_lewis, bm_daniel |
| Japanese (`j`) | 4 / 1 | jf_alpha, jf_gongitsune, jf_nezumi, jf_tebukuro · jm_kumo |
| Mandarin Chinese (`z`) | 4 / 4 | zf_xiaobei, zf_xiaoni, zf_xiaoxiao, zf_xiaoyi · zm_yunjian, zm_yunxi, zm_yunxia, zm_yunyang |
| Spanish (`e`) | 1 / 2 | ef_dora · em_alex, em_santa |
| French (`f`) | 1 / 0 | ff_siwis |
| Hindi (`h`) | 2 / 2 | hf_alpha, hf_beta · hm_omega, hm_psi |
| Italian (`i`) | 1 / 1 | if_sara · im_nicola |
| Brazilian Portuguese (`p`) | 1 / 2 | pf_dora · pm_alex, pm_santa |

There are very few Spanish voices (three) and the model card gives them no grade. French has only one voice.

## Play: voices, mixes and speeds

The script [lab-tts/jugar_kokoro.py](../lab-tts/jugar_kokoro.py) generates 12 samples in `out/juego/`:

- **English voices:** `af_heart`, `af_bella`, `am_adam`, `bm_george`, with the same sentence.
- **Voice mix:** `voice="af_heart,am_michael"`. The repo averages the embeddings of the two voices, so an intermediate voice is obtained.
- **Speed:** `speed=0.75` (slow), `speed=1.25` (fast) and `speed=1.0` for `af_heart`.
- **Spanish:** `ef_dora`, `em_alex`, `em_santa`, the mix `ef_dora,em_alex` and `ef_dora` at `speed=0.8`.

| Sample | Voice | Speed | Audio | Synthesis | RTF |
|--------|-------|-------|-------|-----------|-----|
| en_af_heart | af_heart | 1.0 | 4.97 s | 3.4 s | 0.69 |
| en_af_bella | af_bella | 1.0 | 5.47 s | 7.3 s | 1.33 |
| en_am_adam | am_adam | 1.0 | 5.22 s | 4.0 s | 0.77 |
| en_bm_george | bm_george | 1.0 | 5.85 s | 5.0 s | 0.86 |
| en_mezcla_heart_michael | af_heart + am_michael | 1.0 | 5.30 s | 3.8 s | 0.71 |
| en_af_heart_lento | af_heart | 0.75 | 6.70 s | 3.5 s | 0.52 |
| en_af_heart_rapido | af_heart | 1.25 | 4.17 s | 2.5 s | 0.60 |
| es_ef_dora | ef_dora | 1.0 | 4.55 s | 2.6 s | 0.58 |
| es_em_alex | em_alex | 1.0 | 4.58 s | 3.7 s | 0.81 |
| es_em_santa | em_santa | 1.0 | 4.62 s | 9.0 s | 1.94 |
| es_mezcla_dora_alex | ef_dora + em_alex | 1.0 | 4.53 s | 2.4 s | 0.54 |
| es_ef_dora_lento | ef_dora | 0.8 | 5.78 s | 3.2 s | 0.56 |

What can be observed in these tests, without judging the sound yet:

- Speed changes the duration of the audio almost proportionally: 0.75 stretches the 4.97 s sample to 6.70 s, and 1.25 shortens it to 4.17 s.
- The mixes work and produce audio without errors. Whether it sounds natural has to be judged by listening.
- The RTF is higher the first time each voice is used (`af_bella` and `em_santa`). The measurements have to be repeated to get a stable value.

These samples come from a single run. Listening to them and judging them is the missing step.

## Limit: it does not clone your voice

Kokoro does not allow voice cloning. Its voices are fixed presets (the model card mentions 54 voices in v1.0). To sound like a specific voice, another cloning model would be needed, with its own license and requirements. I have not checked this yet.

## Service (planned, not built)

Kokoro does not include a server. The planned option is to wrap it with FastAPI and uvicorn inside the same venv:

- A `POST /tts` endpoint that receives the text and returns a WAV.
- The pipeline is loaded once at startup, so later requests do not repeat the loading.
- Listen only on `127.0.0.1`, so it cannot be reached from other machines.

With an RTF of 1.08 on this machine, each request would take roughly as long as the audio lasts. It is suitable for personal use and testing, not for many users at once.

## Pending

- **Hardware:** RTF measured (1.08 on the first run). Peak RAM still to be measured, and the test repeated to get a stable value.
- **Languages:** the releases table says 8 and VOICES.md lists 9 language blocks. Check before publishing.
- **Spanish:** synthesis tested with `ef_dora`. Voice quality still to be judged by listening; I have not been able to do that.
- **Listening:** judge the quality of the 12 samples in `out/juego/`. I cannot listen to them.
- **FastAPI service:** not built.
- **API price:** figure from April 2025; check before publishing.
