<!-- Publishable summary. Full article (Spanish): posts/001-04-NU-S-kokoro-82m.md. Keep in sync. -->

A text-to-speech model with 82 million parameters. Small enough for a laptop.

Kokoro is an open-weight TTS model released under Apache 2.0, so it can also be used in commercial products.

🔧 **Type:** text-to-speech. Architecture derived from StyleTTS 2, decoder-only (no diffusion), with ISTFTNet for waveform generation. Used from Python with the `kokoro` package.
📏 **Size:** 82M parameters. Version 1.0, released January 2025.
💻 **Minimum hardware:** a regular laptop CPU. The weights are about 330 MB in fp32 (our estimate, not stated in the model card).
🛠️ **Interfaces:** Python API, plus a Hugging Face demo and a Google Colab notebook.
👥 **Who uses it:** voice assistants, reading tools and prototypes. The model card says it has been deployed in numerous projects and commercial APIs.
🏢 **Behind it:** the architecture comes from StyleTTS 2 (Li et al.). The model was trained by an independent developer known as rzvzn; the model card reports about $1,000 of A100 GPU time.
🤓 **Curiosity:** "kokoro" means "heart" or "spirit" in Japanese.

Our Pokémon for this one: Jigglypuff, the one that sings to sleep.

Model card: https://huggingface.co/hexgrad/Kokoro-82M

#AI #TTS #OpenSource
