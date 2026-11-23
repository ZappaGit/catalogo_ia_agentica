# 002 · Qwen3-8B

**Main source:** https://huggingface.co/Qwen/Qwen3-8B
**License:** Apache 2.0
**Consulted:** 2026-11-06
**Code:** 01-UU-S-002 (catalogue 01 Text and LLMs · UU · Starter)
**Associated Pokémon:** Porygon — a Pokémon made of computer code, born in the digital world; a language model that is pure software and can switch between "thinking" and "answering quickly" fits that idea.

---

## Summary

One model, two ways of thinking: Qwen3-8B switches between reasoning step by step and answering quickly, with the same set of weights.

Qwen3-8B is an open-weight causal language model (text generation) from the Qwen team, with 8.2 billion parameters, published under the Apache 2.0 license, which also allows it to be used in commercial projects.

🔧 **Type and technology:** decoder-only transformer with grouped-query attention (GQA: 32 query heads and 8 key/value heads), 36 layers. Thinking mode is on by default and can be turned off per request. Used from Python with `transformers`.
📏 **Size:** 8.2 B parameters (6.95 B without embeddings). Native context of 32,768 tokens, up to 131,072 with YaRN. BF16 weights (safetensors), about 16.4 GB.
💻 **Minimum hardware:** about 24 GB of VRAM for the BF16 weights, with some margin; about 10 GB at 8 bits and about 5 GB at 4 bits *(estimate: 8.19 B × bytes per parameter, plus a 20–30 % margin; see verification notes)*.
🛠️ **Interfaces:** Python (`transformers`), SGLang and vLLM (server compatible with the OpenAI API), and local applications such as Ollama, LM Studio, MLX-LM and llama.cpp, according to the model card.
👥 **Who uses it and for what:** reasoning, code, mathematics, agents with external tools, and multilingual chat and translation (more than 100 languages and dialects, according to the model card). It has about 7 million downloads on Hugging Face (snapshot of 2026-11-06).
💡 **Why it matters:** a single model covers both fast chat and long reasoning, so there is no need for two different models for each case.
🏢 **Behind the model:** the Qwen team, which develops the Qwen models; the model card cites the Qwen3 technical report (arXiv:2505.09388).
🤓 **Curiosity:** you can switch mode mid-conversation by adding `/think` or `/no_think` to your message.

Model card and example: https://huggingface.co/Qwen/Qwen3-8B

---

## Settings: thinking mode

- **Per-turn switch:** `/think` and `/no_think` in the user message change the mode for that response only (example from the model card).
- **Recommended sampling:** in thinking mode, Temperature 0.6, TopP 0.95 and TopK 20. The model card says **not** to use greedy decoding.
- **Response length:** in thinking mode the outputs are long. The model card suggests `max_new_tokens` of 32,768 so the response is not cut off.

## Minimum hardware

| Precision | Weights | With 20–30 % margin | Recommended |
|-----------|---------|---------------------|-------------|
| BF16 / FP16 | 8.19 B × 2 B ≈ 16.4 GB | ≈ 19.7–21.3 GB | GPU with 24 GB of VRAM |
| INT8 | 8.19 B × 1 B ≈ 8.2 GB | ≈ 9.8–10.6 GB | GPU with 12 GB of VRAM |
| INT4 | 8.19 B × 0.5 B ≈ 4.1 GB | ≈ 4.9–5.3 GB | GPU with 8 GB of VRAM |

Long contexts need extra memory for the KV cache, so the margin is a rough estimate. CPU inference uses system RAM instead of VRAM and is much slower.

## Interfaces

- `transformers` (`AutoModelForCausalLM`, `AutoTokenizer`).
- SGLang (`sglang>=0.4.6.post1`) and vLLM (`vllm>=0.8.5`) for an OpenAI-compatible API.
- Ollama, LM Studio, MLX-LM, llama.cpp and KTransformers, which the model card lists as compatible with Qwen3.

## Who uses it and why

- Developers who need an open model for both reasoning and fast chat.
- Agent systems, because the model card highlights tool calling in both modes.
- The model card reports about 7 million downloads and 2,170 likes (snapshot 2026-11-06). It does not cite specific production users, so none are cited here.

## Why it matters

Qwen3-8B lets the same model reason at length on mathematics or code and answer briefly in everyday chat, controlled by a switch in the chat template or in the prompt. Its Apache 2.0 license allows commercial use.

## Behind the model

- **Organization:** Qwen team (the model card mentions Alibaba).
- **Authors:** listed in the Qwen3 technical report, arXiv:2505.09388, as "Qwen Team". The model card does not name individual authors. *(Pending: confirm the wording of the affiliation in the article.)*

---

## How to run it

