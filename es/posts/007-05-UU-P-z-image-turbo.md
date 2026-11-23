# 007 · Z-Image-Turbo

**Fuente principal:** https://huggingface.co/Tongyi-MAI/Z-Image-Turbo
**Artículo científico:** https://arxiv.org/abs/2511.22699 (Z-Image Team, v1 27 nov 2025)
**Licencia:** Apache 2.0
**Consultado:** 2026-11-10
**Código:** 05-UU-P-007 (catálogo 05 Imagen, vídeo y 3D · UU · Paradox)
**Origen:** cola de candidatos de `indice.md`, tomado del catálogo del vault `IA_Agentica/HuggingFace` (entrada "Z-Image-Turbo / Qwen-Image 2.1 (imagen)"). Elegido como primer candidato de la cola; es el primer modelo de imagen de la serie.
**Familias:** Paradox · UU · Transformer de difusión (DiT) · variante destilada de Z-Image (ver la sección "Familias")

---

## Resumen

Un modelo de imagen de 6.000 millones de parámetros que dibuja en 8 pasos, cuando su versión base necesita 50.

Z-Image-Turbo es un modelo de texto a imagen del equipo Tongyi-MAI de Alibaba. Es una versión destilada de Z-Image: el mismo modelo, entrenado para llegar al resultado con muchos menos pasos. Es de código abierto, con licencia Apache 2.0.

🔧 **Tipo y tecnología:** transformer de difusión para texto a imagen, con un diseño de flujo único llamado S3-DiT, un codificador de texto Qwen3-4B y un VAE Flux (resumen del artículo, ver Pendiente). Destilado a 8 pasos. Python, con Hugging Face Diffusers.
📏 **Tamaño:** 6,15 B de parámetros, prompts bilingües (inglés y chino), 1024 × 1024 en el ejemplo de la tarjeta. Se distribuye en safetensors.
💻 **Hardware mínimo:** unos **16 GB de VRAM** en una GPU de consumo, según indica la tarjeta (en BF16). El transformer solo ocupa unos 12,3 GB en BF16 *(estimación: 6,15 B × 2 bytes; la cifra de 16 GB es de la tarjeta)*. Una versión cuantizada Q4 funciona en CPU en el portátil de referencia, con unos 6,2 GB de pesos en RAM; ver el artículo 009.
🛠️ **Interfaces:** Python con `ZImagePipeline` de `diffusers`, instalado desde la última versión. Aplicaciones como Draw Things y DiffusionBee, e inferencia alojada a través de fal. La tarjeta no menciona ComfyUI.
👥 **Quién lo usa y para qué:** la tarjeta no nombra empresas ni proyectos. Tiene 723.026 descargas y 5.583 me gusta (a 2026-11-10), y las demos de Hugging Face y ModelScope permiten probarlo a cualquiera.
💡 **Por qué importa:** 8 pasos en lugar de 50 significa una imagen en pocos segundos en una sola GPU de consumo, lo que hace práctica la generación local de imágenes para particulares. La tarjeta dice que 16 GB de VRAM bastan; no lo hemos medido *(nuestra lectura de la tarjeta)*.
🏢 **Detrás del modelo:** la organización Tongyi-MAI, del grupo Alibaba. El artículo lo firma el "Z-Image Team" con 23 coautores nombrados.
🤓 **Curiosidad:** el modelo se destiló de un modelo base de 50 pasos con guidance, y la versión Turbo funciona con escala de guidance 0. Las "8 NFE" (evaluaciones de la red) de la tarjeta corresponden a 9 pasos en el código, que hacen 8 pasadas del transformer.

Tarjeta del modelo: https://huggingface.co/Tongyi-MAI/Z-Image-Turbo

---

## Qué es

Z-Image-Turbo es un **modelo de texto a imagen**. Recibe una descripción escrita y devuelve una imagen. En esta versión no edita imágenes existentes. Su tarjeta lo describe como "un modelo base eficiente para generar imágenes con un transformer de difusión de flujo único", y es la versión destilada y rápida del modelo Z-Image.

