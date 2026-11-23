<!-- Publishable summary. Full article: posts/011-04-NU-P-whisper-large-v3-turbo.md. Keep in sync. -->

Drop in a voice note and get the text back, on a laptop with no graphics card.

Whisper large-v3-turbo is OpenAI's open speech recognition model (audio to text). It transcribes audio in many languages, can translate it into English, and gives timestamps for each sentence. It has an MIT license, so it can also be used in commercial products.

🔧 **Type:** speech recognition. A Transformer encoder-decoder: Whisper large-v3 with the decoder cut from 32 layers to 4 and fine-tuned. The card says it is "way faster, at the expense of a minor quality degradation".
📏 **Size:** 809 M parameters, 1.6 GB of weights in FP16. It listens in 30-second windows; the card lists 99 languages, with strong results in about 10.
💻 **Minimum hardware:** we tested it on a 16 GB laptop with no GPU: it used **3.9 GB of RAM**, and a 75 s audio took 82 s to transcribe, about real time.
🛠️ **Interfaces:** Python with Hugging Face `transformers`: one `pipeline` call with the path to the audio. There are Whisper conversions for CTranslate2 (faster-whisper) and CoreML (Apple).
🏢 **Behind the model:** OpenAI, based on the paper by Alec Radford and others (2022). Its 4.8 million downloads in the last month (as of 2026-11-14) put it among the most used speech models on the Hub.
🤓 **Watch out:** the card itself warns that it can hallucinate, writing text that was never said in the audio. And in our test, when one recording mixed Spanish and English, it left out the sentences in one of the two languages.

Our families for this one: Paradox · NU tier · Audio to text · Transformer encoder-decoder.

Model card: https://huggingface.co/openai/whisper-large-v3-turbo
