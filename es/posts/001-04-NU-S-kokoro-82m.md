# 001 · Kokoro-82M

**Fuente principal:** https://huggingface.co/hexgrad/Kokoro-82M
**Licencia:** Apache 2.0
**Consultado:** 2026-11-06
**Código:** 04-NU-S-001 (catálogo 04 Voz y audio · NU · Starter)
**Pokémon asociado:** Jigglypuff — es el Pokémon que canta para dormir a la gente; un modelo que "habla" con 82 millones de parámetros encaja con esa idea de voz ligera y reconocible.

---

## Resumen

Un modelo que habla con 82 millones de parámetros. Cabe en tu portátil.

Kokoro es un modelo de texto a voz (TTS) de código abierto, con pesos publicados bajo licencia Apache 2.0, lo que permite usarlo también en proyectos comerciales.

🔧 **Tipo y tecnología:** TTS basado en StyleTTS 2 con un decodificador ISTFTNet. Solo decodificador: no usa difusión. Se usa desde Python, con el paquete `kokoro` y el conversor grafema-fonema `misaki`.
📏 **Tamaño:** 82 millones de parámetros. Versión 1.0, publicada el 27 de enero de 2025, entrenada con unas pocas cientos de horas de audio.
💻 **Hardware mínimo:** CPU y RAM de un portátil normal. Los pesos ocupan unos 330 MB en fp32 *(estimación: 82 M × 4 bytes; no lo indica la ficha)*.
🛠️ **Interfaces:** API de Python (`KPipeline`), con salida de audio a 24 kHz. Hay demo en Hugging Face Spaces y un notebook de Google Colab.
👥 **Quién lo usa y para qué:** asistentes de voz, lectura de textos y prototipos. La ficha indica que ya se ha desplegado en numerosos proyectos y APIs comerciales.
💡 **Por qué importa:** su precio de API era de menos de 1 dólar por millón de caracteres en abril de 2025, según la propia ficha. Demuestra que un modelo pequeño puede sonar muy bien si se entrena con buenos datos.
🏢 **Detrás del modelo:** la arquitectura viene de StyleTTS 2 (Li et al., con código en GitHub). El modelo lo entrenó de forma independiente el desarrollador conocido como rzvzn, con un coste de unos 1.000 dólares en GPUs A100.
🤓 **Curiosidad:** "kokoro" significa "corazón" o "espíritu" en japonés, y es también el nombre de una IA de la saga Terminator.

Ficha y demo: https://huggingface.co/hexgrad/Kokoro-82M

---

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Parámetros | 82 M | Ficha HF | Sí |
| Licencia | Apache 2.0 | Metadatos de la ficha | Sí |
| Arquitectura | StyleTTS 2 + ISTFTNet, solo decodificador | Ficha HF ("Model Facts") | Sí |
| Lenguaje / librerías | Python, `kokoro` ≥0.9.2, `misaki`, `espeak-ng` | Ficha HF (uso) | Sí |
| Versión y fecha | v1.0, 27 ene 2025 | Tabla "Releases" | Sí |
| Datos de entrenamiento | Unas pocas cientos de horas, audio permisivo y sintético de proveedores cerrados | Ficha HF | Sí |
| Coste de entrenamiento | ~1.000 USD (1.000 h de A100 80 GB) | Ficha HF | Sí (lo declara el autor) |
| Precio de API | < 1 USD por millón de caracteres (abril 2025) | Ficha HF, cita a terceros | Sí, pero es dato de 2025 |
| Idiomas y voces | v1.0: 8 idiomas y 54 voces | Tabla "Releases" (enlace a VOICES.md) | Sí |
| Hardware mínimo | ~330 MB de pesos en fp32 | Cálculo propio | **Estimación** |
| Significado del nombre | "corazón/espíritu" en japonés | Ficha HF | Sí |
| Prueba local (inglés) | Carga, síntesis y RTF 1,08 en CPU; código de salida 0 | `lab-tts/test_kokoro.py`, ejecutado en el equipo | Sí (una ejecución) |
| Prueba local (español) | Síntesis con `ef_dora`, espeak-ng 1.52.0; RTF 0,66 | `lab-tts/test_kokoro_es.py`, ejecutado en el equipo | Sí (una ejecución) |
| Idiomas (VOICES.md) | La tabla de releases dice 8; VOICES.md lista 9 bloques de idioma | Ficha HF, VOICES.md | Discrepancia, pendiente |

