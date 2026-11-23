# 005 · llama.cpp

**Fuente principal:** https://github.com/ggml-org/llama.cpp (README, `tools/server/README.md`, API de GitHub)
**Modelo usado en la prueba:** https://huggingface.co/Qwen/Qwen3-1.7B-GGUF (ficha del modelo, Apache 2.0)
**Licencia:** MIT (llama.cpp). El modelo de la prueba, Qwen3-1.7B-GGUF, usa Apache 2.0.
**Consultado:** 2026-11-08
**Código:** 01-NU-S-005 (catálogo 01 Texto y LLM · tier NU, *provisional: llama.cpp es un runtime, no un modelo, así que no tiene tier por parámetros* · Starter; ver la sección "Familias")
**Pokémon asociado:** — (no se usa para herramientas)

---

## Resumen

Ejecutar un modelo de lenguaje en una Raspberry Pi 5 sin GPU, con un único programa en C++.

llama.cpp es un motor de inferencia de código abierto, escrito en C/C++, que ejecuta modelos de lenguaje en formato GGUF. No es un modelo: es el programa que carga los pesos y genera el texto, con una herramienta de línea de comandos y un servidor HTTP compatible con la API de OpenAI.

🔧 **Tipo y tecnología:** runtime de inferencia (no es un modelo). C/C++ con la librería `ggml`; funciona en CPU y, opcionalmente, en GPU. Lee archivos GGUF, que guardan los pesos ya cuantizados.
📏 **Tamaño:** el programa son unos pocos megabytes de binarios compilados desde el código fuente. El modelo de la prueba, Qwen3-1.7B en Q8_0, ocupa 1,70 GiB.
💻 **Hardware mínimo:** un equipo con CPU de 64 bits y RAM suficiente para el archivo del modelo más el contexto. En la Raspberry Pi 5 (8 GB) el modelo de 1,7 B en Q8_0 funcionó con unos 7 GB disponibles *(medido en nuestra prueba, no es un mínimo)*.
🛠️ **Interfaces:** CLI (`llama-cli`), servidor HTTP (`llama-server`) con API compatible con OpenAI y una API de librería.
👥 **Quién lo usa y para qué:** el README lo presenta como base de muchas herramientas y servidores locales. No hemos verificado proyectos concretos, así que no se citan nombres.
💡 **Por qué importa:** permite ejecutar un modelo cuantizado en hardware modesto, sin Python ni CUDA, y con una API estándar.
🏢 **Detrás del proyecto:** la organización `ggml-org` en GitHub. Repositorio creado el 2023-03-10.
🤓 **Curiosidad:** la última versión en el momento de la consulta era la v0.9.0 (2026-11-04), y el repositorio tenía unas 133.758 estrellas (API de GitHub, foto del 2026-11-08).

Repositorio: https://github.com/ggml-org/llama.cpp

---

## Qué es

llama.cpp es un proyecto en C/C++ para inferencia (generar texto con un modelo ya entrenado). No es un modelo ni incluye pesos. Lee modelos en formato **GGUF**, un formato de archivo que guarda los tensores y los metadatos necesarios para ejecutarlos. La mayoría de los GGUF están cuantizados: guardan los pesos con menos bits para usar menos memoria.

Tiene dos programas principales:

- `llama-cli`: ejecuta un modelo desde la terminal, en un solo turno o como chat interactivo.
- `llama-server`: un servidor HTTP con API compatible con OpenAI (rutas de chat completions, responses y embeddings, según su README).

La opción `-hf usuario/repo[:cuant]` descarga el archivo GGUF de Hugging Face y lo guarda en caché. Si no se indica la cuantización, usa `Q4_K_M` por defecto, o el primer archivo GGUF del repositorio si ese no existe (`tools/server/README.md`).

## Tipo y tecnología

- **Tipo:** runtime de inferencia. No es un modelo; ejecuta modelos.
- **Lenguaje:** C++ (API de GitHub). El núcleo es la librería `ggml`, en la que se apoya el proyecto.
- **Formatos:** GGUF, el formato que usa el proyecto para modelos cuantizados.
- **Backends:** CPU por defecto; la compilación puede usar GPU u otros aceleradores según las opciones elegidas al compilar (ver `docs/build.md`).
- **Dependencias:** el servidor HTTP usa `cpp-httplib` y `nlohmann/json`, ambas con licencia MIT (README).

## Tamaño

