# 004 · all-MiniLM-L6-v2

**Main source:** https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
**License:** Apache 2.0
**Consulted:** 2026-11-08
**Code:** 02-NU-S-004 (catalogue 02 Embeddings and RAG · NU · Starter)
**Origin:** vault catalogue `IA_Agentica/HuggingFace`, "Top 10 global por descargas" table (snapshot 2026-11-05), first place by downloads. Not a text generation model or a voice model, which is why it was chosen for this slot.
**Families:** Starter · NU · Embeddings · Encoder (embeddings) · sentence-transformers line (see the "Families" section)

---

## LinkedIn text

The most downloaded model in our Hugging Face snapshot, and it does not write or speak: it turns a sentence into a list of 384 numbers.

all-MiniLM-L6-v2 is an embedding model with 23 million parameters. It maps a sentence or a short paragraph to a vector, so that texts with similar meaning end up close to each other. It is open-source, under the Apache 2.0 license.

🔧 **Type and technology:** encoder-only transformer with 6 layers (the card does not state it; see Pending), mean pooling and L2 normalization of the output. Trained for sentence similarity. Implemented in Python on PyTorch.
📏 **Size:** 22.7 M parameters, 384-dimensional output, input truncated to 256 word pieces. The repository weighs about 1.8 GB because it stores several formats (safetensors, ONNX, OpenVINO, TensorFlow, Rust), but the model itself is small.
💻 **Minimum hardware:** any CPU with about 0.2 GB of RAM, or the same on a GPU *(estimate: 22.7 M × 4 bytes in FP32 ≈ 91 MB, plus a runtime margin; not stated in the model card)*.
🛠️ **Interfaces:** Python with `sentence-transformers` (`model.encode(sentences)`), `transformers`, and ONNX, OpenVINO or Rust runtimes; the card also lists text-embeddings-inference.
👥 **Who uses it and for what:** the card names no companies or projects. It says the vectors can be used for information retrieval, clustering and sentence similarity. Its 178,968,052 downloads (as of 2026-11-08) are the main evidence of wide use.
💡 **Why it matters:** it is very small and runs on a laptop CPU, so a semantic search or a RAG prototype can be built without a GPU. Larger embedding models usually give better quality, but at a higher cost in memory and time *(our reading, not a benchmark from the card)*.
🏢 **Behind the model:** the `sentence-transformers` namespace on Hugging Face. The card says it was developed during a Hugging Face community week, using JAX/Flax, with TPU hardware and support from Google's JAX and Cloud team.
🤓 **Curiosity:** the card lists 1,170,060,424 training pairs, the largest source being about 726 million Reddit comments. The model was trained for a similarity task, not to write text.

Model card: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

#Embeddings #AI #OpenSource

---

## What it is

all-MiniLM-L6-v2 is an **embedding model** (sentence embeddings). It does not generate text: it reads a sentence and returns a fixed-length vector of 384 numbers. Two sentences with similar meaning produce vectors that point in similar directions, which can be measured with cosine similarity.

It is a sentence and short-paragraph encoder according to the card. The card's intended uses are information retrieval, clustering and sentence similarity.

## Type and technology

