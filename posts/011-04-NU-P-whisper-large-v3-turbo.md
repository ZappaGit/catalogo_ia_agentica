# 011 · Whisper large-v3-turbo

**Main source:** https://huggingface.co/openai/whisper-large-v3-turbo (model card, `config.json`, Hugging Face API)
**Paper:** Radford et al., *Robust Speech Recognition via Large-Scale Weak Supervision* (2022), https://huggingface.co/papers/2212.04356
**License:** MIT (model card metadata)
**Consulted:** 2026-11-14
**Code:** 04-NU-P-011 (catalogue 04 Voice and audio · tier NU · Paradox; see the "Families" section)
**Associated Pokémon:** —
**Origin:** vault catalogue `IA_Agentica/HuggingFace`, category "04 Voz y audio". Chosen as the most popular audio-to-text model that runs on a 16 GB PC: the Whisper family leads speech recognition on the Hub; `whisper-large-v3` has more likes, but turbo is the one that runs at about real time on the reference machine (see "Choice").

---

## Summary

Drop in a voice note and get the text back, on a laptop with no graphics card.

Whisper large-v3-turbo is OpenAI's open speech recognition model. It transcribes audio in many languages, can translate it into English, and gives timestamps for each sentence.

🔧 **Type and technology:** speech recognition (audio to text). Transformer encoder-decoder, used with the Hugging Face `transformers` library.
📏 **Size:** 809 million parameters. A 1.6 GB weight file in FP16.
💻 **Minimum hardware:** in our test it used 3.9 GB of RAM on a CPU-only laptop (16 GB of RAM, no CUDA). A long audio took about as long to transcribe as to listen to.
🛠️ **Interfaces:** Python with `transformers` (a `pipeline` call with the audio path), for audio files of any length.
💡 **Why it matters:** it is large-v3 with the decoder cut from 32 layers to 4. The model card says it is "way faster, at the expense of a minor quality degradation".
🏢 **Behind the model:** OpenAI (Alec Radford and others), MIT license.
🤓 **Curiosity:** OpenAI's own card warns that it can "hallucinate": write text that was never said in the audio.

Model card: https://huggingface.co/openai/whisper-large-v3-turbo

---

## Choice

The user asked for the most popular audio-to-text model that can run on a personal 16 GB computer. Hugging Face API, 2026-11-14, task `automatic-speech-recognition`:

| Model | Downloads (last 30 days) | Likes | Note |
|-------|--------------------------|-------|------|
| argmaxinc/whisperkit-coreml | 67,619,890 | 266 | Whisper converted to CoreML for Apple Silicon; does not run on the reference Windows machine |
| openai/whisper-large-v3-turbo | 4,821,167 | 3,530 | This article |
| openai/whisper-large-v3 | 3,414,552 | 6,809 | Most liked; 1,550 M parameters |

Both large models fit in 16 GB. Turbo was chosen because it has fewer decoder layers and is the faster one on a CPU. large-v3 was not tested on the machine.

## What it is

Whisper is a family of speech recognition (ASR) and speech translation models from OpenAI. Per the model card, it was "trained on >5M hours of labeled data" and generalises "to many datasets and domains in a zero-shot setting".

**large-v3-turbo** is "a finetuned version of a pruned Whisper large-v3. In other words, it's the exact same model, except that the number of decoding layers have reduced from 32 to 4" (model card). The encoder, which listens to the audio, keeps its 32 layers; the decoder, which writes the text token by token, is much smaller.

## Type and technology

- **Architecture:** Transformer encoder-decoder (*sequence-to-sequence*) (model card, "Model details").
- **Input:** audio resampled to 16 kHz mono, turned into a log-Mel spectrogram with 128 bands (`num_mel_bins: 128` in `config.json`).
- **Window:** "Whisper has a receptive field of 30-seconds" (model card). Longer audio is processed with a long-form algorithm (see "Settings").
- **Layers (`config.json`):** 32 encoder layers, 4 decoder layers, hidden size 1280, vocabulary of 51,866 tokens, up to 448 output tokens per window.
- **Tasks:** transcription (same language as the audio) and translation into English (`task="translate"`).
- **Languages:** the card metadata lists 99 language codes. The card says it shows "strong ASR results in ~10 languages".

## Size

- **Parameters:** 808,878,080 (Hugging Face API, `safetensors`, FP16).
- **Weights:** `model.safetensors`, 1,617,824,864 bytes (about 1.6 GB).
- **In memory on CPU:** loaded in float32, as the model card does when there is no CUDA, the weights take about 3.2 GB *(estimate: 808.9 M × 4 bytes)*. The measured peak of the process was 3.84–3.90 GB (see "Minimum hardware").

