# Glosario · IA 365 modelos

Explicaciones de los términos que aparecen en los artículos de la serie. Cada término enlaza a los artículos donde se usa.

Artículos: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md) · [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md) · [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md)

---

## Audio y voz

### TTS (Text-to-Speech)
Convertir texto escrito en voz hablada. Entrada: texto. Salida: archivo de audio.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### ASR (Automatic Speech Recognition)
El proceso inverso al TTS: convertir voz en texto. Whisper es un ejemplo.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md) (como contraste)

### Normalización de texto
Paso previo al TTS que convierte abreviaturas, números y símbolos en palabras ("Dr. 3" → "doctor tres").
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### G2P (grapheme-to-phoneme) y fonemas
G2P convierte cada palabra escrita en sus sonidos (fonemas). En Kokoro lo hace la librería `misaki`.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### Prosodia
Entonación, ritmo, pausas y énfasis de una frase. El módulo de prosodia de un TTS decide cómo suena una frase, no solo qué palabras dice.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### Espectrograma
Representación del sonido como intensidad de cada frecuencia a lo largo del tiempo. Es la "imagen" intermedia que muchos modelos de voz generan antes de llegar a la onda de audio.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### STFT e iSTFT
- **STFT** (transformada de Fourier de tiempo corto): pasa una señal de audio a espectrograma.
- **iSTFT**: la operación inversa, que pasa el espectrograma a audio.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### Vocoder
Módulo que convierte una representación intermedia (espectrograma o similar) en la forma de onda final.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### ISTFTNet
Vocoder que predice magnitud y fase de cada fragmento de sonido y usa la iSTFT para obtener el audio. Es más rápido que generar cada muestra de audio directamente.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### StyleTTS 2
Arquitectura de TTS publicada en 2023 (Li et al.). Tiene un codificador de texto, un módulo de prosodia, un módulo que genera el estilo de la voz y un decodificador.
Kokoro toma solo el decodificador y el enfoque ISTFTNet; no incluye el módulo de difusión ni el codificador publicado.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

---

## Arquitecturas de texto

### Transformer
Arquitectura que procesa secuencias de tokens con mecanismos de atención. Es la base de casi todos los LLM actuales.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Decoder-only
Variante de transformer que solo tiene la parte de generación. Produce texto un token cada vez, cada token depende de los anteriores. GPT y Qwen son de este tipo.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Token
Unidad mínima de texto que procesa el modelo. Puede ser una palabra, parte de una palabra o un símbolo. El contexto y la velocidad se miden en tokens.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Contexto (context window)
Cantidad máxima de tokens que el modelo puede tener en cuenta a la vez (entrada más respuesta). Qwen3-8B tiene 32.768 tokens nativos y hasta 131.072 con YaRN.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### GQA (Grouped-Query Attention)
Variante de atención en la que varias "cabezas" de consulta comparten las mismas claves y valores. Reduce la memoria que necesita el modelo al generar texto largo. Qwen3-8B usa 32 cabezas de consulta y 8 de clave/valor.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### KV cache
Memoria donde el modelo guarda las claves y valores de los tokens ya procesados para no recalcularlos. Crece con la longitud del contexto, por eso los textos largos necesitan más memoria aunque el modelo sea el mismo.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Soft switch (`/think` y `/no_think`)
Órdenes que se escriben en el mensaje del usuario para activar o desactivar el razonamiento de Qwen3 turno a turno. Solo funcionan si `enable_thinking=True`; con `enable_thinking=False` se ignoran.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md), [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md)

### Thinking mode (modo de razonamiento)
El modelo genera un bloque de razonamiento antes de la respuesta. Da mejores resultados en matemáticas y código, pero produce salidas más largas y lentas. Qwen3 permite activarlo o desactivarlo.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Chat template
Plantilla que convierte la lista de mensajes (usuario, asistente, sistema) en el formato de tokens especiales que el modelo espera.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

---

## Modelos y pesos

### Parámetros
Números que el modelo aprende durante el entrenamiento. "82 M" significa 82 millones; "8,2 B" significa 8.200 millones. Más parámetros suelen significar más capacidad y más memoria necesaria.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Parámetros sin embeddings
Parámetros del modelo sin contar la tabla de embeddings (la que convierte tokens en vectores). Es una cifra más representativa de la parte "de razonamiento" del modelo cuando el vocabulario es grande. En Qwen3-0.6B, 0,44 B de 0,6 B.
Aparece en: [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md)

### Pesos (weights)
Los valores concretos de los parámetros, guardados en un archivo. Ocupan la mayor parte de la memoria al ejecutar el modelo.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Safetensors
Formato de archivo para guardar pesos. Es más seguro que el formato antiguo de PyTorch porque no ejecuta código al cargarse.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Precisión: FP16, BF16, INT8 e INT4
Cuántos bits ocupa cada peso:
- **FP16 / BF16**: 16 bits (2 bytes). BF16 tiene el mismo rango que FP32, con menos precisión.
- **INT8**: 8 bits (1 byte).
- **INT4**: 4 bits (0,5 bytes).

Menos bits = menos memoria, con algo de pérdida de calidad.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Cuantización
Reducir la precisión de los pesos (por ejemplo, de BF16 a INT4) para que el modelo quepa en menos memoria.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Hardware: VRAM y RAM
- **VRAM**: memoria de la tarjeta gráfica. Es la que más rápido mueve los pesos.
- **RAM**: memoria del sistema. Permite ejecutar el modelo en CPU, pero es mucho más lento.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Estimación de hardware
Fórmula usada en la serie: memoria de pesos ≈ parámetros × bytes por parámetro, más un margen del 20–30 % para contexto y activaciones. Es una aproximación; la medida real depende del entorno.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

---

## Otros conceptos

### Difusión (diffusion)
Método generativo que parte de ruido y lo refina en varios pasos hasta obtener el resultado. Se usa en generación de imágenes y, en algunos TTS, para el estilo de la voz. Kokoro no lo usa.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### Familias (serie IA 365 modelos)
Clasificación propia de la serie, inspirada en cómo se agrupan los Pokémon: grupo (arquitectura), categoría (Starter, Legendary, etc.), tier según parámetros (NU, RU, UU, OU, Uber), tipo (modalidad) y línea evolutiva. Es un recurso de divulgación, no una clasificación oficial.
Aparece en: [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md)

### Model card
Ficha del modelo en Hugging Face, con descripción, uso, licencia y datos de entrenamiento. Es la fuente principal de los datos de la serie.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Licencia Apache 2.0
Licencia permisiva que permite uso comercial, modificación y redistribución, con aviso de copyright. Es la que usan Kokoro y Qwen3-8B.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)
