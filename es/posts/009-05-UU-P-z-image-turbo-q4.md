# 009 · Z-Image-Turbo Q4 (GGUF, stable-diffusion.cpp)

**Fuente principal (modelo cuantizado):** https://huggingface.co/leejet/Z-Image-Turbo-GGUF
**Modelo base:** https://huggingface.co/Tongyi-MAI/Z-Image-Turbo (ver el artículo 007)
**Codificador de texto:** https://huggingface.co/unsloth/Qwen3-4B-Instruct-2507-GGUF (Q4_K_M)
**VAE:** `ae.safetensors` de https://huggingface.co/Comfy-Org/z_image_turbo (ver Pendiente)
**Runtime:** stable-diffusion.cpp, release `master-1091-b9d7176`, https://github.com/leejet/stable-diffusion.cpp (MIT)
**Licencia:** Apache 2.0 (modelo base, archivos cuantizados y codificador de texto; el repositorio del VAE también es Apache 2.0)
**Consultado:** 2026-11-12
**Código:** 05-UU-P-009 (catálogo 05 Imagen, vídeo y 3D · UU · Paradox: variante cuantizada de un modelo conocido)
**Origen:** continuación del artículo 007 (Z-Image-Turbo). Elegido para comprobar si el modelo de 6 B funciona en este portátil una vez cuantizado.
**Familias:** Paradox · UU · Transformer de difusión (DiT) · versión cuantizada (GGUF Q4_K) de Z-Image-Turbo (ver la sección "Familias")

---

## Texto para LinkedIn

El mismo modelo de imagen de 6.000 millones de parámetros del artículo 007, cuantizado a 4 bits, ahora dibuja en un portátil sin tarjeta gráfica: 8 minutos por imagen.

Es la versión cuantizada de Z-Image-Turbo. El modelo de difusión se comprime de 16 bits a unos 4 bits por peso, así que cabe en los 16 GB de RAM del portátil. Se ejecuta con stable-diffusion.cpp, un programa en C/C++, bajo licencia Apache 2.0.

🔧 **Tipo y tecnología:** transformer de difusión para texto a imagen, cuantizado en GGUF Q4_K, con un codificador de texto Qwen3-4B (Q4_K_M) y el VAE de estilo FLUX. Ejecutado en CPU con el runtime en C/C++ stable-diffusion.cpp.
📏 **Tamaño:** modelo de difusión de 3,86 GB (Q4_K), codificador de texto de 2,50 GB, VAE de 0,34 GB. Salida de 512 × 512 píxeles.
💻 **Hardware mínimo:** **unos 6,2 GB de RAM** para los pesos, medidos en CPU sin GPU. Nuestro equipo de pruebas tiene 15,7 GB de RAM y no tiene CUDA.
🛠️ **Interfaces:** la línea de comandos `sd-cli.exe` de stable-diffusion.cpp, y su servidor HTTP `sd-server`. ComfyUI: no probado aquí.
👥 **Quién lo usa y para qué:** el repositorio cuantizado tiene 265.885 descargas el último mes (a 2026-11-12); la ficha no nombra empresas ni proyectos.
💡 **Por qué importa:** es el primer modelo de imagen de 6.000 millones de parámetros de la serie que funciona en este portátil. El coste es el tiempo: una imagen de 8 pasos tardó 480 s. El modelo base, que necesita GPU, es más rápido *(medición propia; el modelo base no se ejecutó aquí)*.
🏢 **Detrás del modelo:** Tongyi-MAI (grupo Alibaba) hizo el modelo base. La cuantización GGUF es de `leejet`, autor de stable-diffusion.cpp.
🤓 **Curiosidad:** la imagen de esta ejecución es un anillo rojo limpio sobre fondo blanco, más cercano al prompt que el resultado oscuro y con textura de Stable Diffusion 1.5 en el artículo 008.

Ficha del modelo: https://huggingface.co/leejet/Z-Image-Turbo-GGUF

#ImageGeneration #AI #OpenSource

---

## Qué es

