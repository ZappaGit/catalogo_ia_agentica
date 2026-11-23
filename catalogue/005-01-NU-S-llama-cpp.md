<!-- Publishable summary. Full article (Spanish): posts/005-01-NU-S-llama-cpp.md. Keep in sync. -->

Run a language model on a Raspberry Pi 5 with no GPU, using a single C++ program.

llama.cpp is an open-source inference engine written in C/C++. It is not a model: it is the program that loads a model in GGUF format and generates text, with a command-line tool and a server with an OpenAI-compatible API. Released under the MIT license.

🔧 **Type:** inference runtime (not a model). C/C++ with the `ggml` library; runs on CPU, with optional GPU support.
📏 **Size:** the test model, Qwen3-1.7B in Q8_0, is 1.70 GiB.
💻 **Minimum hardware:** in our test, a Raspberry Pi 5 with 8 GB of RAM ran the 1.7B model at Q8_0 with no GPU. Our measurements: about 44 tokens/s to read the prompt and about 6 tokens/s to generate text.
🛠️ **Interfaces:** `llama-cli` in the terminal, `llama-server` with an OpenAI-compatible API (default port 9931), and a C library.
🏢 **Behind it:** the `ggml-org` organization on GitHub.

Our families for this one: Starter · NU tier (provisional, it is a runtime, not a model) · Text.

Repository: https://github.com/ggml-org/llama.cpp

#LLM #AI #OpenSource
