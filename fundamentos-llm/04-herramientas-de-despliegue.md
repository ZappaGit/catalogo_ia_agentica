# 04 · Herramientas para desplegar un LLM

**Consultado:** 2026-11-08
**Relacionado:** [03-despliegue-e-integracion.md](03-despliegue-e-integracion.md) (formas de desplegar y cómo integrar el modelo).

Este documento describe cada herramienta: qué es, su licencia, cómo se instala, cómo se arranca Qwen3, en qué puerto responde y qué hardware pide. Lo que se ha comprobado en este equipo se indica; lo demás viene de la documentación oficial citada en la última sección.

---

## 1. Comparativa rápida

| Herramienta | Tipo | Licencia | Hardware habitual | API | Probada aquí |
|-------------|------|----------|-------------------|-----|--------------|
| `transformers` (Python) | Librería | Apache 2.0 | CPU o GPU | No incluye servidor | Sí (0,6 B, CPU) |
| Ollama | Programa local con API | MIT | CPU o GPU | Sí (`/api/chat` y compatible) | No |
| llama.cpp (`llama-server`) | Servidor en C/C++ | MIT | CPU o GPU, modelos GGUF cuantizados | Sí (compatible con OpenAI) | No |
| LM Studio | Aplicación de escritorio | Gratuita, cerrada (ver sección 7) | CPU o GPU | Sí, puerto 1234 | No |
| vLLM | Servidor para producción | Apache 2.0 | GPU NVIDIA, modelo completo en VRAM | Sí (compatible con OpenAI) | No |
| SGLang | Servidor para producción | Apache 2.0 | GPU (también CPU e Intel, según la guía) | Sí (compatible con OpenAI) | No |
| MLX-LM | Librería y servidor | MIT | Apple Silicon (ver sección 7) | Sí | No |
| KTransformers | Motor de inferencia híbrido | Apache 2.0 | CPU y GPU (ver sección 7) | Sí (según la ficha) | No |

---

## 2. Transformers (Python)

Es la librería de Hugging Face que usamos en `lab-llm/`. No es un servidor: el modelo vive dentro de tu programa.

**Instalación** (desde la ficha de Qwen3):

```powershell
pip install "transformers>=4.51.0" accelerate
```

**Uso:** `AutoModelForCausalLM.from_pretrained(...)` y `model.generate(...)`. Es la opción para entender el proceso (tokens, muestreo, razonamiento), no para atender peticiones de varios usuarios.

**En nuestro equipo:** probada con Qwen3-0,6B en CPU, a unos 5 tokens/s. Qwen3-8B carga, pero no cabe en RAM y la generación va por disco (ver [02](02-limites-y-razonamiento.md) y el artículo 002).

---

## 3. Ollama

Programa que descarga, guarda y ejecuta modelos en tu equipo, con una API local. Es la opción más sencilla para empezar.

**Instalación** (comandos del README oficial):

```powershell
irm https://ollama.com/install.ps1 | iex
```

En Windows también hay instalador gráfico en ollama.com. En Linux: `curl -fsSL https://ollama.com/install.sh | sh`.

**Arrancar Qwen3:**

```powershell
ollama run qwen3:8b
```

Las etiquetas de Qwen3 en el catálogo son `qwen3:0.6b`, `qwen3:1.7b`, `qwen3:4b`, `qwen3:8b`, `qwen3:14b`, `qwen3:30b`, `qwen3:32b` y `qwen3:235b` (comprobado el 2026-11-08). La cuantización de cada etiqueta está en su página; no la hemos comprobado.

**API:** escucha en `http://localhost:11434`. El README oficial documenta `/api/chat`:

```powershell
curl http://localhost:11434/api/chat -d '{ "model": "qwen3:8b", "messages": [{"role": "user", "content": "Hola"}], "stream": false }'
```

**Estado aquí:** no instalada ni probada.

---

## 4. llama.cpp (`llama-server`)

Motor en C/C++ que ejecuta modelos en formato **GGUF**, que suelen estar cuantizados (menos bits por peso, menos memoria). Incluye un servidor HTTP con API compatible con OpenAI.

**Instalación:** el README oficial indica un gestor de paquetes (por ejemplo Winget en Windows, marcado en el badge del README) o compilar desde el código. La instalación exacta depende del sistema; conviene seguir la guía de la versión que se use.

**Arrancar un modelo desde Hugging Face** (opción `-hf` del servidor, documentada en `tools/server/README.md`):

```powershell
llama-server -hf <usuario>/<repositorio-GGUF-de-Qwen3>:Q4_K_M --port 9931
```

El repositorio GGUF de Qwen3-8B no se ha comprobado todavía; hay que buscar uno oficial o de confianza y citarlo en el artículo. La cuantización por defecto es `Q4_K_M` si no se indica otra.

**Puerto:** `--port` por defecto es **9931** en la versión documentada (comprobado el 2026-11-08). Ojo: no es el 8080 que aparece en muchos tutoriales antiguos.

