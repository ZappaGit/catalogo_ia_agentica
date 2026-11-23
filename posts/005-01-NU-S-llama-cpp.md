# 005 · llama.cpp

**Main source:** https://github.com/ggml-org/llama.cpp (README, `tools/server/README.md`, GitHub API)
**Model used in the test:** https://huggingface.co/Qwen/Qwen3-1.7B-GGUF (model card, Apache 2.0)
**License:** MIT (llama.cpp). The test model, Qwen3-1.7B-GGUF, is under Apache 2.0.
**Consulted:** 2026-11-08
**Code:** 01-NU-S-005 (catalogue 01 Text and LLMs · tier NU, *provisional: llama.cpp is a runtime, not a model, so it has no parameter tier* · Starter; see the "Families" section)
**Associated Pokémon:** — (not used for tools)

---

## LinkedIn text

Run a language model on a Raspberry Pi 5 with no GPU, using a single C++ program.

llama.cpp is an open-source inference engine, written in C/C++, that runs language models in GGUF format. It is not a model: it is the program that loads the weights and generates text, with a command-line tool and an HTTP server compatible with the OpenAI API.

🔧 **Type and technology:** inference runtime (not a model). C/C++ with the `ggml` library; it runs on CPU and optionally on GPU. It reads GGUF files, which store the weights already quantized.
📏 **Size:** the program is a few megabytes of binaries built from source. The test model, Qwen3-1.7B at Q8_0, is 1.70 GiB.
💻 **Minimum hardware:** a machine with a 64-bit CPU and enough RAM for the model file plus the context. On the Raspberry Pi 5 (8 GB) the 1.7B model at Q8_0 ran with about 7 GB available *(measured in our test, not a minimum)*.
🛠️ **Interfaces:** CLI (`llama-cli`), HTTP server (`llama-server`) with an OpenAI-compatible API, and a library API.
👥 **Who uses it and for what:** the README lists it as the base of many local tools and servers. We did not verify specific projects, so no names are given here.
💡 **Why it matters:** it lets you run a quantized model on modest hardware, without Python or CUDA, and with a standard API.
🏢 **Behind the project:** the `ggml-org` organization on GitHub. Repository created on 2023-03-10.
🤓 **Curiosity:** the latest release at the time of consulting was v0.9.0 (2026-11-04), and the repository had about 133,758 stars (GitHub API, snapshot 2026-11-08).

Repository: https://github.com/ggml-org/llama.cpp

#LLM #AI #OpenSource

---

## What it is

llama.cpp is a C/C++ project for inference (generating text with an already trained model). It is not a model and it does not include weights. It reads models in **GGUF** format, a file format that stores the tensors and the metadata needed to run them. Most GGUF files are quantized: they store the weights with fewer bits to use less memory.

It has two main programs:

- `llama-cli`: runs a model from the terminal, either in a single turn or as an interactive chat.
- `llama-server`: an HTTP server with an API compatible with OpenAI (chat completions, responses and embeddings routes, according to its README).

The `-hf user/repo[:quant]` option downloads the GGUF file from Hugging Face and caches it. If the quantization is not given, it uses `Q4_K_M` by default, or the first GGUF file in the repository if that one does not exist (`tools/server/README.md`).

## Type and technology

- **Type:** inference runtime. It is not a model; it runs models.
- **Language:** C++ (GitHub API). The core is the `ggml` library, linked from the project.
- **Formats:** GGUF, the format used by the project for quantized models.
- **Backends:** CPU by default; the build can use GPUs or other accelerators depending on the options chosen when compiling (see `docs/build.md`).
- **Dependencies:** the HTTP server uses `cpp-httplib` and `nlohmann/json`, both MIT (README).

## Size

- **Repository:** the README is the reference for installation. The latest release at consulting time was v0.9.0 (2026-11-04).
- **Our test build:** the `llama-cli` binary is about 1.2 MB and `llama-bench` about 73 KB, dynamically linked with `libllama`. The build was done from the `master` branch with `--depth 1`, at commit `7d7f028`, which reports version `0.9.0-dev (build 1)`.
- **Test model:** `Qwen3-1.7B-Q8_0.gguf`, 1.70 GiB, 1.72 B parameters (benchmark output).

## Minimum hardware

The memory needed is roughly the size of the GGUF file, plus the KV cache, which grows with the context length. The table shows the sizes for the quantizations of the test model; the sizes of the other quantizations are not verified.

| Configuration | Model memory | Reference |
|---------------|--------------|-----------|
| Qwen3-1.7B, Q8_0 (tested) | 1.70 GiB (benchmark) | Raspberry Pi 5, 8 GB RAM, CPU, 4 threads |
| Qwen3-1.7B, Q4_K_M (default in `-hf`) | not measured | — |

The Raspberry Pi 5 test used 4 threads. The memory reported before the test was 7.9 GiB total and about 6.5 GiB available. During generation, RAM usage was about 0.6 GiB used and 7.3 GiB available after the process ended.

## Interfaces