**Status: generates text on the work machine, but far too slowly to use.** Qwen3-8B produced a response on the work machine (see item "i"), at about 0.1 tokens per second, because most of the weights run from disk. The timings in item "h" come from the Qwen3-0.6B script, not from the 8B. The commands had been checked against the model card and the PyPI index.

### a. Prerequisites

- Python 3.10 or newer (the machine has Python 3.12.10).
- Windows 11. An NVIDIA GPU with CUDA and about 24 GB of VRAM is recommended; the CPU works but is slow and needs about 24 GB of RAM.
- Optional: WSL 2 with Ubuntu, if you prefer Linux tools.

### b. Virtual environment

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

WSL (Ubuntu):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### c. Installation

First install PyTorch, choosing the CUDA version that matches your GPU from https://pytorch.org (the default `pip install torch` may not use the GPU).

```powershell
python -m pip install --upgrade pip
pip install torch
```

Then the Hugging Face libraries:

```powershell
pip install "transformers>=4.51.0" accelerate
```

`accelerate` is required for `device_map="auto"`.

### d. Minimal example

Save it as `run_qwen3.py` in a folder outside the project (for example, in the scratchpad folder), not in the global Python environment:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen3-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
)

messages = [{"role": "user", "content": "Give me a short introduction to large language models in two sentences."}]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,  # no reasoning block: shorter answer
)
inputs = tokenizer([text], return_tensors="pt").to(model.device)

