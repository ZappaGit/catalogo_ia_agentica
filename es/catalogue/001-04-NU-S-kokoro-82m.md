<!-- Resumen para publicar. Artículo completo (español): posts/001-04-NU-S-kokoro-82m.md. Mantener sincronizado. -->

Un modelo de texto a voz con 82 millones de parámetros. Lo bastante pequeño para un portátil.

Kokoro es un modelo de texto a voz (TTS) de pesos abiertos, publicado bajo licencia Apache 2.0, así que también se puede usar en productos comerciales.

🔧 **Tipo:** texto a voz. Arquitectura derivada de StyleTTS 2, solo decodificador (sin difusión), con ISTFTNet para generar la forma de onda. Se usa desde Python con el paquete `kokoro`.
📏 **Tamaño:** 82 M de parámetros. Versión 1.0, publicada en enero de 2025.
💻 **Hardware mínimo:** CPU y RAM de un portátil normal. Los pesos ocupan unos 330 MB en fp32 (estimación nuestra, no la indica la ficha del modelo).
🛠️ **Interfaces:** API de Python, además de una demo en Hugging Face y un notebook de Google Colab.
👥 **Quién lo usa:** asistentes de voz, herramientas de lectura y prototipos. La ficha dice que se ha desplegado en numerosos proyectos y APIs comerciales.
🏢 **Detrás del modelo:** la arquitectura viene de StyleTTS 2 (Li et al.). El modelo lo entrenó el desarrollador independiente conocido como rzvzn; la ficha indica unos 1.000 dólares de tiempo en GPU A100.
🤓 **Curiosidad:** "kokoro" significa "corazón" o "espíritu" en japonés.

Nuestro Pokémon para este: Jigglypuff, el que canta para dormir.

Ficha del modelo: https://huggingface.co/hexgrad/Kokoro-82M
