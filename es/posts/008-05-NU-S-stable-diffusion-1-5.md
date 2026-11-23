# 008 · Stable Diffusion 1.5

**Fuente principal:** https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5 (espejo del repositorio `runwayml/stable-diffusion-v1-5`, ya obsoleto)
**Runtime usado:** stable-diffusion.cpp, release `master-1091-b9d7176`, https://github.com/leejet/stable-diffusion.cpp (MIT)
**Licencia:** CreativeML OpenRAIL-M (modelo); MIT (runtime)
**Consultado:** 2026-11-12
**Código:** 05-NU-S-008 (catálogo 05 Imagen, vídeo y 3D · NU · Starter)
**Origen:** elegido por el autor para la primera prueba en CPU de los modelos de imagen de la serie. No está en la cola de candidatos del vault; es el modelo de referencia para una prueba pequeña de texto a imagen que funcione en CPU.
**Familias:** Starter · NU · Difusión (U-Net, difusión latente) · línea Stable Diffusion (ver la sección "Familias")

---

## Texto para LinkedIn

El modelo que popularizó la generación local de imágenes, ejecutado en un portátil sin tarjeta gráfica: una imagen tardó 7 minutos.

Stable Diffusion 1.5 es un modelo de texto a imagen de unos 0,9 mil millones de parámetros. Convierte una descripción escrita en una imagen, quitando ruido paso a paso en un espacio comprimido. Es de código abierto, con licencia CreativeML OpenRAIL-M, que tiene restricciones de uso.

🔧 **Tipo y tecnología:** difusión latente: un denoiser U-Net, un codificador de texto CLIP y un decodificador VAE. Ejecutado aquí con stable-diffusion.cpp, un runtime en C/C++.
📏 **Tamaño:** unos 0,9 mil millones de parámetros; el archivo que usamos (`v1-5-pruned-emaonly.safetensors`) pesa 4,27 GB. Salida de 512 × 512 píxeles.
💻 **Hardware mínimo:** el runtime informó de 2,78 GB de pesos en RAM, y funcionó en CPU sin GPU. Nuestro equipo de pruebas tiene 15,7 GB de RAM y no tiene CUDA.
🛠️ **Interfaces:** la línea de comandos `sd-cli.exe` de stable-diffusion.cpp, el servidor HTTP `sd-server` de la misma release, y Python (`diffusers`, sin probar aquí).
👥 **Quién lo usa y para qué:** la ficha no nombra usuarios. Tiene 1.019.121 descargas el último mes y 1,36 mil me gusta (a 2026-11-12), así que es uno de los modelos de imagen más usados del Hub.
💡 **Por qué importa:** es la forma más barata de ver un modelo real de texto a imagen funcionando en un portátil normal. Nuestra ejecución tardó 429 s por imagen de 20 pasos: lento, pero funciona. Los modelos más nuevos dan mejor calidad, pero necesitan más memoria *(medición propia en este equipo)*.
🏢 **Detrás del modelo:** la organización de la ficha es el espacio `stable-diffusion-v1-5` de Hugging Face, espejo del repositorio `runwayml`, ya obsoleto; los autores originales y el artículo no están comprobados todavía *(ver Pendiente)*.
🤓 **Curiosidad:** la imagen de esta ejecución salió como un anillo rojo sobre un fondo oscuro con textura. El prompt pedía fondo blanco, así que el modelo siguió "círculo rojo" y no el resto.

Ficha del modelo: https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5

#ImageGeneration #AI #OpenSource

---

## Qué es

Stable Diffusion 1.5 es un **modelo de texto a imagen**. No edita imágenes: recibe un prompt y devuelve una imagen, partiendo de ruido aleatorio y quitándolo paso a paso. La eliminación de ruido se hace en un espacio "latente" comprimido, lo que hizo práctico el modelo en hardware de consumo en su época.

## Tipo y tecnología

- **Tarea:** generación de imágenes a partir de texto.
- **Arquitectura:** difusión latente: un codificador de texto (CLIP, ver Pendiente para la versión exacta), una U-Net que predice el ruido en cada paso y un VAE que decodifica el latente final a píxeles. El archivo que usamos es un único checkpoint en safetensors con todas las partes.
- **Muestreador:** el runtime informa de "Euler A" (la línea del registro `sampling using Euler A method`), que usa por defecto.
- **Implementación:** el modelo se distribuye para PyTorch/`diffusers`. Nuestra prueba lo ejecutó con stable-diffusion.cpp, un runtime en C/C++ con backend CPU (AVX, AVX2 y AVX512 en x86, según su README).

## Tamaño