La generación de imágenes por difusión parte de ruido aleatorio y lo quita paso a paso, guiada por el texto. Un modelo que necesita menos pasos es más rápido, pero hay que mantener la calidad; para eso sirve la destilación (ver el glosario).

## Tipo y tecnología

- **Tarea:** generación de imágenes a partir de texto (`pipeline_tag` en la API: text-to-image).
- **Arquitectura:** transformer de difusión (DiT). La tarjeta lo llama "Scalable Single-Stream Diffusion Transformer (S3-DiT)": los tokens de texto y de imagen pasan por el mismo flujo del transformer. `transformer/config.json` da 30 capas, tamaño oculto 3840 y 30 cabezas de atención. El resumen del artículo decía 32 cabezas; el config lo contradice, así que se usa el config. El tamaño de la FFN (10240, del resumen del artículo) no está en el config y queda pendiente.
- **Codificador de texto:** `text_encoder/config.json` describe un modelo Qwen3 con 36 capas y tamaño oculto 2560. Sus tres archivos safetensors suman unos 8 GB en BF16, lo que corresponde a un modelo de unos 4 B de parámetros. La tarjeta no lo nombra; el nombre Qwen3-4B viene del resumen del artículo.
- **VAE:** `vae/config.json` es un `AutoencoderKL` con 16 canales latentes, cuatro bloques de reducción (compresión espacial 8x) y `_name_or_path: flux-dev`, así que es un VAE de estilo Flux.
- **Destilación:** la tarjeta dice que Turbo es "una versión destilada de Z-Image" que necesita "solo 8 NFE". La tabla de modelos de la tarjeta da 50 pasos con CFG para el Z-Image base y 8 pasos sin CFG para Turbo. Los métodos (Decoupled-DMD y DMDR) aparecen en el resumen del artículo, no en la tarjeta *(pendiente)*.
- **Lenguaje de implementación:** Python, con la biblioteca `diffusers` de Hugging Face (clase `ZImagePipeline`).

## Tamaño

- **Parámetros:** 6 B según la tarjeta; 6.154.908.736 según la API (metadatos de safetensors, tensores F32). La tabla del artículo también da 6,15 B.
- **Contexto:** no aplica; la entrada es un texto.
- **Resolución:** el ejemplo de la tarjeta usa 1024 × 1024. No se encontró el rango admitido.
- **Formato:** solo safetensors. No hay archivo GGUF en el repositorio (la página enlaza 106 cuantizaciones de terceros, que no se han revisado aquí).
- **Almacenamiento del repositorio:** 53.980.522.390 bytes según la API (unos 54 GB). La API no da tamaños por archivo.

## Hardware mínimo

| Configuración | Memoria | Cálculo | Recomendado |
|---------------|---------|---------|-------------|
| Solo pesos en BF16, transformer | ≈ 12,3 GB | 6,15 B × 2 bytes | — |
| Pesos en BF16, transformer + codificador de texto | ≈ 20,4 GB | 6,15 B × 2 + ≈ 4 B × 2 bytes | — |
| Según la tarjeta | 16 GB de VRAM | Tarjeta: "cabe cómodamente en 16G de VRAM en dispositivos de consumo" | GPU NVIDIA de consumo |
| Pesos en FP32 (safetensors tal como se publican) | ≈ 24,6 GB | 6,15 B × 4 bytes | No cabe en 16 GB |

La cifra de 16 GB es la afirmación de la tarjeta. Nuestra estimación de 12,3 GB cubre solo los pesos; el codificador de texto, el VAE y las activaciones añaden memoria, por eso la cifra de la tarjeta es mayor. Ninguno de estos valores se ha medido en el equipo de referencia.

El artículo también informa de generación en menos de un segundo en GPU H800. Su nota al pie dice que para esa velocidad hacen falta FlashAttention-3 y `torch.compile`. Es un resultado de centro de datos, no una cifra de portátil.

**Equipo de referencia:** 15,7 GB de RAM, gráficos Intel integrados, sin CUDA. El modelo en BF16 no cabe ahí. La versión GGUF Q4 sí funciona (artículo 009).

