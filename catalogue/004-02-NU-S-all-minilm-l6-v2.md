<!-- Publishable summary. Full article (Spanish): posts/004-02-NU-S-all-minilm-l6-v2.md. Keep in sync. -->

The most downloaded model in our Hugging Face snapshot. It does not write or speak: it turns a sentence into 384 numbers.

all-MiniLM-L6-v2 is an embedding model with 22.7 million parameters. It maps a sentence or a short paragraph to a vector, so that texts with similar meaning end up close to each other. It is open-source, under the Apache 2.0 license.

🔧 **Type:** sentence embeddings. Encoder-only transformer with mean pooling. Used from Python with `sentence-transformers`.
📏 **Size:** 22.7M parameters, 384-dimensional vectors, input truncated at 256 word pieces.
💻 **Minimum hardware:** any CPU with about 0.2 GB of RAM *(our estimate, not stated in the model card)*.
🛠️ **Interfaces:** Python (`sentence-transformers`, `transformers`), ONNX, OpenVINO and Rust exports.
🏢 **Behind it:** the `sentence-transformers` namespace on Hugging Face, developed during a Hugging Face community week. Its 179 million downloads (as of 2026-11-08) make it one of the most used models on the Hub.

Our families for this one: Starter · NU tier · Embeddings · Encoder.

Model card: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