## Minimum hardware

| Configuration | Memory | Calculation | Recommended |
|---------------|--------|-------------|-------------|
| CPU, float32, sequential mode | 3.84–3.90 GB peak of the process | Measured (`psutil`), 2026-11-14 | Reference laptop: 15.7 GB RAM, 12 CPU threads, Intel UHD without CUDA |
| CPU, float32, chunked mode (batch 4) | 5.00 GB peak | Measured | Same machine |
| GPU, float16 | about 1.6 GB for the weights *(estimate: 808.9 M × 2 bytes)* | Not tested | A GPU with CUDA |

Speed on the reference machine (sequential mode):

- Each 30-second window took about 25–30 s. An 8.7 s clip took 29.7 s (RTF 3.4), because a short clip still fills a whole window.
- A 75.4 s audio took 82.4 s with the language set and 89.6 s with automatic detection (RTF 1.09–1.19): about real time.

## Interfaces

- **Python with `transformers`:** the model card uses `pipeline("automatic-speech-recognition", ...)` and passes the path to an audio file: `pipe("audio.mp3")`. Several files can be passed as a list with `batch_size`.
- **Lower-level API:** `AutoModelForSpeechSeq2Seq` and `AutoProcessor`, for more control over generation (model card).
- **Other runtimes:** the vault catalogue lists conversions of the Whisper family for CTranslate2 (`Systran/faster-whisper-*`) and CoreML (`argmaxinc/whisperkit-coreml`). They were not checked for this article.

## Settings and usage

From the model card, unless stated otherwise:

- **Language:** detected automatically. If it is known, pass it: `generate_kwargs={"language": "english"}`. In our test, setting it saved about 8 % of the time on the long audio.
- **Task:** `"transcribe"` by default; `"translate"` produces English text.
- **Timestamps:** `return_timestamps=True` for sentences, `return_timestamps="word"` for words.
- **Long audio:** two algorithms. *Sequential* (sliding 30 s window) is the default and is recommended when "transcription accuracy is the most important factor". *Chunked* (`chunk_length_s=30`) splits the audio and is recommended when speed matters most. **On the reference CPU, chunked mode was slower (RTF 1.76 vs 1.09), used more memory (5.0 vs 3.9 GB) and repeated sentences at the joins.** Our recommendation for this machine is the sequential mode.
- **Decoding heuristics:** the card shows temperature fallback `(0.0, 0.2, 0.4, 0.6, 0.8, 1.0)`, `compression_ratio_threshold=1.35`, `logprob_threshold=-1.0` and `no_speech_threshold=0.6`. Not tested separately.

## Who uses it and for what

- The model card says the primary intended users are "AI researchers", and that Whisper is "also potentially quite useful as an ASR solution for developers, especially for English speech recognition".
- The vault catalogue shows several conversions of Whisper among the most downloaded speech models (CoreML for Apple devices, CTranslate2). We did not verify any named product or organization that uses large-v3-turbo.

## Why it matters

It brings the quality of Whisper's largest model to an ordinary computer. Cutting the decoder from 32 to 4 layers makes generation much cheaper, because the decoder runs once per output token while the encoder runs once per 30-second window. On a laptop without a GPU it transcribed at about real time with less than 4 GB of RAM.

## Behind the model

