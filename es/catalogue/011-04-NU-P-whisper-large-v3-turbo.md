<!-- Resumen para publicar. Artículo completo (español): posts/011-04-NU-P-whisper-large-v3-turbo.md. Mantener sincronizado. -->

Le pasas una nota de voz y te devuelve el texto, en un portátil sin tarjeta gráfica.

Whisper large-v3-turbo es el modelo abierto de reconocimiento de voz (audio a texto) de OpenAI. Transcribe audio en muchos idiomas, puede traducirlo al inglés y da marcas de tiempo por frase. Tiene licencia MIT, así que también se puede usar en productos comerciales.

🔧 **Tipo:** reconocimiento de voz. Transformer codificador-decodificador: es Whisper large-v3 con el decodificador recortado de 32 capas a 4 y reentrenado. La ficha dice que es "way faster, at the expense of a minor quality degradation".
📏 **Tamaño:** 809 M de parámetros, pesos de 1,6 GB en FP16. Escucha el audio en ventanas de 30 segundos; la ficha enumera 99 idiomas, con buenos resultados en unos 10.
💻 **Hardware mínimo:** lo probamos en un portátil de 16 GB de RAM sin GPU: usó **3,9 GB de RAM** y un audio de 75 s tardó 82 s en transcribirse, más o menos a tiempo real.
🛠️ **Interfaces:** Python con `transformers` de Hugging Face: una llamada a `pipeline` con la ruta del audio. Hay conversiones de Whisper para CTranslate2 (faster-whisper) y CoreML (Apple).
🏢 **Detrás del modelo:** OpenAI, a partir del paper de Alec Radford y otros (2022). Sus 4,8 millones de descargas en el último mes (a 2026-11-14) lo sitúan entre los modelos de voz más usados del Hub.
🤓 **Ojo:** la propia ficha avisa de que puede alucinar, es decir, escribir texto que nunca se dijo en el audio. Y en nuestra prueba, cuando una grabación mezcló español e inglés, se saltó las frases de uno de los dos idiomas.

Nuestras familias para este: Paradox · tier NU · Audio a texto · Transformer codificador-decodificador.

Ficha del modelo: https://huggingface.co/openai/whisper-large-v3-turbo