- **Repositorio:** el README es la referencia para la instalación. La última versión en el momento de la consulta era la v0.9.0 (2026-11-04).
- **Compilación de la prueba:** el binario `llama-cli` ocupa unos 1,2 MB y `llama-bench` unos 73 KB, enlazados dinámicamente con `libllama`. Se compiló desde la rama `master` con `--depth 1`, en el commit `7d7f028`, que informa de la versión `0.9.0-dev (build 1)`.
- **Modelo de la prueba:** `Qwen3-1.7B-Q8_0.gguf`, 1,70 GiB, 1,72 B de parámetros (salida del benchmark).

## Hardware mínimo

La memoria necesaria es aproximadamente el tamaño del archivo GGUF, más la caché KV, que crece con la longitud del contexto. La tabla muestra los tamaños de las cuantizaciones del modelo de la prueba; los tamaños de otras cuantizaciones no están verificados.

| Configuración | Memoria del modelo | Referencia |
|---------------|--------------------|------------|
| Qwen3-1.7B, Q8_0 (probado) | 1,70 GiB (benchmark) | Raspberry Pi 5, 8 GB de RAM, CPU, 4 hilos |
| Qwen3-1.7B, Q4_K_M (por defecto en `-hf`) | no medido | — |

La prueba en la Raspberry Pi 5 usó 4 hilos. La memoria antes de la prueba era de 7,9 GiB en total y unos 6,5 GiB disponibles. Durante la generación, la RAM usada era de unos 0,6 GiB y quedaban 7,3 GiB disponibles tras terminar el proceso.

## Interfaces

- **Terminal:** `llama-cli -hf <repo>:<cuant> -p "prompt" -n <tokens>`. La opción `-st` (`--single-turn`) ejecuta un turno y termina. Nuestro primer intento usó `-no-cnv`, que esta versión no acepta.
- **Servidor HTTP:** `llama-server -hf <repo>:<cuant>`. El puerto por defecto es el 9931 (`--port`), y expone las rutas compatibles con OpenAI.
- **Librería:** la API en C de `libllama` (enlazada por los ejemplos del proyecto y por aplicaciones externas).
- **Instalación:** el README ofrece un script de instalación (`llama.app`), binarios precompilados en la página de releases, Docker y compilación desde el código. Las insignias del README muestran también un paquete de Winget.

## Quién lo usa y para qué

- El README dice que el servidor lo usan proyectos y herramientas externos; no se citan proyectos concretos.
- No hemos verificado una lista de usuarios, así que este artículo no afirma ninguna.

## Por qué importa

En nuestra prueba ejecutó un modelo Qwen3 cuantizado en la Raspberry Pi 5 sin GPU y sin código Python: el programa es un binario compilado que lee el archivo GGUF. No lo hemos comparado con otras herramientas, así que este artículo no afirma nada sobre memoria o velocidad frente a ellas.

## Detrás del proyecto

- **Organización:** `ggml-org` en GitHub. El README enlaza con el proyecto `ggml`, sobre el que se construye llama.cpp.
- **Desarrollo:** la API de GitHub muestra el repositorio como activo (último push el 2026-11-08 en el momento de la consulta).

## Curiosidades

- El proyecto se creó el 2023-03-10 (API de GitHub). El README presenta ahora un comando `llama` con los subcomandos `cli` y `serve`, además de los binarios que usamos en la prueba.
- En la ficha del modelo Qwen3-1.7B-GGUF, los ajustes recomendados incluyen `--temp 0.6 --top-k 20 --top-p 0.95 --min-p 0 --presence-penalty 1.5` (ficha del modelo). En nuestra prueba no los usamos.

---

## Familias

| Familia | Valor | Motivo |
|---------|-------|--------|
| Grupo (arquitectura) | No aplica: runtime, no una red neuronal | llama.cpp ejecuta transformers decoder-only (LLM). El grupo describe el modelo, no el programa. |
| Categoría | Starter | Forma sencilla de empezar a ejecutar LLM en hardware local. |
| Tier (parámetros) | NU (< 1 B) — *provisional* | llama.cpp no tiene parámetros. Se asigna el código NU por el esquema de códigos de la serie; ver "Pendiente". |
| Tipo (modalidad) | Texto (a través del modelo que ejecuta) | La prueba usa texto. |
| Línea evolutiva | ggml → llama.cpp | El proyecto se construye sobre la librería `ggml`; el repositorio en GitHub es `ggml-org/llama.cpp`. |
| Ditto | No aplica | No es un modelo para ajuste fino. |

---

## Cómo ejecutarlo

**Estado: probado en la Raspberry Pi 5 (8 GB de RAM, aarch64, 4 hilos).** La compilación y el modelo de prueba se ejecutaron en la Raspberry Pi. No se ha probado en el equipo de referencia con Windows (15,7 GB de RAM, gráficos Intel UHD, sin CUDA). Los comandos son para la Raspberry Pi en Linux.

