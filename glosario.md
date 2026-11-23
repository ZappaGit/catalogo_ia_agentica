# Glossary · IA 365 models

Explanations of the terms that appear in the series' articles. Each term links to the articles where it is used.

Articles: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md) · [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md) · [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md) · [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md) · [005 · llama.cpp](posts/005-01-NU-S-llama-cpp.md) · [006 · OpenClaw](posts/006-01-NU-S-openclaw.md) · [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md) · [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md) · [009 · Z-Image-Turbo Q4](posts/009-05-UU-P-z-image-turbo-q4.md) · [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md) · [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

---

## Audio and speech

### TTS (Text-to-Speech)
Converting written text into spoken voice. Input: text. Output: an audio file.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### ASR (Automatic Speech Recognition)
The reverse of TTS: converting speech into text. Whisper is an example.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md) (as a contrast) · [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

### Text normalization
A step before TTS that converts abbreviations, numbers and symbols into words ("Dr. 3" → "doctor three").
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### G2P (grapheme-to-phoneme) and phonemes
G2P converts each written word into its sounds (phonemes). In Kokoro this is done by the `misaki` library.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### Prosody
The intonation, rhythm, pauses and emphasis of a sentence. The prosody module of a TTS decides how a sentence sounds, not just which words it says.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### Spectrogram
A representation of sound as the intensity of each frequency over time. It is the intermediate "image" that many speech models generate before reaching the audio waveform. Whisper does the reverse: it turns the audio into a log-Mel spectrogram (frequencies on the Mel scale, closer to human hearing) and reads the text from it.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md) · [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

### STFT and iSTFT
- **STFT** (short-time Fourier transform): converts an audio signal into a spectrogram.
- **iSTFT**: the inverse operation, which converts a spectrogram back into audio.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### Vocoder
A module that converts an intermediate representation (a spectrogram or similar) into the final waveform.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### ISTFTNet
A vocoder that predicts the magnitude and phase of each sound fragment and uses the iSTFT to obtain the audio. It is faster than generating each audio sample directly.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### StyleTTS 2
A TTS architecture published in 2023 (Li et al.). It has a text encoder, a prosody module, a module that generates the voice style, and a decoder.
Kokoro takes only the decoder and the ISTFTNet approach; it does not include the diffusion module or the published encoder.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### Encoder-decoder (sequence-to-sequence)
A Transformer with two parts: the encoder reads the whole input (in Whisper, 30 seconds of audio) and the decoder writes the output token by token while looking at it. Whisper large-v3-turbo keeps 32 encoder layers and cuts the decoder to 4.
Appears in: [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

### RTF (real-time factor)
Processing time divided by the duration of the audio. Below 1, the system is faster than real time; 1 means it takes as long as the audio lasts.
Appears in: [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

### Hallucination (in speech recognition)
Text in a transcription that was never said in the audio. The Whisper model card attributes it to training on large amounts of noisy data.
Appears in: [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

### Pruning
Removing parts of a trained model (layers, neurons) to make it smaller and faster, usually followed by more training to recover quality. Whisper large-v3-turbo is a pruned large-v3.
Appears in: [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

### Physical modelling (articulatory synthesis)
Making a voice by simulating the body that produces it (lungs, vocal folds, throat, tongue, lips, nose) instead of playing recordings or learning from data. Each control has a physical meaning, such as the position of the tongue.
Appears in: [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md)

### Vocal tract and glottis
The **glottis** is the opening between the vocal folds; its opening and closing produces the buzz of the voice. The **vocal tract** is the tube above it (throat, mouth, nose) whose shape filters that buzz into vowels and consonants.
Appears in: [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md)

### Formant
A resonance of the vocal tract: a band of frequencies that the tract's shape reinforces. The first two formants are what tells one vowel from another.
Appears in: [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md)

### FDTD (finite-difference time-domain)
A numerical method that simulates a wave step by step in time and space. CHIMERA uses it to compute air pressure and airflow along the sections of the vocal tract.
Appears in: [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md)

### WebAssembly and AudioWorklet
**WebAssembly** (wasm) is a compiled code format that browsers run at near-native speed. An **AudioWorklet** is the browser's real-time audio thread; it needs a secure context (HTTPS or localhost).
Appears in: [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md)

---

## Text architectures

### Transformer
An architecture that processes sequences of tokens with attention mechanisms. It is the basis of almost all current LLMs.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Decoder-only
A variant of the transformer that has only the generation part. It produces text one token at a time, and each token depends on the previous ones. GPT and Qwen are of this type.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Token
The smallest unit of text the model processes. It can be a word, part of a word or a symbol. Context and speed are measured in tokens.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Context (context window)
The maximum number of tokens the model can take into account at once (input plus response). Qwen3-8B has 32,768 native tokens and up to 131,072 with YaRN.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### GQA (Grouped-Query Attention)
An attention variant in which several query "heads" share the same keys and values. It reduces the memory the model needs when generating long text. Qwen3-8B uses 32 query heads and 8 key/value heads.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### KV cache
Memory where the model stores the keys and values of tokens already processed, so they do not have to be recomputed. It grows with the length of the context, which is why long texts need more memory even when the model is the same.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Soft switch (`/think` and `/no_think`)
Commands written in the user's message to turn Qwen3's reasoning on or off turn by turn. They only work if `enable_thinking=True`; with `enable_thinking=False` they are ignored.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md), [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md) · [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Thinking mode
The model generates a reasoning block before the answer. It gives better results in mathematics and code, but produces longer and slower outputs. Qwen3 allows it to be turned on or off.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Chat template
A template that converts the list of messages (user, assistant, system) into the format of special tokens the model expects.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

---

## Phases of generating a response

The order in which the phases occur when a response is generated. Each entry refers to the diagram in [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process).

1. Chat template → 2. Tokenization → 3. Embedding → 4. Transformer blocks (each with 8 internal steps, see below) → 5. Logits → 6. Sampling → 7. End or new token.

### Chat template (phase 1)
Before tokenization, the list of messages is turned into a single text with the model's role tags. With `enable_thinking=False`, the template adds an empty `<think>` block so the model answers directly.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### Tokenization (phase 2)
The step that converts text into a list of token IDs, using the tokenizer's vocabulary (151,669 entries in Qwen3-8B). It is the same step the tokenizer performs before the model sees anything. See [fundamentos-llm/01-tokenizacion.md](fundamentos-llm/01-tokenizacion.md).
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### Embedding (phase 3)
A table that replaces each token ID with a vector of numbers (4,096 values in Qwen3-8B). It is the first thing the model receives.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### Transformer block (phase 4)
Each block applies the same operations, one after another. Qwen3-8B has 36 blocks, so each token's vector passes through all of them. Inside each block:
1. **RMSNorm**: normalizes the vector before attention.
2. **Q, K and V projections**: create the query, key and value of each token.
3. **QK-Norm**: normalizes Q and K for each head before comparing them.
4. **RoPE**: encodes the token's position within the Q and K vectors.
5. **Causal attention with KV cache**: each token looks only at the previous ones (see the entries below).
6. **Residual connection**: adds the block's input to the attention output.
7. **RMSNorm** and **SwiGLU MLP**: a second computation step, with a gate that decides how much information passes.
8. **Residual connection**: adds again, and the result is the input of the next block.

Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### RMSNorm
A normalization that scales each vector by its root mean square, without subtracting the mean. It is simpler than LayerNorm and is used before each attention and MLP sublayer.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### QK-Norm
An extra normalization that applies RMSNorm to the query (Q) and key (K) of each head. It helps keep the product that measures attention from blowing up in large models. Qwen3 includes it in its implementation.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### RoPE (Rotary Position Embedding)
A way of encoding position by rotating the pairs of values in Q and K according to the token's number. The base used in Qwen3-8B is theta = 1,000,000. This lets the model know which token comes before another without needing a position table.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### Causal attention
Attention in which each token can only look at itself and the tokens before it, never at the ones after. It is what allows text to be generated from left to right. It is computed by comparing the current token's query with the keys of all the previous tokens, and using the result to mix their values.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### Residual connection
Adds a block's input to its output. The original signal still reaches the deep layers, which is how a 36-block model can be trained.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### SwiGLU MLP
The part of the block that transforms each token vector one token at a time, without looking at other tokens. It uses three matrices: it expands from 4,096 to 12,288 values, multiplies two paths (one passed through SiLU, which acts as a gate) and reduces back to 4,096. In Qwen3-8B, SwiGLU is the form of the MLP.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### Prefill and decode
Two calculation modes. In **prefill** the model processes all the input tokens at once and fills the KV cache. In **decode** it generates one new token at a time, using the cache. The speed in tokens per second is mainly measured in the decode phase.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### LM head and logits (phase 5)
The final linear layer: it converts the final vector of each token into a number (logit) for each vocabulary token. A high logit indicates that the token is likely to come next. In Qwen3-8B, the layer has 151,936 outputs and does not share weights with the embedding.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### Sampling: temperature, top-p and top-k (phase 6)
How the next token is chosen from the logits:
- **Temperature**: scales the logits. Low values make the choice more conservative; high values, more varied. The Qwen3 model card recommends 0.6 in thinking mode.
- **Top-k**: only the k tokens with the highest logit are considered (20 in the Qwen3 recommendation).
- **Top-p**: the most probable tokens are considered until their cumulative probability reaches p (0.95 in the Qwen3 recommendation).

The model card asks not to use greedy decoding, which always picks the token with the highest logit.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### End-of-sequence token (EOS) (phase 7)
A special token that indicates the response has finished. If the model generates it, the loop stops. If not, the chosen token is added to the context and the process repeats from the embedding.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

### Decoding
The last step: converts the list of generated IDs back into text. With `skip_special_tokens=True` the special tokens are removed, but the text of a `<think>` block is kept.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#internal-process)

---

## Models and weights

### Parameters
Numbers the model learns during training. "82 M" means 82 million; "8.2 B" means 8.2 billion. More parameters usually mean more capacity and more memory required.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Parameters without embeddings
The model's parameters, not counting the embedding table (the one that converts tokens into vectors). It is a figure more representative of the "reasoning" part of the model when the vocabulary is large. In Qwen3-0.6B, 0.44 B out of 0.6 B.
Appears in: [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md) · [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Weights
The concrete values of the parameters, stored in a file. They take up most of the memory when the model runs.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Safetensors
A file format for storing weights. It is safer than the older PyTorch format because it does not execute code when loaded.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Precision: FP16, BF16, INT8 and INT4
How many bits each weight takes up:
- **FP16 / BF16**: 16 bits (2 bytes). BF16 has the same range as FP32, with less precision.
- **INT8**: 8 bits (1 byte).
- **INT4**: 4 bits (0.5 bytes).

Fewer bits = less memory, with some loss of quality.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Quantization
Reducing the precision of the weights (for example, from BF16 to INT4) so the model fits in less memory. Names such as Q8_0 or Q4_K_M indicate the quantization scheme of a GGUF file.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md) · [005 · llama.cpp](posts/005-01-NU-S-llama-cpp.md) · [009 · Z-Image-Turbo Q4](posts/009-05-UU-P-z-image-turbo-q4.md)

### GGUF
A file format for storing quantized models, with the weights and the metadata needed to run them. It is the format read by llama.cpp.
Appears in: [005 · llama.cpp](posts/005-01-NU-S-llama-cpp.md) · [009 · Z-Image-Turbo Q4](posts/009-05-UU-P-z-image-turbo-q4.md)

### Hardware: VRAM and RAM
- **VRAM**: graphics card memory. It moves the weights the fastest.
- **RAM**: system memory. It allows running the model on CPU, but it is much slower.
Appears in: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Hardware estimate
Formula used in the series: weight memory ≈ parameters × bytes per parameter, plus a 20–30 % margin for context and activations. It is an approximation; the real measurement depends on the environment.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

---

## Embeddings and similarity

### Sentence embedding
A fixed-length vector of numbers that represents the meaning of a whole sentence or short text. Texts with similar meaning get vectors that are close to each other. It is the output of embedding models such as all-MiniLM-L6-v2 (384 values).
Appears in: [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Cosine similarity
A measure of how much two vectors point in the same direction, from -1 (opposite) to 1 (same direction). It is the usual way to compare sentence embeddings.
Appears in: [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Mean pooling
Turning the vectors of all the tokens into one sentence vector by averaging them, ignoring the padding (using the attention mask). Used by all-MiniLM-L6-v2.
Appears in: [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Contrastive training
Training that teaches the model to bring the vectors of matching pairs (for example, a question and its answer) closer together, and to push apart those of non-matching pairs in the same batch.
Appears in: [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Encoder-only
A transformer that reads the whole input and produces a representation for it, without generating text token by token (unlike a decoder-only model). BERT and all-MiniLM-L6-v2 are of this type.
Appears in: [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

---

## Other concepts

### Diffusion
A generative method that starts from noise and refines it in several steps until it reaches the result. It is used in image generation and, in some TTS models, for the voice style. Kokoro does not use it.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md) · [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md) · [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md)

### DiT (Diffusion Transformer)
A diffusion model whose denoiser is a transformer instead of a convolutional network. The text and the image tokens are processed by the transformer, which predicts the noise to remove at each step.
Appears in: [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md)

### Distillation (distilled model)
Training a smaller or faster model (the student) to reproduce the result of a larger one (the teacher) with fewer steps or less computation. Z-Image-Turbo is distilled from the 50-step Z-Image base model to 8 steps.
Appears in: [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md)

### Guidance (classifier-free guidance, CFG)
A setting that makes the image follow the prompt more closely. It usually needs a second pass of the model per step; the distilled Turbo model runs with guidance scale 0, so it does not need that pass.
Appears in: [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md)

### VAE (variational autoencoder)
A network that compresses the image into a smaller latent representation and decodes it back to pixels. The diffusion model works in that compressed space, which saves memory and time.
Appears in: [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md)

### Latent diffusion
Diffusion done in a compressed representation (the latent) instead of in pixels. A VAE compresses the image before the denoising and decodes the result at the end, which saves memory and time.
Appears in: [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md)

### U-Net
A convolutional network with an encoder and a decoder joined by skip connections. In Stable Diffusion 1.5 it is the denoiser: at each step it predicts the noise to remove.
Appears in: [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md)

### CLIP (text encoder)
A text encoder trained to match texts with images. In Stable Diffusion 1.5 it turns the prompt into vectors that guide the denoising.
Appears in: [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md)

### stable-diffusion.cpp
An open-source C/C++ runtime for image diffusion models, with a CPU backend, a command-line tool and an HTTP server. It is a runtime, not a model; articles 008 and 009 run with it.
Appears in: [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md) · [009 · Z-Image-Turbo Q4](posts/009-05-UU-P-z-image-turbo-q4.md)

### llama.cpp
An open-source inference engine in C/C++ that runs models in GGUF format, with a command-line tool and an HTTP server with an OpenAI-compatible API. It is a runtime, not a model.
Appears in: [005 · llama.cpp](posts/005-01-NU-S-llama-cpp.md) (also [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md) and [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md) as an option to run the model)

### Gateway (control process)
A local program that stays running and manages sessions, tools, events and the connections to the outside (for example messaging channels). In OpenClaw, the Gateway is the control plane; the Control UI, the CLI and the TUI connect to it. It is not a model.
Appears in: [006 · OpenClaw](posts/006-01-NU-S-openclaw.md)

### Families (IA 365 models series)
The series' own classification, inspired by how Pokémon are grouped: group (architecture), category (Starter, Legendary, etc.), tier by parameters (NU, RU, UU, OU, Uber), type (modality) and evolutionary line. It is an educational resource, not an official classification.
Appears in: [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md) · [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Model card
The model's page on Hugging Face, with description, usage, license and training data. It is the main source of the series' data.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Apache 2.0 License
A permissive license that allows commercial use, modification and redistribution, with a copyright notice. It is the one used by Kokoro and Qwen3-8B.
Appears in: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)
