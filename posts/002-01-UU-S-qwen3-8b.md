# 002 · Qwen3-8B

**Fuente principal:** https://huggingface.co/Qwen/Qwen3-8B
**Licencia:** Apache 2.0
**Consultado:** 2026-11-06
**Código:** 01-UU-S-002 (catálogo 01 Texto y LLMs · UU · Starter)
**Pokémon asociado:** Porygon — un Pokémon hecho de código informático, nacido en el mundo digital; un modelo de lenguaje que es puro software y puede cambiar entre "pensar" y "responder rápido" encaja con esa idea.

---

## Texto de LinkedIn

Un modelo, dos formas de pensar: Qwen3-8B alterna entre razonar paso a paso y responder rápido, con el mismo conjunto de pesos.

Qwen3-8B es un modelo de lenguaje causal de pesos abiertos (generación de texto) del equipo Qwen, con 8,2 mil millones de parámetros, publicado bajo licencia Apache 2.0, lo que permite usarlo también en proyectos comerciales.

🔧 **Tipo y tecnología:** transformer solo decodificador (decoder-only) con atención de consultas agrupadas (GQA: 32 cabezas de consulta y 8 de clave/valor), 36 capas. El modo de pensamiento viene activado por defecto y se puede desactivar por petición. Se usa desde Python con `transformers`.
📏 **Tamaño:** 8,2 B parámetros (6,95 B sin embeddings). Contexto nativo de 32.768 tokens, hasta 131.072 con YaRN. Pesos en BF16 (safetensors), unos 16,4 GB.
💻 **Hardware mínimo:** unos 24 GB de VRAM para los pesos en BF16 con algo de margen; unos 10 GB en 8 bits y unos 5 GB en 4 bits *(estimación: 8,19 B × bytes por parámetro, más un margen del 20–30 %; ver notas de verificación)*.
🛠️ **Interfaces:** Python (`transformers`), SGLang y vLLM (servidor compatible con la API de OpenAI), y aplicaciones locales como Ollama, LM Studio, MLX-LM y llama.cpp, según la ficha.
👥 **Quién lo usa y para qué:** razonamiento, código, matemáticas, agentes con herramientas externas, y chat y traducción multilingüe (más de 100 idiomas y dialectos, según la ficha). Tiene unos 7 millones de descargas en Hugging Face (snapshot del 2026-11-06).
💡 **Por qué importa:** un solo modelo cubre el chat rápido y el razonamiento largo, así que no hace falta tener dos modelos distintos para cada caso.
🏢 **Detrás del modelo:** el equipo Qwen, que desarrolla los modelos Qwen; la ficha cita el informe técnico de Qwen3 (arXiv:2505.09388).
🤓 **Curiosidad:** puedes cambiar de modo a mitad de conversación añadiendo `/think` o `/no_think` a tu mensaje.

Ficha y ejemplo: https://huggingface.co/Qwen/Qwen3-8B

#LLM #IA #OpenSource

---

## Ajustes: modo de pensamiento

- **Cambio por turno:** `/think` y `/no_think` en el mensaje del usuario cambian el modo solo en esa respuesta (ejemplo de la ficha).
- **Muestreo recomendado:** en modo pensamiento, Temperature 0.6, TopP 0.95 y TopK 20. La ficha dice **no** usar decodificación voraz (greedy).
- **Longitud de respuesta:** en modo pensamiento las salidas son largas. La ficha sugiere `max_new_tokens` de 32.768 para no cortar la respuesta.

## Hardware mínimo

| Precisión | Pesos | Con margen 20–30 % | Recomendado |
|-----------|-------|--------------------|-------------|
| BF16 / FP16 | 8,19 B × 2 B ≈ 16,4 GB | ≈ 19,7–21,3 GB | GPU con 24 GB de VRAM |
| INT8 | 8,19 B × 1 B ≈ 8,2 GB | ≈ 9,8–10,6 GB | GPU con 12 GB de VRAM |
| INT4 | 8,19 B × 0,5 B ≈ 4,1 GB | ≈ 4,9–5,3 GB | GPU con 8 GB de VRAM |

Los contextos largos necesitan memoria extra para la caché KV, así que el margen es una estimación aproximada. La inferencia en CPU usa la RAM del sistema en lugar de la VRAM y es mucho más lenta.

## Interfaces

- `transformers` (`AutoModelForCausalLM`, `AutoTokenizer`).
- SGLang (`sglang>=0.4.6.post1`) y vLLM (`vllm>=0.8.5`) para una API compatible con OpenAI.
- Ollama, LM Studio, MLX-LM, llama.cpp y KTransformers, que la ficha lista como compatibles con Qwen3.

## Quién lo usa y por qué

- Desarrolladores que necesitan un modelo abierto para razonar y para chat rápido.
- Sistemas de agentes, porque la ficha destaca la llamada a herramientas en ambos modos.
- La ficha reporta unos 7 millones de descargas y 2.170 "me gusta" (snapshot 2026-11-06). No cita usuarios de producción concretos, así que aquí no se citan.

## Por qué importa

Qwen3-8B permite que el mismo modelo razone con extensión en matemáticas o código y responda brevemente en el chat cotidiano, controlado por un interruptor en la plantilla de chat o en el prompt. Su licencia Apache 2.0 permite el uso comercial.

## Detrás del modelo

- **Organización:** equipo Qwen (la ficha menciona Alibaba).
- **Autores:** figuran en el informe técnico de Qwen3, arXiv:2505.09388, como "Qwen Team". La ficha no nombra a los autores individuales. *(Pendiente: confirmar la redacción de la afiliación en el artículo.)*

---