- **Parámetros:** 0,9 B (metadatos de la ficha, en F32).
- **Resolución de salida:** 512 × 512 en la prueba (valor por defecto del runtime).
- **Archivo de pesos:** `v1-5-pruned-emaonly.safetensors`, 4,27 GB. El repositorio contiene otros archivos (un segundo checkpoint más grande, archivos pickle `.ckpt` y subcarpetas de `diffusers`); el total del repositorio es de unos 47 GB.

## Hardware mínimo

| Configuración | Memoria | Fuente | Recomendado |
|---------------|---------|--------|-------------|
| CPU, pesos del runtime en RAM | 2,78 GB | Medido: el informe de memoria del propio runtime en nuestro registro | Cualquier PC con 8 GB de RAM *(estimación para el resto del sistema)* |
| GPU, FP16 | ≈ 2 GB de VRAM | Estimación a partir del tamaño de los pesos | GPU de consumo |

Los 2,78 GB son la suma del codificador de texto (469 MB), el modelo de difusión (2.155 MB) y el VAE (160 MB), según los informa el runtime. No se ha medido el uso total de RAM del proceso.

**Nuestro equipo (15,7 GB de RAM, gráficos integrados, sin CUDA):** funciona. Los tiempos de nuestra ejecución están en "Cómo ejecutarlo".

## Interfaces

- `sd-cli.exe`: la herramienta de línea de comandos usada aquí. Opciones usadas: `-m` (modelo), `-p` (prompt), `-W` y `-H` (tamaño), `--steps`, `--cfg-scale`, `-s` (semilla), `-o` (salida).
- `sd-server.exe`: un servidor de la misma release, sin probar.
- Python: `test_sd15_sdcpp.py` (en `lab-img/`) llama a `sd-cli.exe` y guarda su registro. La ruta con `diffusers` no está probada aquí.

## Quién lo usa y para qué

- La ficha no nombra empresas, productos ni proyectos de investigación que usen el modelo.
- Popularidad (2026-11-12): 1.019.121 descargas el último mes y 1,36 mil me gusta en la página de Hugging Face. Las descargas miden alcance, no calidad.

## Por qué importa

Es lo bastante pequeño para correr en la CPU de un portátil, y aun así muestra la cadena completa de texto a imagen: prompt de entrada, imagen de salida, con el muestreador, la semilla y el número de pasos a la vista. En nuestra ejecución, una imagen de 512 × 512 con 20 pasos tardó 429 s en este equipo. Los modelos más nuevos, como Z-Image-Turbo, dan mejor calidad, pero necesitan más memoria *(nuestra lectura de las ejecuciones, ver los artículos 007 y 009 de la serie)*.

## Detrás del modelo

- **Organización:** la cuenta `stable-diffusion-v1-5` de Hugging Face, que es un espejo del repositorio original `runwayml` (ya obsoleto).
- **Autores:** pendiente de comprobar en el artículo del modelo (ver Pendiente).
- **Licencia:** CreativeML OpenRAIL-M. Permite usar y redistribuir con restricciones en algunos usos; leer el texto completo antes de un uso comercial.

## Curiosidades

- La primera imagen en este equipo tenía el objeto principal correcto, un círculo rojo, pero el fondo era una textura marrón oscura y no el fondo blanco que pedía el prompt. Mantenemos ese resultado tal como salió.
- La decodificación del VAE tardó 54 s, alrededor de una séptima parte del muestreo (372,9 s), así que decodificar la imagen final no es despreciable en CPU.

---

## Familias

| Familia | Valor | Motivo |
|---------|-------|--------|
| Grupo (arquitectura) | Difusión (U-Net latente) | Elimina ruido sobre un latente en pasos y luego lo decodifica con un VAE. |
| Categoría | Starter | Modelo pequeño que funciona en la CPU de un portátil, bueno para empezar con los modelos de imagen. |
| Nivel (parámetros) | NU (< 1 B) | Unos 0,9 B de parámetros. |
| Tipo (modalidad) | Imagen | Entrada de texto, salida de imagen. |
| Línea evolutiva | Stable Diffusion 1.x → 1.5 | Versión 1.5 de la primera línea de Stable Diffusion. Las líneas posteriores (SDXL, SD3) son modelos aparte en esta serie. |
| Ditto | No asignado | Usado como modelo terminado en este artículo; también es una base habitual para fine-tuning, que no hemos probado. |

---

## Cómo ejecutarlo

**Estado: probado en el equipo (CPU, stable-diffusion.cpp, una imagen).** Script: `lab-img/test_sd15_sdcpp.py`. Registro: `lab-img/out/sd15_prueba.log`. Imagen: `lab-img/out/sd15_prueba.png`.

### a. Requisitos previos
- Windows 11 con una CPU que soporte AVX2 (el build `cpu` de la release elige el mejor juego de instrucciones en tiempo de ejecución).
- Unos 5 GB libres para el archivo del modelo.
- Python 3.12 (el script solo usa la biblioteca estándar).

