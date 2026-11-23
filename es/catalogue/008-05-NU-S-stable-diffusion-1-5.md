<!-- Resumen para publicar. Artículo completo (en español): posts/008-05-NU-S-stable-diffusion-1-5.md. Mantener sincronizado. -->

El modelo que popularizó la generación local de imágenes, ejecutado en un portátil sin tarjeta gráfica: una imagen tardó 7 minutos.

Stable Diffusion 1.5 es un modelo de texto a imagen de unos 0,9 mil millones de parámetros. Convierte una descripción escrita en una imagen, quitando ruido paso a paso en un espacio comprimido. Es de código abierto, con licencia CreativeML OpenRAIL-M, que tiene restricciones de uso.

🔧 **Tipo:** difusión latente (denoiser U-Net, codificador de texto CLIP, decodificador VAE). Ejecutado con stable-diffusion.cpp, un runtime en C/C++.
📏 **Tamaño:** unos 0,9 B de parámetros, archivo de pesos de 4,27 GB, salida de 512 × 512.
💻 **Hardware mínimo:** 2,78 GB de pesos en RAM, solo CPU, sin GPU (medido en un portátil de 15,7 GB).
🛠️ **Interfaces:** línea de comandos `sd-cli.exe`, servidor HTTP `sd-server`, Python con `diffusers` (no probado aquí).
🏢 **Detrás:** la cuenta `stable-diffusion-v1-5` de Hugging Face, espejo del repositorio `runwayml`, ya obsoleto. Tiene 1.019.121 descargas el último mes (a 2026-11-12).

Nuestras familias para este modelo: Starter · nivel NU · Difusión · línea Stable Diffusion 1.x.

Ficha del modelo: https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5

#ImageGeneration #AI #OpenSource
