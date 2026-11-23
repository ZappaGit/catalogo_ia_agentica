<!-- Resumen para publicar. Artículo completo (en español): posts/007-05-UU-P-z-image-turbo.md. Mantener sincronizado. -->

Un modelo de imagen de 6.000 millones de parámetros que dibuja en 8 pasos, cuando su versión base necesita 50.

Z-Image-Turbo es un modelo de texto a imagen del equipo Tongyi-MAI de Alibaba. Es una versión destilada de Z-Image: el mismo modelo, entrenado para llegar al resultado con muchos menos pasos. Es de código abierto, con licencia Apache 2.0.

🔧 **Tipo:** transformer de difusión para texto a imagen, destilado a 8 pasos. Se usa desde Python con Hugging Face Diffusers.
📏 **Tamaño:** 6,15 B de parámetros, prompts bilingües (inglés y chino), pesos en safetensors.
💻 **Hardware mínimo:** unos **16 GB de VRAM** en una GPU de consumo, según indica la tarjeta del modelo (nuestra estimación de solo los pesos: unos 12,3 GB en BF16).
🛠️ **Interfaces:** Python con `ZImagePipeline` de Diffusers, aplicaciones de escritorio como Draw Things y DiffusionBee, e inferencia alojada a través de fal.
🏢 **Detrás:** la organización Tongyi-MAI del grupo Alibaba. Sus 723.000 descargas (a 2026-11-10) muestran un alcance amplio.

Nuestras familias para este modelo: Paradox · nivel UU · Imagen · Transformer de difusión.

Tarjeta del modelo: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
