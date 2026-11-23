<!-- Resumen para publicar. Artículo completo (en español): posts/009-05-UU-P-z-image-turbo-q4.md. Mantener sincronizado. -->

El mismo modelo de imagen de 6.000 millones de parámetros del artículo 007, cuantizado a 4 bits, ahora dibuja en un portátil sin tarjeta gráfica: 8 minutos por imagen.

Es la versión cuantizada de Z-Image-Turbo. El modelo de difusión se comprime de 16 bits a unos 4 bits por peso, así que cabe en los 16 GB de RAM del portátil. Se ejecuta con stable-diffusion.cpp, un programa en C/C++, bajo licencia Apache 2.0.

🔧 **Tipo:** transformer de difusión para texto a imagen, cuantizado en GGUF Q4_K, con codificador de texto Qwen3-4B. Ejecutado en CPU con stable-diffusion.cpp.
📏 **Tamaño:** modelo de difusión de 3,86 GB, codificador de texto de 2,50 GB, VAE de 0,34 GB. Salida de 512 × 512.
💻 **Hardware mínimo:** **unos 6,2 GB de RAM** para los pesos, medidos en CPU sin GPU.
🛠️ **Interfaces:** línea de comandos `sd-cli.exe` y servidor HTTP `sd-server` de stable-diffusion.cpp.
🏢 **Detrás:** Tongyi-MAI (grupo Alibaba) hizo el modelo base; la cuantización GGUF es de `leejet`, autor de stable-diffusion.cpp. El repositorio cuantizado tiene 265.885 descargas el último mes (a 2026-11-12).

Nuestras familias para este modelo: Paradox · nivel UU · Imagen · Transformer de difusión.

Ficha del modelo: https://huggingface.co/leejet/Z-Image-Turbo-GGUF

#ImageGeneration #AI #OpenSource