- **Terminal:** `llama-cli -hf <repo>:<quant> -p "prompt" -n <tokens>`. The `-st` (`--single-turn`) option runs one turn and exits. Our first attempt used `-no-cnv`, which this build does not accept.
- **HTTP server:** `llama-server -hf <repo>:<quant>`. The default port is 9931 (`--port`), and it exposes the OpenAI-compatible routes.
- **Library:** the C API of `libllama` (linked by the project's examples and external applications).
- **Installation:** the README offers an install script (`llama.app`), pre-built binaries on the releases page, Docker, and a build from source. The README badges also show a Winget package.

## Who uses it and for what

- The README says the server is used by external projects and tools; no specific projects are named here.
- We did not verify a list of users, so this article does not state any.

## Why it matters

In our test it ran a quantized Qwen3 model on the Raspberry Pi 5 with no GPU and no Python code: the program is a compiled binary that reads the GGUF file. We did not compare it with other tools, so this article makes no claim about memory or speed relative to them.

## Behind the project

- **Organization:** `ggml-org` on GitHub. The README links to the `ggml` project, which llama.cpp is built on.
- **Development:** the GitHub API shows the repository as active (last push on 2026-11-08 at the time of consulting).

## Curiosities

- The project was created on 2023-03-10 (GitHub API). The README now presents a `llama` command with subcommands `cli` and `serve` in addition to the binaries used in our test.
- In the Qwen3-1.7B-GGUF model card the recommended runtime settings include `--temp 0.6 --top-k 20 --top-p 0.95 --min-p 0 --presence-penalty 1.5` (model card). We did not use these settings in our test.

---

## Families

| Family | Value | Reason |
|--------|-------|--------|
| Group (architecture) | Not applicable: runtime, not a neural network | llama.cpp runs decoder-only transformers (LLMs). The group describes the model, not the program. |
| Category | Starter | Simple way to start running LLMs on local hardware. |
| Tier (parameters) | NU (< 1 B) — *provisional* | llama.cpp has no parameters. The NU code is assigned for the series' code scheme; see "Pending". |
| Type (modality) | Text (through the model it runs) | The test uses text. |
| Evolutionary line | ggml → llama.cpp | The project is built on the `ggml` library; the repository on GitHub is `ggml-org/llama.cpp`. |
| Ditto | Not applicable | It is not a model for fine-tuning. |

---

## How to run it

**Status: tested on the Raspberry Pi 5 (8 GB RAM, aarch64, 4 threads).** The build and the test model run on the Raspberry Pi. Not tested on the reference Windows machine (15.7 GB RAM, Intel UHD graphics, no CUDA). Commands are for the Raspberry Pi in Linux.

### a. Prerequisites

- Raspberry Pi 5 with 8 GB RAM, or a 64-bit Linux machine with enough free RAM for the model.
- Git, CMake, a C++ compiler and `libcurl4-openssl-dev` (installed for the test; the README does not state it is required for `-hf`).
- Internet access to download the model from Hugging Face.

### b. Build

```bash
sudo apt update && sudo apt install -y git cmake build-essential libcurl4-openssl-dev
git clone --depth 1 https://github.com/ggml-org/llama.cpp ~/llama.cpp
cd ~/llama.cpp
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j4 --target llama-cli llama-bench
```

The build took several minutes on the Raspberry Pi 5 with 4 threads (not timed exactly). The binaries are in `build/bin/`.

### c. Quick test

```bash
./build/bin/llama-cli -hf Qwen/Qwen3-1.7B-GGUF:Q8_0 \
  -st -p "Resume en tres frases: la junta aprueba cambiar el horario de la piscina." -n 300
```

Result: the model finished the reasoning block (`[Start thinking]`) and then started the answer, which was **truncated** at 300 tokens in the middle of a sentence. The limit was too low for thinking mode, so the output was cut. The run shows:

- Prompt processing: **38.6 tokens/s**.
- Generation: **5.7 tokens/s**.

### d. Benchmark

```bash
./build/bin/llama-bench -m <path-to-GGUF> -t 4 -p 512 -n 128 -r 3
```

The `-m` path is in the Hugging Face cache, not in `~/.cache/llama.cpp/` as the pasted script suggested. In this build the path is `~/.cache/huggingface/hub/models--Qwen--Qwen3-1.7B-GGUF/snapshots/<hash>/Qwen3-1.7B-Q8_0.gguf`.

| Test | Tokens | Speed |
|------|--------|-------|
| pp512 (prompt processing) | 512 | 43.77 ± 0.02 t/s |
| tg128 (generation) | 128 | 6.31 ± 0.02 t/s |

### e. Check and temperature

The Raspberry Pi temperature was measured with `vcgencmd measure_temp` at several points. The readings ranged from 48.8 °C (before the build) to 74.1 °C (during the build). After the benchmark it was 72.5 °C, and it was 59.3 °C once OpenClaw had been restarted and the machine was idle.

### f. Warnings

- **Download:** the Q8_0 GGUF is 1.70 GiB, cached in the Hugging Face cache.
- **License:** llama.cpp is MIT. The Qwen3-1.7B-GGUF model is Apache 2.0 according to its model card (`license: apache-2.0`).
- **Hardware:** the 1.7B model at Q8_0 generates at about 6 tokens per second on the Raspberry Pi 5 CPU. This is usable for tests but slow for long answers.
- **Sampling:** the test used the default settings. The model card recommends others (see Curiosities); a different setting may change the result and the length of the answer.

## Estimated use cases *(estimate: arithmetic from the benchmark, not measured end to end)*

The times use the measured rates: prompt processing 43.77 t/s and generation 6.31 t/s (`llama-bench`, 4 threads). Estimated time ≈ input tokens / 43.8 + output tokens / 6.3.

| Task | Approx. tokens in / out | Estimated time on the Pi |
|------|-------------------------|--------------------------|
| Classify an inbox message (short prompt, one-word answer) | ~80 / ~5 | 2–3 s |
| Summarize a 300-word document in 3 sentences | ~450 / ~80 | ~25 s |
| Answer a question with 3 RAG fragments as context | ~600 / ~100 | ~30 s |

Conclusions (estimates):

- Queued background jobs (classify, index, summarize) fit well on the Pi.
- Live chat is marginal: with streaming, the first word would appear after about 10–15 s with RAG context, since processing 600 prompt tokens alone takes about 14 s.
- Thinking mode should be off for these tasks. In our test it used most of the token budget. The option is `llama-cli --reasoning off` (checked in the `--help` of this build); `/no_think` has not been tested.

**Thermal check.** The maximum measured temperature was 74.1 °C. The official Raspberry Pi documentation describes throttling between 80 and 85 °C and full throttling at 85 °C; the 80 °C onset comes from user reports, not from the documentation. `vcgencmd get_throttled` returned `throttled=0x0` after the tests, so no throttling was recorded since the last boot.

**Comparison caveat.** The reference laptop ran Qwen3-0.6B with `transformers` in float32 at 4.2–5.7 tokens/s (`lab-llm/README.md`). That is a different model size, precision and tool from the Pi test, so the difference cannot be attributed to llama.cpp alone.

**Not tested yet:** Qwen3-4B in Q4_K_M (speed and quality), and the quality of the answers in Spanish for these three tasks.

## Verification notes

| Data | Value | Source | Verified? |
|------|-------|--------|-----------|
| License of llama.cpp | MIT | GitHub API (`ggml-org/llama.cpp`) and README badge | Yes |
| Language | C++ | GitHub API | Yes |
| Repository created | 2023-03-10 | GitHub API | Yes |
| Latest release at consulting | v0.9.0, 2026-11-04 | GitHub API (`releases/latest`) | Yes |
| Stars | 133,758 | GitHub API, snapshot 2026-11-08 | Yes |
| Default port of `llama-server` | 9931 | `tools/server/README.md` | Yes |
| Default quantization of `-hf` | Q4_K_M, or the first GGUF file | `tools/server/README.md` | Yes |
| OpenAI-compatible API | chat completions, responses, embeddings | `tools/server/README.md` | Yes |
| Test model license | Apache 2.0 | Model card `Qwen/Qwen3-1.7B-GGUF` | Yes |
| Test model file | `Qwen3-1.7B-Q8_0.gguf`, 1.70 GiB, 1.72 B | Benchmark output on the Raspberry Pi | Yes (measured) |
| Speed on the Pi (pp512 / tg128) | 43.77 / 6.31 t/s | `llama-bench`, 4 threads | Yes (measured) |
| Speed on the Pi, quick test | 38.6 / 5.7 t/s | `llama-cli` output | Yes (measured) |
| Pi temperature | 48.8 to 74.1 °C | `vcgencmd measure_temp` | Yes (measured) |
| Throttling thresholds | Limit at 85 °C; reduction between 80 and 85 °C | Raspberry Pi documentation (via search); the 80 °C onset comes from forum reports | Partly (documentation says 80–85 °C; onset on Pi 5 is from users) |
| Throttling after the tests | `throttled=0x0` | `vcgencmd get_throttled` on the Pi | Yes (measured) |
| `llama-cli` reasoning flag | `--reasoning off` | `llama-cli --help` of build 7d7f028 | Yes |
| Laptop 0.6B (transformers) | 4.2–5.7 t/s, float32 | `lab-llm/README.md` | Yes (measured on the reference machine) |
| Minimum hardware | — | — | **No verified** (only the tested case is reported) |
| Behind the project | `ggml-org` | GitHub | Yes (organization only) |
| Downloads of projects that use llama.cpp | — | — | **No verified** |

## Pending

- **Tier:** llama.cpp has no parameters, so the NU tier is a provisional code agreed for the series. It should be confirmed or changed before publication.
- **Quick test truncated:** the test with 300 tokens was cut during the answer, so the answer is not complete. A new run with more tokens (for example 1,024) would show the full answer.
- **Other quantizations and reference machine:** the test covers only Q8_0 on the Raspberry Pi 5. Q4_K_M and the reference Windows machine are not measured.
- **Installation note in `fundamentos-llm/04`:** the README now recommends an install script (`llama.app`) and mentions a `llama` command. The existing note in that file mentions the Winget badge and the `llama-server` command; it should be reviewed.