## Cómo ejecutarlo

**Estado: sin probar.** Los comandos de esta sección se han comprobado con la ficha del modelo y con el índice de PyPI (los nombres de paquete existen), pero no se han ejecutado en este equipo. No se ha descargado el modelo (~16,4 GB) ni se ha lanzado el ejemplo.

### a. Requisitos previos

- Python 3.10 o más reciente (la máquina tiene Python 3.12.10).
- Windows 11. Se recomienda una GPU NVIDIA con CUDA y unos 24 GB de VRAM; la CPU funciona pero es lenta y necesita unos 24 GB de RAM.
- Opcional: WSL 2 con Ubuntu, si prefieres herramientas de Linux.

### b. Entorno virtual

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

WSL (Ubuntu):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### c. Instalación

Instala primero PyTorch, eligiendo la versión con CUDA que corresponda a tu GPU desde https://pytorch.org (el `pip install torch` por defecto puede no usar la GPU).

```powershell
python -m pip install --upgrade pip
pip install torch
```

Después, las librerías de Hugging Face:

```powershell
pip install "transformers>=4.51.0" accelerate
```

`accelerate` es necesario para `device_map="auto"`.

### d. Ejemplo mínimo

Guárdalo como `run_qwen3.py` en una carpeta fuera del proyecto (por ejemplo, en la carpeta scratchpad), no en el entorno global de Python:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen3-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
)

messages = [{"role": "user", "content": "Give me a short introduction to large language models in two sentences."}]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,  # sin bloque de razonamiento: respuesta más corta
)
inputs = tokenizer([text], return_tensors="pt").to(model.device)

output_ids = model.generate(**inputs, max_new_tokens=128)
new_tokens = output_ids[0][len(inputs.input_ids[0]):]
print(tokenizer.decode(new_tokens, skip_special_tokens=True).strip())
```

Ejecútalo:

```powershell
python run_qwen3.py
```

La ficha del modelo no tiene acceso restringido, así que no hace falta token de Hugging Face. Si tienes uno (para descargas más rápidas o límites de peticiones), configúralo en la shell y nunca en el código:

```powershell
$env:HF_TOKEN = "<tu-token>"
```

### e. Comprobación

El resultado esperado son dos frases sobre modelos de lenguaje impresas en consola, sin etiquetas `<think>`, porque el ejemplo desactiva el pensamiento. Si la salida está vacía o el proceso se queda sin memoria, revisa los avisos de abajo.

### f. Avisos

- **Tamaño de la descarga:** unos 16,4 GB en BF16, guardados en la caché de Hugging Face (`%USERPROFILE%\.cache\huggingface`).
- **Licencia:** Apache 2.0. No hace falta aceptar ninguna condición en Hugging Face.
- **Hardware:** el ejemplo funciona en CPU pero es lento. En GPU necesita unos 24 GB de VRAM en BF16; con menos VRAM, carga una versión cuantizada.
- **Modo de pensamiento:** viene activado por defecto y genera salidas largas. Pon `max_new_tokens` alto (la ficha sugiere 32.768) si usas ese modo.

---

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Parámetros | 8,2 B (8.190.735.360 en los metadatos safetensors BF16) | Ficha; API de HF `safetensors.parameters` | Sí |
| Parámetros sin embeddings | 6,95 B | Ficha | Sí |
| Capas / atención | 36 capas; 32 cabezas Q / 8 KV (GQA) | Ficha | Sí |
| Contexto | 32.768 nativo; 131.072 con YaRN | Ficha | Sí |
| Licencia | Apache 2.0 | Metadatos de la ficha y enlace a LICENSE | Sí |
| Librería | `transformers` ≥ 4.51.0 | Ficha | Sí |
| Tamaño de pesos | ≈ 16,38 GB (suma de 5 shards; 15,26 GiB) | API de HF `?blobs=true` | Sí |
| Hardware (BF16) | ≈ 19,7–21,3 GB con margen | Cálculo: 8,19 B × 2 B + 20–30 % | **Estimación** |
| Hardware (INT8 / INT4) | ≈ 10 GB / ≈ 5 GB | Cálculo: 8,19 B × 1 B / 0,5 B + margen | **Estimación** |
| Descargas / me gusta | 7.000.357 / 2.170 | API de HF, snapshot 2026-11-06 | Sí (snapshot) |
| Acceso restringido | No | API de HF `gated: false` | Sí |
| Autor | Qwen Team | Cita de la ficha; arXiv:2505.09388 | Sí |
| Organización | Alibaba (mencionada en la ficha) | Ficha | Parcial: redacción de la afiliación pendiente |
| Fecha de publicación | No indicada en la ficha | — | **Pendiente** |
| Comandos de "Cómo ejecutarlo" | Nombres de paquete comprobados en PyPI: `transformers` (5.22.1 la última; 4.51.0+ disponible), `accelerate` (1.15.0), `torch` (2.15.0) | `pip index versions` | Nombres sí; **no ejecutados** |

## Pendiente

- Fecha de publicación de Qwen3 (abril de 2025 es de memoria; la ficha no la confirma).
- Confirmar la redacción de la afiliación con Alibaba en el informe técnico.
- Ejecutar "Cómo ejecutarlo" en este equipo y registrar el entorno (GPU, Python, versión de transformers) antes de cambiar el estado a probado.
- Verificar las cifras de hardware midiendo la VRAM pico en BF16 y en 4 bits.
- La ficha pide `transformers` ≥ 4.51.0 y la última en PyPI es 5.22.1; comprobar qué versión necesita el ejemplo (el argumento `torch_dtype` podría cambiar en versiones nuevas).
