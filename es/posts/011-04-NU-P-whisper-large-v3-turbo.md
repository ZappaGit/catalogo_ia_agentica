# 011 · Whisper large-v3-turbo

**Fuente principal:** https://huggingface.co/openai/whisper-large-v3-turbo (ficha del modelo, `config.json`, API de Hugging Face)
**Paper:** Radford et al., *Robust Speech Recognition via Large-Scale Weak Supervision* (2022), https://huggingface.co/papers/2212.04356
**Licencia:** MIT (metadatos de la ficha)
**Consultado:** 2026-11-14
**Código:** 04-NU-P-011 (catálogo 04 Voz y audio · tier NU · Paradox; ver la sección "Familias")
**Pokémon asociado:** —
**Origen:** catálogo del vault `IA_Agentica/HuggingFace`, categoría "04 Voz y audio". Elegido como el modelo de audio a texto más popular que funciona en un PC de 16 GB: la familia Whisper lidera el reconocimiento de voz en el Hub; `whisper-large-v3` tiene más likes, pero turbo es el que va más o menos a tiempo real en la máquina de referencia (ver "Elección").

---

## Resumen

Le pasas una nota de voz y te devuelve el texto, en un portátil sin tarjeta gráfica.

Whisper large-v3-turbo es el modelo abierto de reconocimiento de voz de OpenAI. Transcribe audio en muchos idiomas, puede traducirlo al inglés y da marcas de tiempo por frase.

🔧 **Tipo y tecnología:** reconocimiento de voz (audio a texto). Transformer codificador-decodificador, que se usa con la librería `transformers` de Hugging Face.
📏 **Tamaño:** 809 millones de parámetros. Un archivo de pesos de 1,6 GB en FP16.
💻 **Hardware mínimo:** en nuestra prueba usó 3,9 GB de RAM en un portátil solo con CPU (16 GB de RAM, sin CUDA). Un audio largo tardó en transcribirse más o menos lo mismo que en escucharse.
🛠️ **Interfaces:** Python con `transformers` (una llamada a `pipeline` con la ruta del audio), para audios de cualquier duración.
💡 **Por qué importa:** es large-v3 con el decodificador recortado de 32 capas a 4. La ficha dice que es "way faster, at the expense of a minor quality degradation".
🏢 **Detrás del modelo:** OpenAI (Alec Radford y otros), licencia MIT.
🤓 **Curiosidad:** la propia ficha de OpenAI avisa de que puede "alucinar": escribir texto que nunca se dijo en el audio.

Ficha del modelo: https://huggingface.co/openai/whisper-large-v3-turbo

---

## Elección

El usuario pidió el modelo de audio a texto más popular que pudiera usar en su ordenador personal de 16 GB. API de Hugging Face, 2026-11-14, tarea `automatic-speech-recognition`:

| Modelo | Descargas (últimos 30 días) | Likes | Nota |
|--------|-----------------------------|-------|------|
| argmaxinc/whisperkit-coreml | 67.619.890 | 266 | Whisper convertido a CoreML para Apple Silicon; no funciona en la máquina Windows de referencia |
| openai/whisper-large-v3-turbo | 4.821.167 | 3.530 | Este artículo |
| openai/whisper-large-v3 | 3.414.552 | 6.809 | El que más likes tiene; 1.550 M de parámetros |

Los dos modelos grandes caben en 16 GB. Se eligió turbo porque tiene menos capas de decodificador y es el más rápido en CPU. large-v3 no se probó en la máquina.

## Qué es

Whisper es una familia de modelos de reconocimiento de voz (ASR) y traducción de voz de OpenAI. Según la ficha, se entrenó con más de 5 millones de horas de datos etiquetados ("trained on >5M hours of labeled data") y generaliza "to many datasets and domains in a zero-shot setting".

**large-v3-turbo** es "a finetuned version of a pruned Whisper large-v3. In other words, it's the exact same model, except that the number of decoding layers have reduced from 32 to 4" (ficha). El codificador, que escucha el audio, mantiene sus 32 capas; el decodificador, que escribe el texto token a token, es mucho más pequeño.