- **Organization:** OpenAI.
- **Paper authors:** Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey and Ilya Sutskever (BibTeX in the model card, 2022).
- **Release on the Hub:** repository created on 2024-10-01 (Hugging Face API). Details of the turbo version are in a GitHub discussion linked from the card (https://github.com/openai/whisper/discussions/2363), not reviewed for this article.
- **Model card:** "partly been written by the Hugging Face team, and partly copied and pasted from the original model card" (disclaimer in the card).

## Curiosities

- **Hallucinations:** the card says that, because of weak supervision on noisy data, "the predictions may include texts that are not actually spoken in the audio input". It also warns about repetitive text.
- **Responsible use:** the card cautions "against using Whisper models to transcribe recordings of individuals taken without their consent".
- **Uneven languages:** accuracy is lower on languages with less training data, and differs by accent and dialect (card).
- **TTS → ASR round trip:** for our test we generated the audio with Kokoro-82M (article 001) and transcribed it with Whisper. The text came back right, but with the numbers written as digits ("dieciséis gigas" → "16 GB").

---

## Families

| Family | Value | Reason |
|--------|-------|--------|
| Group (architecture) | Transformer encoder-decoder | Not in the series' list of groups (decoder, encoder…); it combines both. |
| Category | Paradox | A pruned and fine-tuned variant of a known model (large-v3). |
| Tier (parameters) | NU (< 1 B) | 808.9 M parameters. |
| Type (modality) | Audio → text | Speech recognition and translation. |
| Evolutionary line | Whisper → large-v2 → large-v3 → large-v3-turbo | Model card size table. Release dates of each version not verified here. |
| Ditto | Partly | The card has a fine-tuning section and says it can improve "with as little as 5 hours of labelled data". |

---

## How to run it

**Status: tested on the reference machine on 2026-11-14** (Windows 11, Python 3.12.10, 15.7 GB RAM, CPU only). Script and full results in `lab-asr/` (`transcribir.py` and `README.md`).

### a. Prerequisites

- Python 3.12, about 2 GB of disk for the weights plus the PyTorch install.
- About 4 GB of free RAM.

### b. Virtual environment

```powershell
cd lab-asr
python -m venv .venv
```

### c. Installation

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install transformers accelerate soundfile imageio-ffmpeg
```

Tested versions: torch 2.15.0+cpu, transformers 5.23.0. `imageio-ffmpeg` brings its own ffmpeg, so mp3, m4a and opus files can be read without installing ffmpeg.

### d. Minimal example

```python
import torch
from transformers import pipeline

asr = pipeline("automatic-speech-recognition",
               model="openai/whisper-large-v3-turbo",
               torch_dtype=torch.float32, device="cpu")
print(asr("audio.wav", return_timestamps=True)["text"])
```

The lab script does the same for any format and saves the text in a `.txt` next to the audio:

```powershell
.\.venv\Scripts\python.exe transcribir.py C:\path\to\note.opus --idioma es
```

### e. Check

With the test clip in Spanish (8.7 s), the output is: "El modelo Whisper convierte la voz en texto. Hoy hemos probado la transcripción en un ordenador sin tarjeta gráfica con 16 GB de memoria." Model load: 107.6 s the first time (with download), about 5 s after that.

### f. Warnings

- **Download:** 1.6 GB of weights to the Hugging Face cache on the first run. Windows shows a warning about symlinks; it does not stop the run.
- **License:** MIT, commercial use allowed.
- **Hardware:** on CPU, count on about as long as the audio for long files, and about 30 s minimum for short ones.
- **Mixed languages:** in a discarded test with Spanish and English sentences alternating, Whisper left the sentences in the second language empty. With audio in a single language, all sentences came out.
- **Test audio:** clean synthetic voice. Real recordings with noise or several speakers were not tested.

## Verification notes

| Data | Value | Source | Verified? |
|------|-------|--------|-----------|
| Parameters | 808,878,080 | Hugging Face API (`safetensors`) | Yes |
| License | MIT | Model card metadata | Yes |
| Architecture | Transformer encoder-decoder; 32 encoder and 4 decoder layers | Model card; `config.json` | Yes |
| Pruned from large-v3 (32 → 4 decoder layers) | as quoted | Model card | Yes |
| Training data | ">5M hours of labeled data" | Model card (the "Training Data" section says "No information provided") | Yes (card statement) |
| Languages | 99 codes in metadata; "strong ASR results in ~10 languages" | Model card | Yes |
| Library | `transformers` | Model card | Yes |
| Release on the Hub | 2024-10-01 | Hugging Face API (`createdAt`) | Yes |
| Weight size | 1,617,824,864 bytes | HTTP header of `model.safetensors` | Yes |
| RAM on CPU | 3.84–3.90 GB (sequential), 5.00 GB (chunked) | Measured, `lab-asr`, 2026-11-14 | Yes (measured) |
| Speed on CPU | RTF 1.09–1.19 on 75 s; about 30 s for clips under 30 s | Measured, `lab-asr`, 2026-11-14 | Yes (measured) |
| Authors / organization | OpenAI; Radford et al. (2022) | Model card BibTeX | Yes |
| Downloads / likes | 4,821,167 (30 days) / 3,530; 128,306,528 all time | Hugging Face API (snapshot 2026-11-14) | Yes |
| Users or organizations | — | — | **Not verified** |

## Pending

- **Real recordings:** test a real voice note and a noisy recording; the test used clean synthetic voice.
- **Release history:** the release dates of large-v2, large-v3 and turbo, and the content of GitHub discussion #2363, were not reviewed.
- **Faster runtimes:** an int8 version with CTranslate2 (faster-whisper) could be faster on CPU. Not tested.
- **large-v3:** not tested on the machine, so the speed difference with turbo is not measured.
- **Card:** no LaTeX card in `carta/` yet (tone 04, turquoise, `\artwave`).