- **Task:** sentence embeddings (feature extraction / sentence similarity; `pipeline_tag: sentence-similarity` in the API).
- **Architecture:** encoder-only transformer, derived from `nreimers/MiniLM-L6-H384-uncased` (card). The card does not state the number of layers; the base model name suggests 6 layers, which is the "L6" in the name, but this has not been checked in `config.json`.
- **Pooling:** mean pooling over the token outputs, using the attention mask, followed by L2 normalization (the card's plain Transformers example uses `mean_pooling` and `F.normalize(..., p=2, dim=1)`).
- **Tokenizer:** WordPiece, uncased (the repository contains `vocab.txt`).
- **Training:** starts from the pretrained base model and is fine-tuned with a contrastive objective: cosine similarity over all pairs in the batch, with cross-entropy loss against the true pairs. The card reports TPU v3-8 hardware, 100 k steps, batch size 1024, learning rate 2e-5 with AdamW, and sequence length 128 during training.
- **Implementation language:** Python, on PyTorch through `sentence-transformers`. The repository also includes TensorFlow, ONNX, OpenVINO and Rust (`rust_model.ot`) exports.

## Size

- **Parameters:** 22,713,728 according to the API (`safetensors`: 22,713,216 F32 + 512 I64 tensor elements). The card page shows "22.7M params".
- **Output dimension:** 384.
- **Input length:** the card says text longer than 256 word pieces is truncated by default. Training used 128 tokens.
- **Format:** safetensors (F32). The API does not give the byte size of `model.safetensors`; the total repository storage is 1,845,474,494 bytes (about 1.8 GB, all formats included).

## Minimum hardware

| Precision | Weights | With margin | Reference |
|-----------|---------|-------------|-----------|
| FP32 (as published) | 22.7 M × 4 B ≈ 91 MB | ≈ 0.15–0.2 GB | Any CPU with 1 GB of RAM |
| FP16 / INT8 | ≈ 45 MB / ≈ 23 MB | < 0.1 GB | Not measured; no quantized variant in this analysis |

The margin covers the runtime, the tokenizer and the activations for a batch of sentences. These are estimates; no measurement has been made on the reference machine.

## Interfaces

- `sentence-transformers` (`SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')`, then `encode`), the usage example on the card.
- `transformers` (`AutoTokenizer`, `AutoModel`, with explicit mean pooling).
- ONNX, OpenVINO, Rust and TensorFlow exports listed on the card; text-embeddings-inference listed in the tags.
- Deployment tags for SageMaker and Azure endpoints appear in the model tags; they were not explored.

## Who uses it and for what

- The card does not name specific companies, products or papers that use it.
- Popularity figure (consulted 2026-11-08): 178,968,052 downloads and 6,079 likes on Hugging Face (API). The vault snapshot of 2026-11-05 gives 180.2 M downloads; the difference is the time between the two readings. Downloads are cumulative and favour older models, so they measure reach, not quality.
- Typical uses according to the card: semantic search, clustering of texts, and sentence similarity. The vault catalogue lists a cross-encoder reranker (`ms-marco-MiniLM-L6-v2`) among the top downloads, which is the usual companion for reordering results (our reading of the catalogue, not a statement from this card).

## Why it matters

It is the smallest useful kind of embedding model: 22.7 M parameters, 384 dimensions and CPU-friendly speed. This makes it a common starting point to test a semantic search or a RAG pipeline (documents, vectors, nearest neighbours) before choosing a larger model. Compared with the larger multilingual embedding models in the same vault catalogue (for example BGE-M3), it is English-focused, shorter in input length and much smaller *(our reading from the cards, not a benchmark)*.

## Behind the model

- **Organization:** the `sentence-transformers` namespace on Hugging Face. The card says the model was developed during a Hugging Face community week, with 7 TPUs v3-8 and support from Google's JAX, Flax and Cloud teams.
- **Authors:** no individual author names appear in the card text.
- **Base model:** `nreimers/MiniLM-L6-H384-uncased`, cited as the starting point in the card.

## Curiosities

- The training data is very large and very mixed: the card's table totals 1,170,060,424 training pairs. The largest sources are Reddit comments (2015–2018, about 726 million pairs), citation pairs from S2ORC (about 116 million), duplicate questions from WikiAnswers (about 77 million) and PAQ question–answer pairs (about 64 million).
- The model has no generative head: it cannot answer a question, only return a vector that can be compared with other vectors.

---

## Families

| Family | Value | Reason |
|--------|-------|--------|
| Group (architecture) | Encoder (embeddings) | Encoder-only transformer; it produces a vector per input, without generating tokens. |
| Category | Starter | Small model that is easy to run on a modest machine and to test a retrieval pipeline. |
| Tier (parameters) | NU (< 1 B) | 22.7 M parameters. |
| Type (modality) | Embeddings | Text input, vector output. |
| Evolutionary line | sentence-transformers line (MiniLM base → all-MiniLM-L6-v2) | The model is a fine-tune of `nreimers/MiniLM-L6-H384-uncased`. Other members of the line (for example `all-MiniLM-L12-v2`) are siblings, not evolutions; not checked in this article. |
| Ditto | Not assigned | It is not a general base for fine-tuning in its card; it is already trained for similarity. |

---

## Verification notes

| Data | Value | Source | Verified? |
|------|-------|--------|-----------|
| Parameters | 22.7 M (22,713,728) | HF API, `safetensors.parameters`; card "22.7M params" | Yes |
| License | Apache 2.0 | Model card YAML (`license: apache-2.0`) | Yes |
| Output dimension | 384 | Model card ("384 dimensional dense vector space") | Yes |
| Input truncation | 256 word pieces by default | Model card, "Intended uses" | Yes |
| Training sequence length | 128 tokens | Model card, training hyperparameters | Yes |
| Pooling and normalization | Mean pooling + L2 normalization | Model card example code | Yes |
| Number of layers | 6 (name "L6") | Model card does not state it; base name only | **No**, see Pending |
| Architecture | Encoder-only transformer, from `nreimers/MiniLM-L6-H384-uncased` | Model card | Yes |
| Libraries | sentence-transformers, transformers, ONNX, OpenVINO, Rust, TF, TEI | Model card and tags | Yes |
| Training data | 1,170,060,424 pairs; Reddit ≈ 726 M | Model card table | Yes |
| Training hardware | 7 TPUs v3-8 (community week) | Model card | Yes |
| Organization | `sentence-transformers` namespace; Hugging Face community week | Model card | Yes |
| Downloads / likes | 178,968,052 / 6,079 | HF API, 2026-11-08 | Yes (snapshot) |
| Downloads in vault | 180.2 M | Vault catalogue, snapshot 2026-11-05 | Yes (other snapshot) |
| Repository storage | 1,845,474,494 bytes | HF API, `usedStorage` | Yes |
| Size of `model.safetensors` in bytes | Not available | HF API gives no per-file sizes | **No**, see Pending |
| Gated access | No | HF API, `gated: false` | Yes |
| Hardware (FP32) | ≈ 0.15–0.2 GB | Calculation: 22.7 M × 4 B + margin | **Estimate** |
| Starter category | Series criterion (`CLAUDE.md`) | Own classification | Proposal |
| NU tier | < 1 B according to `CLAUDE.md` | Own classification | Yes |

## Pending

- **Number of layers:** the card does not state it. Check `config.json` in the repository (or the Files tab) before publishing "6 layers".
- **Size in bytes of `model.safetensors`:** the API gives no per-file sizes. Check the Files tab.
- **Measured hardware:** run the example on the reference machine and record the memory before changing the status to `tested`.
- **Who uses it:** the card names no projects. Any claim about specific users needs a source outside the card.
- **Quality comparison with larger embedding models:** the statement in "Why it matters" is our reading; it should be backed by a benchmark (for example MTEB) before it is stated as a fact.
- **Community-week details:** the card gives the event description only; no release date is stated.