### a. Requisitos previos

- Raspberry Pi 5 con 8 GB de RAM, o una máquina Linux de 64 bits con RAM libre suficiente para el modelo.
- Git, CMake, un compilador de C++ y `libcurl4-openssl-dev` (instalados para la prueba; el README no indica que sean obligatorios para `-hf`).
- Acceso a internet para descargar el modelo desde Hugging Face.

### b. Compilación

```bash
sudo apt update && sudo apt install -y git cmake build-essential libcurl4-openssl-dev
git clone --depth 1 https://github.com/ggml-org/llama.cpp ~/llama.cpp
cd ~/llama.cpp
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j4 --target llama-cli llama-bench
```

La compilación tardó varios minutos en la Raspberry Pi 5 con 4 hilos (no se cronometró con precisión). Los binarios están en `build/bin/`.

### c. Prueba rápida

```bash
./build/bin/llama-cli -hf Qwen/Qwen3-1.7B-GGUF:Q8_0 \
  -st -p "Resume en tres frases: la junta aprueba cambiar el horario de la piscina." -n 300
```

Resultado: el modelo terminó el bloque de razonamiento (`[Start thinking]`) y empezó la respuesta, que quedó **truncada** a 300 tokens a mitad de frase. El límite era demasiado bajo para el modo con razonamiento, así que la salida se cortó. La ejecución muestra:

- Procesamiento del prompt: **38,6 tokens/s**.
- Generación: **5,7 tokens/s**.

### d. Benchmark

```bash
./build/bin/llama-bench -m <ruta-al-GGUF> -t 4 -p 512 -n 128 -r 3
```

La ruta de `-m` está en la caché de Hugging Face, no en `~/.cache/llama.cpp/` como sugería el script pegado. En esta versión la ruta es `~/.cache/huggingface/hub/models--Qwen--Qwen3-1.7B-GGUF/snapshots/<hash>/Qwen3-1.7B-Q8_0.gguf`.

| Prueba | Tokens | Velocidad |
|--------|--------|-----------|
| pp512 (procesamiento del prompt) | 512 | 43,77 ± 0,02 t/s |
| tg128 (generación) | 128 | 6,31 ± 0,02 t/s |

### e. Comprobación y temperatura

La temperatura de la Raspberry Pi se midió con `vcgencmd measure_temp` en varios puntos. Las lecturas fueron desde 48,8 °C (antes de la compilación) hasta 74,1 °C (durante la compilación). Tras el benchmark marcó 72,5 °C, y 59,3 °C una vez reiniciado OpenClaw y con la máquina en reposo.

### f. Avisos

- **Descarga:** el GGUF Q8_0 pesa 1,70 GiB y queda en la caché de Hugging Face.
- **Licencia:** llama.cpp es MIT. El modelo Qwen3-1.7B-GGUF es Apache 2.0 según su ficha (`license: apache-2.0`).
- **Hardware:** el modelo de 1,7 B en Q8_0 genera unos 6 tokens por segundo en la CPU de la Raspberry Pi 5. Sirve para pruebas, pero es lento para respuestas largas.
- **Muestreo:** la prueba usó los ajustes por defecto. La ficha del modelo recomienda otros (ver Curiosidades); un ajuste distinto puede cambiar el resultado y la longitud de la respuesta.

## Casos de uso estimados *(estimación: aritmética a partir del benchmark, no medido de extremo a extremo)*

Los tiempos usan las velocidades medidas: procesamiento del prompt 43,77 t/s y generación 6,31 t/s (`llama-bench`, 4 hilos). Tiempo estimado ≈ tokens de entrada / 43,8 + tokens de salida / 6,3.

| Tarea | Tokens aproximados entrada / salida | Tiempo estimado en la Pi |
|-------|-------------------------------------|--------------------------|
| Clasificar un mensaje del buzón (prompt corto, respuesta de una palabra) | ~80 / ~5 | 2–3 s |
| Resumir un documento de 300 palabras en 3 frases | ~450 / ~80 | ~25 s |
| Responder una pregunta con 3 fragmentos de RAG como contexto | ~600 / ~100 | ~30 s |

Conclusiones (estimaciones):