output_ids = model.generate(**inputs, max_new_tokens=128)
new_tokens = output_ids[0][len(inputs.input_ids[0]):]
print(tokenizer.decode(new_tokens, skip_special_tokens=True).strip())
```

Run it:

```powershell
python run_qwen3.py
```

The model card is not gated, so no Hugging Face token is needed. If you have one (for faster downloads or higher rate limits), set it in the shell and never in the code:

```powershell
$env:HF_TOKEN = "<your-token>"
```

### e. Check

The expected result is two sentences about language models printed to the console, without `<think>` tags, because the example disables thinking. If the output is empty or the process runs out of memory, check the warnings below.

### f. Warnings

- **Download size:** about 16.4 GB in BF16, stored in the Hugging Face cache (`%USERPROFILE%\.cache\huggingface`).
- **License:** Apache 2.0. No terms need to be accepted on Hugging Face.
- **Hardware:** the example runs on CPU but is slow. On a GPU it needs about 24 GB of VRAM in BF16; with less VRAM, load a quantized version.
- **Thinking mode:** it is on by default and generates long outputs. Set `max_new_tokens` high (the model card suggests 32,768) if you use that mode.

### g. Why the weights are needed and why the download takes time

- **The weights are the model.** The code only describes how the answer is computed; the 8.2 billion parameters are the values the model learned during training. Without them there is no knowledge to use, and the program cannot generate anything.
- **They cannot be generated locally.** Training a model like this requires GPU clusters for weeks, so the only practical option is to download the already-trained weights from Hugging Face.
- **The download is large.** Qwen3-8B takes up about 16.4 GB in BF16. Also, without a Hugging Face token, requests are rate-limited, and the time depends on the connection and the server load.
- **In the 0.6B lab:** Qwen3-0.6B takes up about 1.2 GB. The first download on this machine, without a token, had not finished when this was written. *(Pending: note the actual time.)* As a rough estimate proportional to size, the 8B (16.4 GB) would take about 13 times longer.
- **How to speed it up:** set `HF_TOKEN` (done once per session, never in the code), download at a time with less traffic, or use a quantized version, which is smaller.

### h. Run result of Qwen3-0.6B (not 8B)

These timings come from `lab-llm/test_qwen3_06b.py`, the 0.6B script, run on the work machine (Intel Core i7-1355U, 16 GB RAM, CPU only). They are **not** Qwen3-8B results. The 0.6B run printed `parámetros: 0.60 B` and loaded in 4.7 s, because its weights were already in the cache.

Two generations, one without thinking and one with `enable_thinking=True` and `max_new_tokens=256`:

| Run | Tokens generated | Time | Speed |
|-----|------------------|------|-------|
| `enable_thinking=False`, `max_new_tokens=128` | 56 | 10.3 s | 5.4 tokens/s |
| `enable_thinking=True`, `max_new_tokens=256` | 166 | 33.4 s | 5.0 tokens/s |

What is seen in the output:

- Without thinking, the answer is two sentences about LLMs, without `<think>`.
- With thinking, the text starts with a `<think>` block and the answer comes after it. The 166 tokens are within the 256-token limit.
- The `<think>` block appears in the decoded output. To get only the answer, the text has to be split at `</think>`.

### i. Script de prueba en español (`lab-llm/test_qwen3_8b.py`)

Versión en español de la prueba del 0,6 B ([test_qwen3_06b.py](../lab-llm/test_qwen3_06b.py)). Hace lo mismo para el 8B: carga el modelo, genera una respuesta sin razonamiento y otra con razonamiento, y mide los tiempos. El prompt está en español, así que sus tiempos no son directamente comparables con la ejecución en inglés de arriba.

Parámetros al principio del script:

| Parámetro | Valor | Qué controla |
|-----------|-------|--------------|
| `MODELO` | `Qwen/Qwen3-8B` | Modelo que se descarga y se carga |
| `PROMPT` | "Dame una introducción breve a los modelos de lenguaje grandes en dos frases." | Pregunta de prueba |
| `TIPO_DE_DATO` | `torch.bfloat16` | Precisión de los pesos. En BF16 ocupan ~16,4 GB; en float32, ~33 GB |
| `DISPOSITIVO` | `"auto"` | `device_map`: reparte los pesos entre GPU y CPU |
| `MAX_TOKENS_SIN_RAZONAMIENTO` | 128 | Límite de tokens nuevos sin razonamiento |
| `MAX_TOKENS_CON_RAZONAMIENTO` | 256 | Límite con razonamiento. La ficha sugiere 32.768 para no cortar el razonamiento |
| `USAR_MUESTREO` | `False` | `False` = decodificación voraz (`do_sample=False`), como en el script del 0,6 B. `True` aplica el muestreo de la ficha |
| `TEMPERATURA` / `TOP_P` / `TOP_K` | 0,6 / 0,95 / 20 | Solo se usan si `USAR_MUESTREO` es `True`. Son los valores recomendados por la ficha para el modo con razonamiento |

Requisitos: una GPU con unos 24 GB de VRAM. En el equipo de referencia (16 GB de RAM, sin CUDA) el modelo no cabe; ver los límites en [lab-llm/README.md](../lab-llm/README.md).

**Resultado de la ejecución en el equipo de referencia (15,7 GB de RAM, gráfica integrada sin CUDA):**

- **Carga:** 548,1 s, incluida la descarga de 16,4 GB (unos 8 minutos).
- **Aviso:** `transformers` indicó que algunos parámetros estaban "en el dispositivo meta porque se descargaron a disco y CPU". El modelo no cabe en RAM, así que parte de los pesos se lee desde el disco en cada paso.
- **Respuesta sin razonamiento (127 tokens):** 2.078 s, unos 0,1 tokens/s. El texto es una lista de cinco puntos sobre los mayores logros de la humanidad, en español.
- **Respuesta con razonamiento:** no terminó. La ejecución se detuvo a mano durante esa parte, sin salida.

Con esta velocidad, una respuesta corta tarda unos 35 minutos. Es una prueba de que el modelo funciona, no de uso práctico.

*(Pendiente: repetir en una máquina con GPU de unos 24 GB de VRAM, o usar una versión cuantizada (GGUF, 4 bits) en llama.cpp u Ollama en el equipo de referencia, y anotar los tiempos.)*

---

## Internal process

The diagrams follow the `transformers` code (`modeling_qwen3.py`) and the model's `config.json`. The figures in parentheses come from that file (see verification notes).

### 1. What happens when a response is generated

```mermaid
flowchart TD
    A[User message] --> B["Chat template<br/>enable_thinking: if False, adds an empty think block"]
    B --> C["Tokenizer<br/>text → token IDs"]
    C --> D["Embedding<br/>IDs → vectors of 4096 values"]
    D --> E["36 transformer blocks<br/>(see diagram 2)"]
    E --> F["Final RMSNorm"]
    F --> G["LM head<br/>4096 → 151,936 logits, one per vocabulary token"]
    G --> H["Sampling<br/>temperature, top-p, top-k"]
    H --> I{End of response?}
    I -- No --> J["New token → embedding<br/>previous K and V are reused from the KV cache"]
    J --> E
    I -- Yes --> K["Decoded text"]
```

The loop repeats once for each new token. That is why speed is measured in tokens per second: each token requires passing through all 36 blocks again.

### 2. One transformer block

```mermaid
flowchart TD
    X["Input h (4096)"] --> N1["RMSNorm"]
    N1 --> QKV["Projections: Q with 32 heads, K and V with 8 heads, 128 dimensions per head"]
    QKV --> QN["QK-Norm: RMSNorm applied to Q and to K per head"]
    QN --> R["RoPE (position rotation, theta = 1,000,000)"]
    R --> ATT["Causal GQA attention<br/>scale 1/√128, with KV cache"]
    ATT --> O["Output projection (32 × 128 → 4096)"]
    O --> S1(("sum"))
    X --> S1
    S1 --> N2["RMSNorm"]
    N2 --> FFN["SwiGLU MLP: 4096 → 12288 → 4096<br/>SiLU(gate) × up"]
    FFN --> S2(("sum"))
    S1 --> S2
    S2 --> Y["Block output (4096)"]