## Interfaces

- **Python con Diffusers:** `from diffusers import ZImagePipeline`. La tarjeta indica instalar `diffusers` desde el código fuente; también dice que dos pull requests (#12703 y #12715) están incluidas en la última versión oficial. No se encontró el número de versión mínima.
- **Guidance:** la tarjeta indica `guidance_scale=0.0` para los modelos Turbo, y el ejemplo usa `num_inference_steps=9`.
- **Aplicaciones de escritorio:** Draw Things y DiffusionBee aparecen en la tarjeta o en sus etiquetas.
- **Inferencia alojada:** un proveedor de inferencia de fal, y demos públicas en Hugging Face y ModelScope.
- **ComfyUI:** no aparece en la tarjeta.

## Quién lo usa y para qué

- La tarjeta no nombra empresas, productos ni proyectos de investigación que usen el modelo.
- Popularidad (a 2026-11-10): 723.026 descargas y 5.583 me gusta en Hugging Face (API). Las descargas son acumuladas, así que miden alcance, no calidad.
- La tarjeta cita las demos de Hugging Face y ModelScope y la Alibaba AI Arena como sitios donde probar el modelo.

## Por qué importa

Es uno de los pocos modelos de texto a imagen de este tamaño con licencia permisiva y diseñado para funcionar en pocos pasos en una sola GPU de consumo. Frente a un modelo base de 50 pasos, el tiempo por imagen baja unas seis veces *(nuestra lectura de los pasos de la tarjeta, no un benchmark)*. No se ha comprobado aquí la calidad de imagen frente a modelos más grandes.

## Detrás del modelo

- **Organización:** Tongyi-MAI, del grupo Alibaba.
- **Autores:** el artículo está firmado por el "Z-Image Team" con 23 coautores nombrados. La tarjeta del modelo no nombra a los autores individualmente.
- **Fechas:** el repositorio se creó el 2025-11-25 y se modificó por última vez el 2026-01-30 (API). La primera versión del artículo (arXiv v1) es del 27 de noviembre de 2025.
- **Modelos relacionados:** la tabla de modelos de la tarjeta lista Z-Image-Omni-Base y Z-Image-Edit como "por publicar". No están disponibles a la fecha de consulta.

## Curiosidades

- El modelo Turbo funciona sin guidance sin clasificador: la escala de guidance es 0. El modelo base necesita guidance, así que la versión destilada elimina esa segunda pasada y ahorra más tiempo.
- Las "8 NFE" de la tarjeta no son lo mismo que los pasos del código (9, que según la tarjeta "en realidad da 8 pasadas del DiT"). La tarjeta no explica la diferencia con detalle; reportamos ambas cifras tal como aparecen.

---

## Familias

| Familia | Valor | Motivo |
|---------|-------|--------|
| Grupo (arquitectura) | Difusión (transformer de difusión, DiT) | Genera la imagen quitando ruido en pasos, con un transformer como denoiser. |
| Categoría | Paradox | Variante destilada de un modelo conocido (Z-Image). La carta de prueba de `carta/pruebas/` tenía "Starter"; aquí se cambia, siguiendo la regla de `CLAUDE.md`. |
| Nivel (parámetros) | UU (4–14 B) | 6,15 B de parámetros. |
| Tipo (modalidad) | Imagen | Entrada de texto, salida de imagen. |
| Línea evolutiva | Z-Image → Z-Image-Turbo | Turbo es la versión destilada del Z-Image base. Z-Image-Omni-Base y Z-Image-Edit se anuncian como hermanos, no publicados. |
| Ditto | No asignado | La tarjeta lo presenta como un modelo terminado para generar imágenes. |

---

## Cómo ejecutarlo

**Estado: no ejecutado.** El lab está en `lab-img/` (no versionado, igual que `lab-llm/` y `lab-tts/`). El script está escrito y compila, pero no se ha cargado el modelo: el equipo de referencia no tiene CUDA y no puede mantener los pesos en RAM (ver "Registro del lab" más abajo).

### a. Requisitos previos
- GPU NVIDIA con unos 16 GB de VRAM o más (afirmación de la tarjeta; no verificada en hardware).
- Windows 11 con Python 3.12 (el equipo de referencia tiene Python 3.12.10).
- Unos 54 GB libres en disco para la caché de Hugging Face.

### b. Entorno virtual
En `lab-img/`: `python -m venv .venv`, y después actualizar pip, como se describe en `lab-img/README.md`.

### c. Instalación
- PyTorch con CUDA. La versión CPU no sirve para esta prueba.
- `diffusers` desde el código fuente de GitHub (instrucción de la tarjeta), con `transformers` y `accelerate`. La versión mínima no está confirmada (ver Pendiente).

### d. Ejemplo mínimo
`lab-img/test_z_image_turbo.py`, con estos valores por defecto: prompt `a red circle on a white background`, 512 × 512, 9 pasos, guidance 0.0, semilla 42, BF16. Guarda `lab-img/out/z_image_turbo_prueba.png`. Si no hay CUDA, muestra un mensaje y termina antes de cargar nada. Ejecutarlo desde `lab-img/` con el entorno virtual del lab: `.\.venv\Scripts\python.exe test_z_image_turbo.py`.

### e. Comprobación
Resultado esperado: un PNG de 512 × 512 con un círculo rojo sobre fondo blanco. Todavía no comprobado.

### f. Avisos
- **Descarga:** unos 54 GB en la caché de Hugging Face (`%USERPROFILE%\.cache\huggingface`).
- **Hardware del equipo de referencia:** no cabe. Pesos en BF16: DiT ≈ 12,3 GB (6,15 B × 2 bytes) y codificador de texto Qwen3-4B ≈ 8 GB (de `text_encoder/config.json` y los tamaños de archivo), es decir, más de 20 GB frente a 15,7 GB de RAM. Forzar la ejecución en CPU (`FORZAR_CPU = True`) haría que los pesos se leyeran desde disco: muy lento, y puede bloquear el sistema. No se recomienda.
- **Seguridad:** los pesos están en safetensors, que no ejecuta código al cargarse. El script no usa `trust_remote_code`. El código que sí se ejecuta es la biblioteca `diffusers`, instalada desde GitHub.
- **Licencia:** Apache 2.0, sin restricción de acceso.
- **Argumentos de Diffusers:** `torch_dtype` y `guidance_scale` siguen el ejemplo de la tarjeta; no se han comprobado contra la versión instalada.

### Registro del lab

| Fecha | Equipo | Resultado |
|-------|--------|-----------|
| 2026-11-12 | Equipo de referencia (sin CUDA, 15,7 GB de RAM) | No ejecutado: los pesos no caben en memoria. El script se detiene antes de cargar. |

## Ilustración de la carta

La carta de este modelo usa el dibujo más sencillo del subtipo imagen: un sol sobre una línea de horizonte, en lugar del paisaje de la categoría 05 con montañas. Es una decisión para la carta de la serie, no una propiedad del modelo.

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Parámetros | 6 B (tarjeta); 6.154.908.736 (API) | Tarjeta del modelo; API de HF `safetensors` | Sí |
| Licencia | Apache 2.0 | Metadatos de la tarjeta y etiquetas de la API | Sí |
| Nombre oficial y organización | Z-Image-Turbo, Tongyi-MAI (grupo Alibaba) | Tarjeta del modelo; artículo | Sí |
| Arquitectura (S3-DiT) | Transformer de difusión de flujo único | Tarjeta del modelo | Sí |
| Capas, tamaño oculto, cabezas | 30, 3840, 30 | `transformer/config.json` | Sí |
| Tamaño de la FFN | 10240 | Solo resumen del artículo | **No**, ver Pendiente |
| Codificador de texto (Qwen3, 36 capas, oculto 2560, ≈ 4 B) | 3 archivos safetensors, ≈ 8 GB BF16 | `text_encoder/config.json`, árbol del repositorio | Sí (nombre Qwen3-4B: resumen del artículo) |
| VAE (AutoencoderKL, 16 canales latentes, flux-dev) | Config | `vae/config.json` | Sí |
| Destilado de Z-Image, 8 NFE | Indicado | Tarjeta del modelo | Sí |
| 9 pasos en el código | Indicado | Ejemplo de la tarjeta | Sí |
| Modelo base: 50 pasos con CFG | Indicado | Tabla de modelos de la tarjeta | Sí |
| Escala de guidance 0 | Indicado | Tarjeta del modelo | Sí |
| Interfaces: `ZImagePipeline` de Diffusers | Indicado | Tarjeta del modelo | Sí |
| Versión mínima de Diffusers | No encontrada | — | **No**, ver Pendiente |
| Idiomas: inglés y chino | Indicado | Tarjeta del modelo | Sí |
| Hardware: 16 GB de VRAM | Indicado | Tarjeta del modelo ("cabe cómodamente en 16G de VRAM") | Sí (como afirmación de la tarjeta) |
| Hardware: pesos BF16 ≈ 12,3 GB | Cálculo: 6,15 B × 2 bytes | Cálculo propio | **Estimación** |
| Menos de un segundo en H800 | Indicado | Artículo | Sí (cifra de centro de datos) |
| Almacenamiento del repositorio | 53.980.522.390 bytes | API de HF `usedStorage` | Sí (instantánea) |
| Descargas / me gusta | 723.026 / 5.583 | API de HF, 2026-11-10 | Sí (instantánea) |
| Creación / última modificación | 2025-11-25 / 2026-01-30 | API de HF | Sí |
| Fecha del artículo (v1) | 27 nov 2025 | arXiv | Sí |
| Acceso restringido | No | API de HF `gated: false` | Sí |
| Categoría Paradox | Criterio de la serie (`CLAUDE.md`) | Clasificación propia | Propuesta |
| Nivel UU | 4–14 B según `CLAUDE.md` | Clasificación propia | Sí |

## Pendiente

- **Tamaño de la FFN y nombres de destilación:** el tamaño de la FFN (10240) y los nombres Decoupled-DMD y DMDR vienen del resumen del artículo, no del repositorio. Verificarlos en el artículo (sección 4.1 y las de destilación) antes de afirmarlos como hechos.
- **Métodos de destilación:** los nombres Decoupled-DMD y DMDR están en el resumen del artículo. Verificarlos en el artículo antes de afirmarlos como hechos.
- **Versión mínima de Diffusers:** la tarjeta da números de PR, no una versión. El repositorio se guardó con `diffusers` 0.36.0.dev0 (`model_index.json`), así que la versión necesaria es esa o posterior; revisar las notas de versión.
- **Soporte de ComfyUI:** no aparece en la tarjeta de Tongyi. Los archivos reempaquetados de Comfy-Org (`Comfy-Org/z_image_turbo`, Apache 2.0) se describen como "Repackaged model files for ComfyUI", así que el uso con ComfyUI está documentado allí.
- **Resoluciones admitidas:** la tarjeta solo da 1024 × 1024 como ejemplo.
- **Codificador de texto y VAE en los 6 B:** resuelto. Los tres archivos safetensors del transformer suman 24,6 GB, es decir, 6,15 B de parámetros a 4 bytes cada uno, así que la cifra de 6,15 B corresponde solo al transformer. El codificador de texto (unos 4 B) y el VAE van aparte.
- **Hardware medido:** el modelo en BF16 no se ha ejecutado en el equipo de referencia (no tiene CUDA). La versión GGUF Q4 sí se ha ejecutado allí; sus tiempos están en el artículo 009. Las cifras de BF16 son afirmación de la tarjeta y nuestra estimación.
- **Usuarios y proyectos:** la tarjeta no nombra ninguno. Cualquier afirmación sobre usuarios concretos necesita una fuente externa.
- **Fecha de publicación:** la tarjeta no la indica. Solo se conocen las fechas del repositorio y del artículo indicadas arriba.