**Razonamiento:** las opciones documentadas son `--reasoning on|off|auto` (por defecto `auto`, que lo detecta de la plantilla), `--reasoning-format` (cómo se devuelve el bloque `<think>`) y `--reasoning-budget N` (tope de tokens para pensar). Este último es útil para evitar lo que vimos en `lab-llm/`: el razonamiento que se come toda la respuesta.

**Contexto largo:** la ficha de Qwen3 indica los parámetros de YaRN para `llama-server`: `--rope-scaling yarn --rope-scale 4 --yarn-orig-ctx 32768`, para pasar de 32.768 a 131.072 tokens.

**Instalación actual (README, comprobado el 2026-11-08):** el README recomienda ahora un script de instalación (`curl -LsSf https://llama.app/install.sh | sh` en Linux o macOS, `irm https://llama.app/install.ps1 | iex` en PowerShell), además de los binarios de la página de releases, Docker y la compilación desde el código. Tras instalarlo aparece también un comando `llama` con subcomandos `cli` y `serve`. Lo anterior sobre Winget sigue siendo válido como insignia del README, pero no es la vía principal.

**Prueba en Raspberry Pi 5 (8 GB, 4 hilos, aarch64):** compilado desde el código fuente (`llama-cli` y `llama-bench`) y probado con Qwen3-1.7B en Q8_0 (1,70 GiB, desde `Qwen/Qwen3-1.7B-GGUF`, licencia Apache 2.0). Resultados medidos:

| Prueba | Resultado |
|--------|-----------|
| Procesamiento del prompt (`llama-bench` pp512) | 43,77 ± 0,02 t/s |
| Generación (`llama-bench` tg128) | 6,31 ± 0,02 t/s |
| Prueba rápida (`llama-cli`, `-n 300`, con razonamiento) | 38,6 t/s de prompt y 5,7 t/s de generación; respuesta **truncada** a 300 tokens |
| Temperatura máxima medida | 74,1 °C; `get_throttled` = `0x0` tras las pruebas |

Dos observaciones prácticas:

- La caché de modelos de esta versión está en la de Hugging Face (`~/.cache/huggingface/hub/`), no en `~/.cache/llama.cpp/`, como sugería el script de prueba.
- Con razonamiento activado, el modelo gastó la mayor parte de los 300 tokens en el bloque `<think>`. Para tareas de clasificación o resumen conviene `--reasoning off`.

Estimaciones para tareas de la serie (aritmética a partir de las velocidades medidas, no medidas de extremo a extremo): clasificar un mensaje, unos 2–3 s; resumir un documento de 300 palabras, unos 25 s; responder con tres fragmentos de RAG, unos 30 s. Detalle y advertencias en el artículo [005 · llama.cpp](../posts/005-01-NU-S-llama-cpp.md).

**Estado aquí:** instalada y probada en la Raspberry Pi 5 (ver arriba). No probada en el equipo de referencia con Windows.

---

## 5. LM Studio

Aplicación de escritorio con interfaz gráfica para descargar y chatear con modelos, que también puede arrancar un servidor local compatible con OpenAI.

**Servidor:** la documentación oficial usa el puerto **1234** y la base `http://localhost:1234/v1` (comprobado el 2026-11-08). El cliente de OpenAI de Python funciona cambiando `base_url`.

**Qwen3:** se busca el modelo en la propia aplicación. No hemos comprobado qué variantes de Qwen3 están disponibles en ella.

**Estado aquí:** no instalada ni probada.

---

## 6. vLLM y SGLang (servidores de producción)

Pensados para servir a varios usuarios a la vez, con GPU. Ambos ofrecen una API compatible con OpenAI.

**Instalación** (README oficial de cada uno):

```powershell
uv pip install vllm
uv pip install --prerelease=allow sglang
```

Las guías completas de instalación están en docs.vllm.ai y docs.sglang.io. En Windows lo habitual es usar WSL 2 con Ubuntu.

**Arrancar Qwen3** (comandos de la ficha de Qwen3-8B):

```shell
# vLLM
vllm serve Qwen/Qwen3-8B --enable-reasoning --reasoning-parser deepseek_r1

# SGLang
python -m sglang.launch_server --model-path Qwen/Qwen3-8B --reasoning-parser qwen3
```

El argumento `--reasoning-parser` separa el razonamiento de la respuesta en la API. Los dos servidores usan parsers distintos según su versión; el de vLLM de la ficha es `deepseek_r1`.

**Puerto:** no lo hemos verificado en la documentación de cada uno. Se puede fijar con `--port`. *(Pendiente.)*

**Hardware:** el modelo completo tiene que caber en VRAM. Para Qwen3-8B en BF16, unos 24 GB de VRAM (ver el artículo 002). La guía de SGLang menciona también GPU Intel y CPU Xeon.

**Estado aquí:** no instalados. Nuestro equipo no tiene GPU NVIDIA con CUDA.

---

## 7. MLX-LM y KTransformers

**MLX-LM** (MIT): librería de Apple para ejecutar modelos con MLX. El README oficial muestra `pip install mlx-lm` y `mlx_lm.generate`. Está pensada para Macs con Apple Silicon. *(La restricción a Apple Silicon es de conocimiento general, no está comprobada en esta sesión.)*