Z-Image-Turbo Q4 es **el mismo modelo que el artículo 007**, guardado con pesos de 4 bits en formato GGUF. Es un modelo de texto a imagen: recibe un prompt y devuelve una imagen. La cuantización reduce la memoria que necesita el modelo; no cambia lo que hace.

La ejecución completa necesita además un codificador de texto (Qwen3-4B, que convierte el prompt en números que el modelo puede usar) y un VAE (que convierte el latente final en píxeles). Esas dos partes son archivos separados.

## Tipo y tecnología

- **Tarea:** generación de imágenes a partir de texto.
- **Arquitectura:** transformer de difusión (DiT) con 30 capas, tamaño oculto 3840 y 30 cabezas de atención (de `transformer/config.json` del modelo base, ver el artículo 007).
- **Cuantización:** `z_image_turbo-Q4_K.gguf`, Q4_K (4 bits con el esquema de cuantización K de llama.cpp). El repositorio lista también Q2_K, Q3_K, Q4_0, Q5_0, Q6_K y Q8_0; solo se probó Q4_K.
- **Codificador de texto:** Qwen3-4B-Instruct-2507, cuantizado a Q4_K_M en GGUF (2,50 GB).
- **VAE:** `ae.safetensors`, 16 canales latentes, autoencoder de estilo FLUX (ver el artículo 007).
- **Muestreador:** Euler, el valor por defecto del runtime en esta ejecución; 8 pasos, CFG 1,0 (ejemplo del runtime; la ficha del modelo base usa guidance 0,0 en diffusers).
- **Implementación:** stable-diffusion.cpp, en C/C++, con backend CPU (AVX, AVX2 y AVX512 en x86, según su README).

## Tamaño

- **Modelo de difusión:** `z_image_turbo-Q4_K.gguf`, 3.864.250.304 bytes (3,86 GB). El modelo base en BF16 ocupa unos 12,3 GB solo para el transformer; el archivo Q4 es aproximadamente un tercio.
- **Codificador de texto:** `Qwen3-4B-Instruct-2507-Q4_K_M.gguf`, 2.497.281.120 bytes (2,50 GB).
- **VAE:** `ae.safetensors`, 335.304.388 bytes (0,34 GB).
- **Salida:** 512 × 512 en la prueba.

## Hardware mínimo

| Configuración | Memoria | Fuente | Recomendado |
|---------------|---------|--------|-------------|
| CPU, las tres partes en RAM | **6.221,12 MB** | Medido: el informe de memoria del runtime (codificador de texto 2.375,91 MB, modelo de difusión 3.685,21 MB, VAE 160,00 MB) | Cualquier PC con 8 GB de RAM *(estimación para el resto del sistema)* |
| Modelo base en BF16 (artículo 007) | ≈ 20 GB | Cálculo (no ejecutado aquí) | GPU |

No se ha medido el uso total de RAM del proceso; los 6,2 GB son los pesos según el informe del runtime.

**Nuestro equipo (15,7 GB de RAM, gráficos integrados, sin CUDA):** la ejecución terminó con `--offload-to-cpu`. Los pesos se quedaron en RAM; no se usó GPU.

## Interfaces

- `sd-cli.exe`: el comando usado aquí, con `--diffusion-model`, `--vae`, `--llm` (el codificador Qwen3), `-p`, `-W`, `-H`, `--steps`, `--cfg-scale`, `-s`, `--offload-to-cpu` y `-o`.
- `sd-server.exe`: la misma release, sin probar.
- Python: `test_zimage_gguf_sdcpp.py` (en `lab-img/`) llama a `sd-cli.exe` y guarda su registro.
- ComfyUI: no probado aquí. Los archivos reempaquetados del modelo base están documentados para ComfyUI (ver el artículo 007).

## Quién lo usa y para qué

- El repositorio cuantizado tiene 265.885 descargas el último mes y 63 me gusta (a 2026-11-12). Las descargas miden alcance, no calidad.
- La ficha no nombra empresas ni proyectos que usen el modelo.

## Por qué importa