- Los trabajos en cola en segundo plano (clasificar, indexar, resumir) caben bien en la Pi.
- El chat en directo queda justo: con streaming, la primera palabra aparecería tras unos 10–15 s con contexto de RAG, porque procesar solo los 600 tokens del prompt tarda unos 14 s.
- Para estas tareas conviene desactivar el modo de razonamiento. En nuestra prueba consumió la mayor parte del presupuesto de tokens. La opción es `llama-cli --reasoning off` (comprobada en la ayuda de esta versión); `/no_think` no se ha probado.

**Comprobación térmica.** La temperatura máxima medida fue de 74,1 °C. La documentación oficial de Raspberry Pi describe la reducción de velocidad entre 80 y 85 °C y la reducción completa a 85 °C; el inicio a 80 °C viene de reportes de usuarios, no de la documentación. `vcgencmd get_throttled` devolvió `throttled=0x0` tras las pruebas, así que no quedó registrado ningún throttling desde el último arranque.

**Advertencia sobre la comparación.** El portátil de referencia ejecutó Qwen3-0,6B con `transformers` en float32 a 4,2–5,7 tokens/s (`lab-llm/README.md`). Es otro tamaño de modelo, otra precisión y otra herramienta, así que la diferencia no se puede atribuir solo a llama.cpp.

**Sin probar todavía:** Qwen3-4B en Q4_K_M (velocidad y calidad) y la calidad de las respuestas en español para estas tres tareas.

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Licencia de llama.cpp | MIT | API de GitHub (`ggml-org/llama.cpp`) e insignia del README | Sí |
| Lenguaje | C++ | API de GitHub | Sí |
| Repositorio creado | 2023-03-10 | API de GitHub | Sí |
| Última versión en la consulta | v0.9.0, 2026-11-04 | API de GitHub (`releases/latest`) | Sí |
| Estrellas | 133.758 | API de GitHub, foto del 2026-11-08 | Sí |
| Puerto por defecto de `llama-server` | 9931 | `tools/server/README.md` | Sí |
| Cuantización por defecto de `-hf` | Q4_K_M, o el primer GGUF | `tools/server/README.md` | Sí |
| API compatible con OpenAI | chat completions, responses, embeddings | `tools/server/README.md` | Sí |
| Licencia del modelo de prueba | Apache 2.0 | Ficha `Qwen/Qwen3-1.7B-GGUF` | Sí |
| Archivo del modelo de prueba | `Qwen3-1.7B-Q8_0.gguf`, 1,70 GiB, 1,72 B | Salida del benchmark en la Raspberry Pi | Sí (medido) |
| Velocidad en la Pi (pp512 / tg128) | 43,77 / 6,31 t/s | `llama-bench`, 4 hilos | Sí (medido) |
| Velocidad en la Pi, prueba rápida | 38,6 / 5,7 t/s | Salida de `llama-cli` | Sí (medido) |
| Temperatura de la Pi | 48,8 a 74,1 °C | `vcgencmd measure_temp` | Sí (medido) |
| Umbrales de throttling | Límite a 85 °C; reducción entre 80 y 85 °C | Documentación de Raspberry Pi (vía búsqueda); el inicio a 80 °C viene de reportes de foros | Parcial (la documentación dice 80–85 °C; el inicio en Pi 5 es de usuarios) |
| Throttling tras las pruebas | `throttled=0x0` | `vcgencmd get_throttled` en la Pi | Sí (medido) |
| Flag de razonamiento de `llama-cli` | `--reasoning off` | `llama-cli --help` de la build 7d7f028 | Sí |
| Portátil 0,6 B (transformers) | 4,2–5,7 t/s, float32 | `lab-llm/README.md` | Sí (medido en el equipo de referencia) |
| Hardware mínimo | — | — | **No verificado** (solo se reporta el caso probado) |
| Detrás del proyecto | `ggml-org` | GitHub | Sí (solo la organización) |
| Descargas de proyectos que usan llama.cpp | — | — | **No verificado** |

## Pendiente

- **Tier:** llama.cpp no tiene parámetros, así que el tier NU es un código provisional acordado para la serie. Debe confirmarse o cambiarse antes de publicar.
- **Prueba rápida truncada:** la prueba con 300 tokens se cortó en la respuesta, así que la respuesta no está completa. Una nueva ejecución con más tokens (por ejemplo 1.024) mostraría la respuesta entera.
- **Otras cuantizaciones y equipo de referencia:** la prueba cubre solo Q8_0 en la Raspberry Pi 5. Q4_K_M y el equipo de referencia con Windows no están medidos.
- **Nota de instalación en `fundamentos-llm/04`:** el README recomienda ahora un script de instalación (`llama.app`) y menciona un comando `llama`. La nota actual de ese archivo menciona la insignia de Winget y el comando `llama-server`; conviene revisarla.