**KTransformers** (Apache 2.0): motor de inferencia que reparte capas entre CPU y GPU. Según su descripción general, sirve para ejecutar modelos grandes con poca VRAM. *(No se ha leído su documentación en esta sesión; hay que revisarla antes de usarla en el artículo.)*

**LM Studio** (sección 5) no es software libre: se distribuye gratis, pero bajo condiciones propias. Los términos completos (https://lmstudio.ai/terms) no se han leído en esta sesión.

---

## 8. Cómo elegir

| Si quieres… | Usa |
|------|-----|
| Entender el modelo (tokens, muestreo, razonamiento) | `transformers` (Python), como en `lab-llm/` |
| Probarlo en tu PC con un clic | Ollama o LM Studio |
| Un servidor local ligero con un modelo cuantizado | llama.cpp (`llama-server`) |
| Servir a varios usuarios con GPU | vLLM o SGLang |
| Usarlo en un Mac con chip de Apple | MLX-LM |

Para nuestro equipo (16 GB de RAM, sin CUDA), las opciones realistas son el 0,6 B o el 1,7 B con `transformers`, Ollama o llama.cpp, o un Qwen3-8B cuantizado en llama.cpp o Ollama. Esta última no se ha probado y la velocidad sería baja.

---

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Licencia de Ollama | MIT | API de GitHub, `ollama/ollama` (2026-11-08) | Sí |
| Licencia de llama.cpp | MIT | API de GitHub, `ggml-org/llama.cpp` | Sí |
| Licencia de vLLM | Apache 2.0 | API de GitHub, `vllm-project/vllm` | Sí |
| Licencia de SGLang | Apache 2.0 | API de GitHub, `sgl-project/sglang` | Sí |
| Licencia de MLX-LM | MIT | API de GitHub, `ml-explore/mlx-lm` | Sí |
| Licencia de KTransformers | Apache 2.0 | API de GitHub, `kvcache-ai/ktransformers` | Sí |
| Instalación de Ollama | `irm https://ollama.com/install.ps1 \| iex` | README de `ollama/ollama` | Sí |
| Puerto y ruta de Ollama | `localhost:11434`, `/api/chat` | README de `ollama/ollama` | Sí |
| Etiquetas Qwen3 en Ollama | `qwen3:0.6b` … `qwen3:235b` | https://ollama.com/library/qwen3 | Sí |
| `llama-server` puerto por defecto | 9931 | `tools/server/README.md` de `ggml-org/llama.cpp` | Sí |
| `llama-server` razonamiento | `--reasoning`, `--reasoning-format`, `--reasoning-budget` | `tools/server/README.md` | Sí |
| `llama-server` cuantización por defecto | Q4_K_M | `tools/server/README.md` | Sí |
| YaRN en `llama-server` | `--rope-scaling yarn --rope-scale 4 --yarn-orig-ctx 32768` | Ficha de Qwen3-8B | Sí |
| LM Studio puerto | 1234, `http://localhost:1234/v1` | Documentación de LM Studio (openai-compat) | Sí |
| Comandos de vLLM y SGLang | Ver sección 6 | Ficha de Qwen3-8B; README de cada proyecto | Sí |
| Instalación de llama.cpp (script) | `curl -LsSf https://llama.app/install.sh \| sh`; `irm https://llama.app/install.ps1 \| iex` | README de `ggml-org/llama.cpp` (2026-11-08) | Sí |
| Comando `llama` de llama.cpp | `llama cli -hf …`, `llama serve -hf …` | README de `ggml-org/llama.cpp` (2026-11-08) | Sí |
| Velocidad de llama.cpp en Raspberry Pi 5 (Qwen3-1.7B Q8_0) | 43,77 t/s (pp512), 6,31 t/s (tg128) | `llama-bench`, prueba propia en la Pi | Sí (medido) |
| Umbrales de throttling de Raspberry Pi | límite 85 °C; reducción entre 80 y 85 °C | Documentación de Raspberry Pi (vía búsqueda); el 80 °C de inicio viene de foros | Parcial |
| Puerto por defecto de vLLM y SGLang | — | — | **No verificado** |
| Restricción de MLX-LM a Apple Silicon | — | Conocimiento general | **No verificado** |
| Descripción de KTransformers | — | Conocimiento general | **No verificado** |
| Términos de LM Studio | — | https://lmstudio.ai/terms (no leído completo) | **No verificado** |
| Repositorio GGUF oficial de Qwen3-8B | — | — | **No verificado** |

## Pendiente

- Confirmar los puertos por defecto de vLLM y SGLang.
- Buscar y citar un repositorio GGUF de Qwen3-8B para llama.cpp.
- Leer los términos de LM Studio antes de citar su licencia.
- Revisar la documentación de KTransformers y MLX-LM antes de describirlos en un artículo.
- Probar al menos una herramienta (llama.cpp u Ollama) en este equipo y anotar el tiempo de carga y la velocidad.