Es el primer modelo de la serie que genera una imagen con un modelo de 6.000 millones de parámetros en este portátil. La cuantización hace que la memoria quepa; el coste es el tiempo. Una imagen de 8 pasos tardó 480 s, y el muestreo solo 439 s, unos 55 s por paso *(medición propia)*. Una GPU sería mucho más rápida. De las pruebas de la serie con modelos de 6.000 millones de parámetros, esta es la única que funcionó en el equipo de referencia.

## Detrás del modelo

- **Modelo base:** Tongyi-MAI (grupo Alibaba), ver el artículo 007.
- **Cuantización:** `leejet`, autor de stable-diffusion.cpp. La ficha enlaza al modelo base e indica que los archivos cuantizados siguen la licencia del modelo base, Apache 2.0.
- **Codificador de texto:** el repositorio de unsloth; el modelo Qwen3 es del equipo Qwen de Alibaba.

## Curiosidades

- El prompt pedía "a red circle on a white background". Esta ejecución dibujó un anillo rojo con centro blanco sobre fondo blanco, sin textura. El mismo prompt en SD 1.5 (artículo 008) dio un fondo oscuro con textura.
- La ficha del modelo base indica guidance 0,0; el ejemplo del runtime usa CFG 1,0. Ambos evitan la segunda pasada por paso, pero el valor no es el mismo, y usamos el del runtime.

---

## Familias

| Familia | Valor | Motivo |
|---------|-------|--------|
| Grupo (arquitectura) | Difusión (transformer de difusión, DiT) | Misma arquitectura que el artículo 007. |
| Categoría | Paradox | Variante cuantizada (GGUF Q4_K) de un modelo conocido, según la regla de `CLAUDE.md`. |
| Nivel (parámetros) | UU (4–14 B) | 6,15 B de parámetros en el transformer; la cuantización no cambia el nivel. |
| Tipo (modalidad) | Imagen | Entrada de texto, salida de imagen. |
| Línea evolutiva | Z-Image → Z-Image-Turbo → Z-Image-Turbo Q4 | Versión cuantizada del modelo del artículo 007. |
| Ditto | No asignado | Usado como modelo terminado. |

---

## Cómo ejecutarlo

**Estado: probado en el equipo (CPU, stable-diffusion.cpp, una imagen).** Script: `lab-img/test_zimage_gguf_sdcpp.py`. Registro: `lab-img/out/zimage_gguf_prueba.log`. Imagen: `lab-img/out/zimage_gguf_prueba.png`.

### a. Requisitos previos
- Windows 11 con una CPU que soporte AVX2.
- Unos 7 GB libres para los tres archivos del modelo.
- Python 3.12 (el script solo usa la biblioteca estándar).

### b. Runtime
Descargar `sd-master-b9d7176-bin-win-cpu-x64.zip` de la release `master-1091-b9d7176` (SHA-256 `7e881e3c95d7ec9bf4b46e87fda37c156da9b38d18fa2439d18f29915750acbb`). Extraerlo en `lab-img/sdcpp/bin/`. Es el mismo build que el del artículo 008.

### c. Archivos del modelo (en `lab-img/models/`)

| Archivo | Fuente | Tamaño | SHA-256 |
|---------|--------|--------|---------|
| `z_image_turbo-Q4_K.gguf` | `leejet/Z-Image-Turbo-GGUF` | 3,86 GB | `14b375ab4f226bc5378f68f37e899ef3c2242b8541e61e2bc1aff40976086fbd` |
| `Qwen3-4B-Instruct-2507-Q4_K_M.gguf` | `unsloth/Qwen3-4B-Instruct-2507-GGUF` | 2,50 GB | `3605803b982cb64aead44f6c1b2ae36e3acdb41d8e46c8a94c6533bc4c67e597` |
| `ae.safetensors` | `Comfy-Org/z_image_turbo` (`split_files/vae/`) | 0,34 GB | `afc8e28272cd15db3919bacdb6918ce9c1ed22e96cb12c4d5ed0fba823529e38` |

Los hashes son los de los archivos locales; no se han comparado con las sumas de verificación de los publicadores, que no se han leído.