## Tipo y tecnología

- **Arquitectura:** Transformer codificador-decodificador (*sequence-to-sequence*) (ficha, "Model details").
- **Entrada:** audio remuestreado a 16 kHz mono, convertido en un espectrograma log-Mel de 128 bandas (`num_mel_bins: 128` en `config.json`).
- **Ventana:** "Whisper has a receptive field of 30-seconds" (ficha). Los audios más largos se procesan con un algoritmo de audio largo (ver "Ajustes").
- **Capas (`config.json`):** 32 capas de codificador, 4 de decodificador, tamaño oculto 1280, vocabulario de 51.866 tokens, hasta 448 tokens de salida por ventana.
- **Tareas:** transcripción (mismo idioma que el audio) y traducción al inglés (`task="translate"`).
- **Idiomas:** los metadatos de la ficha enumeran 99 códigos de idioma. La ficha dice que da "strong ASR results in ~10 languages".

## Tamaño

- **Parámetros:** 808.878.080 (API de Hugging Face, `safetensors`, FP16).
- **Pesos:** `model.safetensors`, 1.617.824.864 bytes (unos 1,6 GB).
- **En memoria con CPU:** cargado en float32, como hace la ficha cuando no hay CUDA, los pesos ocupan unos 3,2 GB *(estimación: 808,9 M × 4 bytes)*. El pico medido del proceso fue de 3,84–3,90 GB (ver "Hardware mínimo").

## Hardware mínimo

| Configuración | Memoria | Cálculo | Recomendado |
|---------------|---------|---------|-------------|
| CPU, float32, modo secuencial | 3,84–3,90 GB de pico del proceso | Medido (`psutil`), 2026-11-14 | Portátil de referencia: 15,7 GB de RAM, 12 hilos de CPU, Intel UHD sin CUDA |
| CPU, float32, modo por trozos (lote 4) | 5,00 GB de pico | Medido | La misma máquina |
| GPU, float16 | unos 1,6 GB para los pesos *(estimación: 808,9 M × 2 bytes)* | No probado | Una GPU con CUDA |

Velocidad en la máquina de referencia (modo secuencial):

- Cada ventana de 30 segundos tardó unos 25–30 s. Un clip de 8,7 s tardó 29,7 s (RTF 3,4), porque un clip corto también ocupa una ventana entera.
- Un audio de 75,4 s tardó 82,4 s con el idioma fijado y 89,6 s con detección automática (RTF 1,09–1,19): más o menos a tiempo real.

## Interfaces

- **Python con `transformers`:** la ficha usa `pipeline("automatic-speech-recognition", ...)` y le pasa la ruta de un archivo de audio: `pipe("audio.mp3")`. Se pueden pasar varios archivos en una lista con `batch_size`.
- **API de más bajo nivel:** `AutoModelForSpeechSeq2Seq` y `AutoProcessor`, para controlar más la generación (ficha).
- **Otros runtimes:** el catálogo del vault recoge conversiones de la familia Whisper para CTranslate2 (`Systran/faster-whisper-*`) y CoreML (`argmaxinc/whisperkit-coreml`). No se comprobaron para este artículo.

## Ajustes y uso

De la ficha, salvo que se indique otra cosa:

- **Idioma:** se detecta automáticamente. Si se conoce, se puede indicar: `generate_kwargs={"language": "english"}`. En nuestra prueba, fijarlo ahorró un 8 % del tiempo en el audio largo.
- **Tarea:** `"transcribe"` por defecto; `"translate"` produce texto en inglés.
- **Marcas de tiempo:** `return_timestamps=True` por frases, `return_timestamps="word"` por palabras.
- **Audio largo:** dos algoritmos. *Secuencial* (ventana deslizante de 30 s) es el de por defecto y el recomendado cuando "transcription accuracy is the most important factor". *Por trozos* (`chunk_length_s=30`) divide el audio y se recomienda cuando lo que más importa es la velocidad. **En la CPU de referencia, el modo por trozos fue más lento (RTF 1,76 frente a 1,09), usó más memoria (5,0 frente a 3,9 GB) y repitió frases en las uniones.** Nuestra recomendación para esta máquina es el modo secuencial.
- **Heurísticas de decodificación:** la ficha muestra la temperatura escalonada `(0.0, 0.2, 0.4, 0.6, 0.8, 1.0)`, `compression_ratio_threshold=1.35`, `logprob_threshold=-1.0` y `no_speech_threshold=0.6`. No se probaron por separado.