## Laboratorio local (lab-tts)

Probado en el equipo de trabajo: Windows 11, Python 3.12.10, GPU Intel UHD (sin CUDA, todo en CPU) y 15,7 GB de RAM. Código, README y pasos en [lab-tts/README.md](../lab-tts/README.md).

Comandos usados (PowerShell, desde `lab-tts`):

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install "kokoro>=0.9.4" soundfile
.\.venv\Scripts\python.exe test_kokoro.py
```

Resultado de la primera ejecución en inglés:

| Medida | Valor |
|--------|-------|
| Versiones | kokoro 0.9.4, torch 2.15.0+cpu |
| Carga del modelo (incluye descarga de pesos) | 58,6 s |
| Audio generado | 8,40 s en un segmento |
| Tiempo de síntesis | 9,0 s |
| RTF | 1,08 |

Prueba en español (`test_kokoro_es.py`, con espeak-ng 1.52.0 instalado):

| Medida | Valor |
|--------|-------|
| Audio generado | 6,90 s con la voz `ef_dora` |
| Tiempo de síntesis | 4,6 s |
| RTF | 0,66 (modelo ya en caché) |

La primera ejecución descarga los pesos (~330 MB) y `en_core_web_sm` (~13 MB) para misaki. Salen avisos de deprecación de PyTorch y de symlinks en Windows; no impiden la ejecución.

## Ajustes: idioma, voz y velocidad

- **Idioma:** se fija al crear el pipeline, `KPipeline(lang_code=...)`. Códigos del repo: `a` inglés americano, `b` inglés británico, `e` español, `f` francés, `i` italiano, `p` portugués de Brasil, `h` hindi. `j` (japonés) necesita `misaki[ja]` y `z` (chino) necesita `misaki[zh]`. El español requiere espeak-ng; ya está instalado en el equipo (1.52.0).
- **Voz:** se elige al llamar al pipeline, `pipeline(texto, voice="...")`. El prefijo de la voz debe coincidir con el idioma. Voces en español según VOICES.md: `ef_dora` (femenina), `em_alex` y `em_santa` (masculinas).
- **Velocidad:** el parámetro `speed` (float o función) acelera o alarga el audio. Lo he probado en las muestras de la sección de juego. VOICES.md recomienda usarlo en textos muy largos para evitar que el modelo acelere.
- **Frases mezcladas:** la prueba usaba una frase en español y otra en inglés con `lang_code="a"`. La parte en español se pronuncia con acento inglés, así que conviene un solo idioma por ejecución.

## Voces disponibles

La v1.0 incluye 54 voces en 9 idiomas, según VOICES.md. El prefijo indica el idioma (`a`, `b`, `e`, `f`, `h`, `i`, `j`, `p`, `z`) y la segunda letra el sexo (`f` femenina, `m` masculina). Cada voz tiene una calificación global de A a F, que refleja la calidad y la cantidad de datos de entrenamiento; la ficha advierte de que es subjetiva.

| Idioma | Voces (F / M) | Nombres |
|--------|---------------|---------|
| Inglés americano (`a`) | 11 / 9 | af_heart (A), af_bella (A-), af_nicole, af_aoede, af_kore, af_sarah, af_alloy, af_nova, af_jessica, af_river, af_sky · am_fenrir, am_michael, am_puck, am_adam, am_echo, am_eric, am_liam, am_onyx, am_santa |
| Inglés británico (`b`) | 4 / 4 | bf_emma (B-), bf_isabella, bf_alice, bf_lily · bm_george, bm_fable, bm_lewis, bm_daniel |
| Japonés (`j`) | 4 / 1 | jf_alpha, jf_gongitsune, jf_nezumi, jf_tebukuro · jm_kumo |
| Chino mandarín (`z`) | 4 / 4 | zf_xiaobei, zf_xiaoni, zf_xiaoxiao, zf_xiaoyi · zm_yunjian, zm_yunxi, zm_yunxia, zm_yunyang |
| Español (`e`) | 1 / 2 | ef_dora · em_alex, em_santa |
| Francés (`f`) | 1 / 0 | ff_siwis |
| Hindi (`h`) | 2 / 2 | hf_alpha, hf_beta · hm_omega, hm_psi |
| Italiano (`i`) | 1 / 1 | if_sara · im_nicola |
| Portugués de Brasil (`p`) | 1 / 2 | pf_dora · pm_alex, pm_santa |

Las voces en español son muy pocas (tres) y la ficha no les da calificación. El francés tiene una sola voz.

## Juego: voces, mezclas y velocidades

El script [lab-tts/jugar_kokoro.py](../lab-tts/jugar_kokoro.py) genera 12 muestras en `out/juego/`:

- **Voces en inglés:** `af_heart`, `af_bella`, `am_adam`, `bm_george`, con la misma frase.
- **Mezcla de voces:** `voice="af_heart,am_michael"`. El repo promedia los embeddings de las dos voces, así que se obtiene una voz intermedia.
- **Velocidad:** `speed=0.75` (lento), `speed=1.25` (rápido) y `speed=1.0` para `af_heart`.
- **Español:** `ef_dora`, `em_alex`, `em_santa`, la mezcla `ef_dora,em_alex` y `ef_dora` a `speed=0.8`.

| Muestra | Voz | Velocidad | Audio | Síntesis | RTF |
|---------|-----|-----------|-------|----------|-----|
| en_af_heart | af_heart | 1.0 | 4,97 s | 3,4 s | 0,69 |
| en_af_bella | af_bella | 1.0 | 5,47 s | 7,3 s | 1,33 |
| en_am_adam | am_adam | 1.0 | 5,22 s | 4,0 s | 0,77 |
| en_bm_george | bm_george | 1.0 | 5,85 s | 5,0 s | 0,86 |
| en_mezcla_heart_michael | af_heart + am_michael | 1.0 | 5,30 s | 3,8 s | 0,71 |
| en_af_heart_lento | af_heart | 0,75 | 6,70 s | 3,5 s | 0,52 |
| en_af_heart_rapido | af_heart | 1,25 | 4,17 s | 2,5 s | 0,60 |
| es_ef_dora | ef_dora | 1.0 | 4,55 s | 2,6 s | 0,58 |
| es_em_alex | em_alex | 1.0 | 4,58 s | 3,7 s | 0,81 |
| es_em_santa | em_santa | 1.0 | 4,62 s | 9,0 s | 1,94 |
| es_mezcla_dora_alex | ef_dora + em_alex | 1.0 | 4,53 s | 2,4 s | 0,54 |
| es_ef_dora_lento | ef_dora | 0,8 | 5,78 s | 3,2 s | 0,56 |

Lo que se puede observar en estas pruebas, sin valorar todavía el sonido:

- La velocidad cambia la duración del audio casi proporcionalmente: 0,75 alarga la muestra de 4,97 s a 6,70 s, y 1,25 la acorta a 4,17 s.
- Las mezclas funcionan y producen audio sin errores. Si suena natural o no, hay que escucharlo.
- El RTF es más alto en la primera vez que se usa cada voz (`af_bella` y `em_santa`). Hay que repetir las medidas para tener un valor estable.

Estas muestras son de una sola ejecución. Escucharlas y valorarlas es el paso que falta.

## Límite: no clona tu voz

Kokoro no permite clonar una voz. Sus voces son presets fijos (la ficha habla de 54 voces en la v1.0). Para sonar como una voz concreta haría falta otro modelo de clonación, con su propia licencia y requisitos. No lo he comprobado todavía.

## Servicio (planificado, no construido)

Kokoro no incluye servidor. La opción prevista es envolverlo con FastAPI y uvicorn dentro del mismo venv:

- Un endpoint `POST /tts` que recibe el texto y devuelve un WAV.
- El pipeline se carga una vez al arrancar, así las peticiones posteriores no repiten la carga.
- Escuchar solo en `127.0.0.1`, para que no sea accesible desde otros equipos.

Con un RTF de 1,08 en este equipo, cada petición tardaría más o menos lo que dura el audio. Sirve para uso personal y pruebas, no para muchos usuarios a la vez.

## Pendiente

- **Hardware:** RTF medido (1,08 en la primera ejecución). Falta medir la RAM pico y repetir la prueba para tener un valor estable.
- **Idiomas:** la tabla de releases dice 8 y VOICES.md lista 9 bloques de idioma. Revisar antes de publicar.
- **Español:** síntesis probada con `ef_dora`. Falta valorar la calidad de la voz al escucharla; no lo he podido hacer yo.
- **Escucha:** valorar la calidad de las 12 muestras de `out/juego/`. Yo no puedo escucharlas.
- **Servicio FastAPI:** no construido.
- **Precio de API:** dato de abril 2025; revisar antes de publicar.