### d. Ejemplo mínimo
`lab-img/test_zimage_gguf_sdcpp.py`, con los valores por defecto: prompt `a red circle on a white background`, 512 × 512, 8 pasos, CFG 1,0, semilla 42, `--offload-to-cpu`. Ejecutar desde `lab-img/`: `python test_zimage_gguf_sdcpp.py`.

### e. Comprobación
El script informa del código de salida, el tiempo total y las rutas. El código 0 significa que la imagen se guardó.

### f. Avisos
- **Descarga:** unos 6,4 GB en total para los tres archivos.
- **Tiempo:** unos 8 minutos por imagen en este equipo. Plantearlo como tarea por lotes.
- **Licencia:** Apache 2.0 para el modelo y el codificador de texto. El VAE viene de un repositorio de reempaquetado; ver Pendiente.

### Resultados en el equipo (2026-11-12)

| Medida | Valor | Fuente |
|--------|-------|--------|
| Código de salida | 0 | Salida del script |
| Tiempo total, una imagen | 480,4 s | Registro del runtime (`generate_image completed in 480.42s`) |
| Cálculo del codificador de texto | 2,2 s | Registro del runtime (`get_learned_condition`) |
| Muestreo (8 pasos, Euler) | 439,3 s, unos 55 s por paso | Registro del runtime |
| Decodificación VAE | 39,0 s | Registro del runtime |
| Pesos en RAM | 6.221,12 MB | Registro del runtime (codificador de texto 2.375,91 MB, modelo de difusión 3.685,21 MB, VAE 160,00 MB) |
| Salida | 512 × 512, anillo rojo sobre fondo blanco | Imagen vista |

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Parámetros del modelo base | 6,15 B (transformer) | Artículo 007 | Sí |
| Arquitectura | 30 capas, oculto 3840, 30 cabezas | `transformer/config.json` (modelo base) | Sí |
| Cuantización usada | Q4_K, 3,86 GB | Listado de archivos de `leejet/Z-Image-Turbo-GGUF` | Sí |
| Licencia de la cuantización | Apache 2.0 | Etiqueta y ficha del repositorio | Sí |
| Codificador de texto | Qwen3-4B-Instruct-2507, Q4_K_M, 2,50 GB, Apache 2.0 | Etiqueta y tamaño de archivo del repositorio de unsloth | Sí |
| VAE | `ae.safetensors`, 0,34 GB | Listado de archivos de `Comfy-Org/z_image_turbo` | Sí (tamaño); original no verificado (ver Pendiente) |
| Runtime | `master-1091-b9d7176`, MIT | Release de GitHub | Sí |
| SHA-256 del runtime | `7e881e3c…` | Zip descargado y digest de la release | Sí |
| Pesos en RAM | 6.221,12 MB | Registro del runtime en este equipo | Sí (medido) |
| Tiempos | 480,4 s total, 439,3 s muestreo, 39,0 s decodificación | Registro del runtime en este equipo | Sí (medido) |
| Tiempo del modelo base en BF16 | No ejecutado | — | — |
| Descargas (repositorio cuantizado) | 265.885, último mes | API de HF, 2026-11-12 | Sí (instantánea) |

## Pendiente

- **Procedencia del VAE:** el archivo `ae.safetensors` viene de `Comfy-Org/z_image_turbo`, un reempaquetado público. El VAE original de FLUX.1 en `black-forest-labs/FLUX.1-schnell` exige aceptar una licencia (HTTP 401 sin sesión), así que no se usó. El archivo de Comfy-Org no se ha comparado con el original; comprobar su hash antes de afirmar que es idéntico.
- **Calidad frente a BF16:** el modelo base no se ejecutó en este equipo, así que la imagen no se puede comparar con el resultado BF16 del artículo 007.
- **Memoria del proceso:** los 6,2 GB son el informe del runtime. Medir el pico de RAM del proceso antes de dar un total.
- **Tipos de cuantización:** solo se probó Q4_K. Q4_0 y Q8_0 aparecen en el repositorio pero no se han medido.
- **Guidance:** el ejemplo del runtime usa CFG 1,0 y la ficha usa guidance 0,0 en diffusers. La diferencia no se ha probado.