## Quién lo usa y para qué

- La ficha dice que los usuarios previstos son sobre todo "AI researchers", y que Whisper es "also potentially quite useful as an ASR solution for developers, especially for English speech recognition".
- El catálogo del vault muestra varias conversiones de Whisper entre los modelos de voz más descargados (CoreML para dispositivos Apple, CTranslate2). No verificamos ningún producto u organización concreta que use large-v3-turbo.

## Por qué importa

Lleva la calidad del modelo más grande de Whisper a un ordenador normal. Recortar el decodificador de 32 a 4 capas abarata mucho la generación, porque el decodificador se ejecuta una vez por cada token de salida, mientras que el codificador se ejecuta una vez por cada ventana de 30 segundos. En un portátil sin GPU transcribió más o menos a tiempo real con menos de 4 GB de RAM.

## Detrás del modelo

- **Organización:** OpenAI.
- **Autores del paper:** Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey e Ilya Sutskever (BibTeX de la ficha, 2022).
- **Publicación en el Hub:** repositorio creado el 2024-10-01 (API de Hugging Face). Los detalles de la versión turbo están en una discusión de GitHub enlazada desde la ficha (https://github.com/openai/whisper/discussions/2363), que no se revisó para este artículo.
- **Ficha del modelo:** "partly been written by the Hugging Face team, and partly copied and pasted from the original model card" (aviso de la ficha).

## Curiosidades

- **Alucinaciones:** la ficha dice que, por el entrenamiento con supervisión débil sobre datos ruidosos, "the predictions may include texts that are not actually spoken in the audio input". También avisa de que puede repetir texto.
- **Uso responsable:** la ficha desaconseja "using Whisper models to transcribe recordings of individuals taken without their consent".
- **Idiomas desiguales:** la precisión es menor en los idiomas con menos datos de entrenamiento, y varía según el acento y el dialecto (ficha).
- **Ida y vuelta TTS → ASR:** para la prueba generamos el audio con Kokoro-82M (artículo 001) y lo transcribimos con Whisper. El texto volvió bien, pero con los números en cifras ("dieciséis gigas" → "16 GB").

---

## Familias

| Familia | Valor | Motivo |
|---------|-------|--------|
| Grupo (arquitectura) | Transformer codificador-decodificador | No está en la lista de grupos de la serie (decoder, encoder…); combina los dos. |
| Categoría | Paradox | Variante recortada y reentrenada de un modelo conocido (large-v3). |
| Tier (parámetros) | NU (< 1 B) | 808,9 M de parámetros. |
| Tipo (modalidad) | Audio → texto | Reconocimiento y traducción de voz. |
| Línea evolutiva | Whisper → large-v2 → large-v3 → large-v3-turbo | Tabla de tamaños de la ficha. Las fechas de cada versión no se verificaron aquí. |
| Ditto | En parte | La ficha tiene una sección de fine-tuning y dice que puede mejorar "with as little as 5 hours of labelled data". |

---

## Cómo ejecutarlo

**Estado: probado en la máquina de referencia el 2026-11-14** (Windows 11, Python 3.12.10, 15,7 GB de RAM, solo CPU). Script y resultados completos en `lab-asr/` (`transcribir.py` y `README.md`).

### a. Requisitos

- Python 3.12, unos 2 GB de disco para los pesos más la instalación de PyTorch.
- Unos 4 GB de RAM libres.

### b. Entorno virtual

```powershell
cd lab-asr
python -m venv .venv
```

### c. Instalación

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install transformers accelerate soundfile imageio-ffmpeg
```

Versiones probadas: torch 2.15.0+cpu, transformers 5.23.0. `imageio-ffmpeg` trae su propio ffmpeg, así que se pueden leer archivos mp3, m4a y opus sin instalar ffmpeg.

### d. Ejemplo mínimo

```python
import torch
from transformers import pipeline

asr = pipeline("automatic-speech-recognition",
               model="openai/whisper-large-v3-turbo",
               torch_dtype=torch.float32, device="cpu")
print(asr("audio.wav", return_timestamps=True)["text"])
```

El script del laboratorio hace lo mismo con cualquier formato y guarda el texto en un `.txt` junto al audio:

```powershell
.\.venv\Scripts\python.exe transcribir.py C:\ruta\a\nota.opus --idioma es
```

### e. Comprobación

Con el clip de prueba en español (8,7 s), la salida es: "El modelo Whisper convierte la voz en texto. Hoy hemos probado la transcripción en un ordenador sin tarjeta gráfica con 16 GB de memoria." Carga del modelo: 107,6 s la primera vez (con descarga), unos 5 s después.

### f. Avisos

- **Descarga:** 1,6 GB de pesos a la caché de Hugging Face en la primera ejecución. Windows muestra un aviso sobre symlinks; no impide la ejecución.
- **Licencia:** MIT, permite uso comercial.
- **Hardware:** en CPU, cuenta con tardar más o menos lo que dura el audio en archivos largos, y unos 30 s como mínimo en los cortos.
- **Idiomas mezclados:** en una prueba descartada con frases que alternaban español e inglés, Whisper dejó vacías las frases del segundo idioma. Con audio en un solo idioma salieron todas las frases.
- **Audio de prueba:** voz sintética y limpia. No se probaron grabaciones reales con ruido o con varias personas.

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Parámetros | 808.878.080 | API de Hugging Face (`safetensors`) | Sí |
| Licencia | MIT | Metadatos de la ficha | Sí |
| Arquitectura | Transformer codificador-decodificador; 32 capas de codificador y 4 de decodificador | Ficha; `config.json` | Sí |
| Recortado de large-v3 (32 → 4 capas de decodificador) | según la cita | Ficha | Sí |
| Datos de entrenamiento | ">5M hours of labeled data" | Ficha (la sección "Training Data" dice "No information provided") | Sí (declaración de la ficha) |
| Idiomas | 99 códigos en los metadatos; "strong ASR results in ~10 languages" | Ficha | Sí |
| Librería | `transformers` | Ficha | Sí |
| Publicación en el Hub | 2024-10-01 | API de Hugging Face (`createdAt`) | Sí |
| Tamaño de los pesos | 1.617.824.864 bytes | Cabecera HTTP de `model.safetensors` | Sí |
| RAM en CPU | 3,84–3,90 GB (secuencial), 5,00 GB (por trozos) | Medido, `lab-asr`, 2026-11-14 | Sí (medido) |
| Velocidad en CPU | RTF 1,09–1,19 en 75 s; unos 30 s para clips de menos de 30 s | Medido, `lab-asr`, 2026-11-14 | Sí (medido) |
| Autores / organización | OpenAI; Radford et al. (2022) | BibTeX de la ficha | Sí |
| Descargas / likes | 4.821.167 (30 días) / 3.530; 128.306.528 en total | API de Hugging Face (dato del 2026-11-14) | Sí |
| Usuarios u organizaciones | — | — | **No verificado** |

## Pendiente

- **Grabaciones reales:** probar una nota de voz real y una grabación con ruido; la prueba usó voz sintética y limpia.
- **Historial de versiones:** no se revisaron las fechas de publicación de large-v2, large-v3 y turbo, ni el contenido de la discusión #2363 de GitHub.
- **Runtimes más rápidos:** una versión int8 con CTranslate2 (faster-whisper) podría ir más rápido en CPU. No probado.
- **large-v3:** no se probó en la máquina, así que la diferencia de velocidad con turbo no está medida.
- **Carta:** todavía no hay carta LaTeX en `carta/` (tono 04, turquesa, `\artwave`).
