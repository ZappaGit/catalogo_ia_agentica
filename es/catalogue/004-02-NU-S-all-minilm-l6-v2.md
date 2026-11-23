<!-- Resumen para publicar. Artículo completo (español): posts/004-02-NU-S-all-minilm-l6-v2.md. Mantener sincronizado. -->

El modelo más descargado de nuestro snapshot de Hugging Face. No escribe ni habla: convierte una frase en 384 números.

all-MiniLM-L6-v2 es un modelo de embeddings con 22,7 millones de parámetros. Asigna a una frase o a un párrafo corto un vector, de forma que los textos de significado parecido quedan cerca unos de otros. Es de código abierto, con licencia Apache 2.0.

🔧 **Tipo:** embeddings de frases. Transformer solo codificador con mean pooling. Se usa desde Python con `sentence-transformers`.
📏 **Tamaño:** 22,7M de parámetros, vectores de 384 dimensiones, entrada truncada a 256 piezas de palabra.
💻 **Hardware mínimo:** cualquier CPU con unos 0,2 GB de RAM *(estimación nuestra; la ficha del modelo no lo indica)*.
🛠️ **Interfaces:** Python (`sentence-transformers`, `transformers`), exportaciones a ONNX, OpenVINO y Rust.
🏢 **Detrás:** el espacio `sentence-transformers` en Hugging Face, desarrollado durante una semana comunitaria de Hugging Face. Sus 179 millones de descargas (a 2026-11-08) lo sitúan entre los modelos más usados del Hub.

Nuestras familias para este: Starter · tier NU · Embeddings · Encoder.

Ficha del modelo: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
