<!-- Resumen publicable. Artículo completo: posts/005-01-NU-S-llama-cpp.md. Mantener sincronizado. -->

Ejecutar un modelo de lenguaje en una Raspberry Pi 5 sin GPU, con un único programa en C++.

llama.cpp es un motor de inferencia de código abierto escrito en C/C++. No es un modelo: es el programa que carga un modelo en formato GGUF y genera texto, con una herramienta de línea de comandos y un servidor con API compatible con OpenAI. Publicado con licencia MIT.

🔧 **Tipo:** runtime de inferencia (no es un modelo). C/C++ con la librería `ggml`; funciona en CPU, con soporte opcional para GPU.
📏 **Tamaño:** el modelo de la prueba, Qwen3-1.7B en Q8_0, ocupa 1,70 GiB.
💻 **Hardware mínimo:** en nuestra prueba, una Raspberry Pi 5 con 8 GB de RAM ejecutó el modelo de 1,7 B en Q8_0 sin GPU. Nuestras medidas: unos 44 tokens/s para leer el prompt y unos 6 tokens/s para generar texto.
🛠️ **Interfaces:** `llama-cli` en la terminal, `llama-server` con API compatible con OpenAI (puerto por defecto 9931) y una librería en C.
🏢 **Detrás:** la organización `ggml-org` en GitHub.

Nuestras familias para este: Starter · tier NU (provisional, es un runtime, no un modelo) · Texto.

Repositorio: https://github.com/ggml-org/llama.cpp