```

The arrows that skip from the input to the sum are the residual connections. They are what allows training 36 layers without the signal getting lost.

### 3. The thinking switch

```mermaid
flowchart LR
    P["Chat template"] --> T{"enable_thinking"}
    T -- "True (default)" --> TH["The model generates its reasoning<br/>between think and /think"]
    T -- "False" --> EM["The template adds an empty think block<br/>to the prompt"]
    TH --> R1["Response"]
    EM --> R2["Direct, shorter response"]
```

The repository's chat template adds `<think>\n\n</think>\n\n` when `enable_thinking` is false. The model thus receives the already-closed block and answers directly.

---

## Verification notes

| Data | Value | Source | Verified? |
|------|-------|--------|-----------|
| Parameters | 8.2 B (8,190,735,360 in the BF16 safetensors metadata) | Model card; HF API `safetensors.parameters` | Yes |
| Parameters without embeddings | 6.95 B | Model card | Yes |
| Layers / attention | 36 layers; 32 Q heads / 8 KV heads (GQA) | Model card | Yes |
| Context | 32,768 native; 131,072 with YaRN | Model card | Yes |
| License | Apache 2.0 | Model card metadata and link to LICENSE | Yes |
| Library | `transformers` ≥ 4.51.0 | Model card | Yes |
| Weight size | ≈ 16.38 GB (sum of 5 shards; 15.26 GiB) | HF API `?blobs=true` | Yes |
| Hardware (BF16) | ≈ 19.7–21.3 GB with margin | Calculation: 8.19 B × 2 B + 20–30 % | **Estimate** |
| Hardware (INT8 / INT4) | ≈ 10 GB / ≈ 5 GB | Calculation: 8.19 B × 1 B / 0.5 B + margin | **Estimate** |
| Downloads / likes | 7,000,357 / 2,170 | HF API, snapshot 2026-11-06 | Yes (snapshot) |
| Restricted access | No | HF API `gated: false` | Yes |
| Author | Qwen Team | Model card citation; arXiv:2505.09388 | Yes |
| Organization | Alibaba (mentioned in the model card) | Model card | Partial: affiliation wording pending |
| Publication date | Not stated in the model card | — | **Pending** |
| "How to run it" commands | Package names checked on PyPI: `transformers` (5.22.1 latest; 4.51.0+ available), `accelerate` (1.15.0), `torch` (2.15.0) | `pip index versions` | Names yes; 8B example not completed; 0.6B script run (see item "h") |
| Hidden size / intermediate | 4096 / 12288 | Repository `config.json` | Yes |
| Dimension per head | 128 | `config.json` (`head_dim`) | Yes |
| Vocabulary | 151,936 | `config.json` (`vocab_size`) | Yes |
| Embedding and LM head | Separate (no shared weights) | `config.json` (`tie_word_embeddings: false`) | Yes |
| RoPE base | theta = 1,000,000 | `config.json` (`rope_theta`) | Yes |
| MLP activation | SiLU, gated (SwiGLU) | `config.json` (`hidden_act`); `modeling_qwen3.py` | Yes |
| Normalization | RMSNorm (ε = 1e-6); QK-Norm on Q and K | `config.json`; `modeling_qwen3.py` (`q_norm`, `k_norm`) | Yes |
| Template with thinking disabled | Adds `<think>\n\n</think>\n\n` to the prompt | `tokenizer_config.json` (`chat_template`) | Yes |
| Local run timings (Qwen3-0.6B, not 8B) | 56 tokens in 10.3 s; 166 tokens in 33.4 s | Output of `test_qwen3_06b.py` run by the user (`parámetros: 0.60 B`) | Yes (one run; CPU, 16 GB RAM) |
| Qwen3-8B local run | Loaded in 548.1 s; 127 tokens in 2,078 s (0.1 tokens/s) without thinking; offload warning | Output of `test_qwen3_8b.py` run by the user | Yes (one run; CPU with disk offload) |

## Pending

- Publication date of Qwen3 (April 2025 is from memory; the model card does not confirm it).
- Confirm the wording of the affiliation with Alibaba in the technical report.
- Get the Qwen3-8B response with thinking enabled. The run was stopped by hand before it finished, so there is no output for that part.
- Repeat the 8B run on a machine that fits it (GPU of about 24 GB of VRAM), or with a quantized version, and record its timings. The 0.1 tokens/s above is from this machine with disk offload and should not be taken as the model's speed.
- Record the versions of `transformers` and `torch` used in the 0.6B run (the lab README lists them: 5.22.2 and 2.15.0+cpu).
- Verify the hardware figures by measuring peak VRAM in BF16 and in 4 bits.
- The model card asks for `transformers` ≥ 4.51.0 and the latest on PyPI is 5.22.1; check which version the example needs (the `torch_dtype` argument may change in newer versions).