### b. Runtime
Descargar el build de Windows para CPU `sd-master-b9d7176-bin-win-cpu-x64.zip` de la release `master-1091-b9d7176`. Su SHA-256 es `7e881e3c95d7ec9bf4b46e87fda37c156da9b38d18fa2439d18f29915750acbb`, que coincide con el digest publicado en la página de la release. Extraerlo en `lab-img/sdcpp/bin/`.

### c. Modelo
Descargar `v1-5-pruned-emaonly.safetensors` (4,27 GB) del repositorio indicado arriba a `lab-img/models/`.

### d. Ejemplo mínimo
`lab-img/test_sd15_sdcpp.py`, con los valores por defecto: prompt `a red circle on a white background`, 512 × 512, 20 pasos, CFG 7,0, semilla 42. Ejecutar desde `lab-img/`: `python test_sd15_sdcpp.py`.

### e. Comprobación
El script informa del código de salida, el tiempo total y las rutas. El código 0 significa que la imagen se guardó.

### f. Avisos
- **Descarga:** 4,27 GB para el modelo.
- **Tiempo:** unos 7 minutos por imagen en este equipo. Plantearlo como tarea por lotes, no interactiva.
- **Licencia:** CreativeML OpenRAIL-M, con restricciones de uso; ver el texto de la licencia.

### Resultados en el equipo (2026-11-12)

| Medida | Valor | Fuente |
|--------|-------|--------|
| Código de salida | 0 | Salida del script |
| Tiempo total, una imagen | 429,0 s | Script (incluye la carga del modelo) |
| Carga del modelo y tensores | ≈ 7,8 s | Registro del runtime (0,01 + 0,53 + 7,05 + 0,22 s entre los pasos de carga) |
| Muestreo (20 pasos, Euler A) | 372,9 s | Registro del runtime |
| Decodificación VAE | 54,3 s | Registro del runtime |
| Pesos en RAM | 2.784,45 MB | Registro del runtime (codificador de texto 469,44 MB, modelo de difusión 2.155,33 MB, VAE 159,68 MB) |
| Salida | 512 × 512, anillo rojo con centro blanco sobre fondo oscuro con textura | Imagen vista |

El prompt pedía un círculo rojo sobre fondo blanco. El modelo dibujó el círculo con un anillo rojo y un centro blanco, pero el fondo es oscuro y con textura. Es un acierto parcial, registrado tal como salió.

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Parámetros | 0,9 B | Metadatos de la ficha (F32) | Sí |
| Licencia | CreativeML OpenRAIL-M | Ficha de HF | Sí |
| Tamaño del archivo del modelo | 4,27 GB (`v1-5-pruned-emaonly.safetensors`) | Listado de archivos de HF | Sí |
| Total del repositorio | 47,3 GB | Listado de archivos de HF | Sí (instantánea) |
| Descargas último mes / me gusta | 1.019.121 / 1,36 mil | Página de HF, 2026-11-12 | Sí (instantánea) |
| Release del runtime | `master-1091-b9d7176`, MIT | Página de la release y repositorio de GitHub | Sí |
| SHA-256 del runtime | `7e881e3c…` | Zip descargado y digest de la release | Sí |
| Pesos en RAM | 2.784,45 MB | Registro del runtime en este equipo | Sí (medido) |
| Tiempos | 429 s total; 372,9 s muestreo; 54,3 s decodificación | Registro del runtime en este equipo | Sí (medido) |
| Memoria del proceso | No medida | — | **No**, ver Pendiente |
| VRAM de GPU | ≈ 2 GB | Estimación a partir del tamaño | **Estimación** |
| Autores y artículo original | No comprobados | — | **No**, ver Pendiente |
| Versión del codificador CLIP | No comprobada | — | **No**, ver Pendiente |

## Pendiente

- **Autores y artículo:** no se han leído los autores de la ficha ni el artículo original. Comprobarlos antes de contar la historia de la organización en el texto de LinkedIn.
- **Codificador de texto:** no se nombra aquí el CLIP exacto; revisar la carpeta `text_encoder` del repositorio antes de nombrarlo.
- **Memoria del proceso:** los 2,78 GB son los pesos según el informe del runtime. Medir el pico de RAM del proceso (por ejemplo, con el Administrador de tareas durante la ejecución) antes de dar un total.
- **Muestreador por defecto:** el registro dice Euler A; verificar el valor por defecto en `sd-cli -h` antes de escribirlo como ajuste fijo.
- **Origen del espejo:** el repositorio `runwayml` está obsoleto; la ficha del espejo da la historia. Confirmar las fechas exactas antes de escribirlas.
- **Comparación con GPU:** no hay cifra de GPU para SD 1.5 medida ni verificada. Las cifras de GPU encontradas en la búsqueda eran de SDXL a 1024 × 1024, otro modelo y otra resolución.
