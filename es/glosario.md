# Glosario · IA 365 modelos

Explicaciones de los términos que aparecen en los artículos de la serie. Cada término enlaza a los artículos donde se usa.

Artículos: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md) · [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md) · [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md) · [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md) · [005 · llama.cpp](posts/005-01-NU-S-llama-cpp.md) · [006 · OpenClaw](posts/006-01-NU-S-openclaw.md) · [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md) · [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md) · [009 · Z-Image-Turbo Q4](posts/009-05-UU-P-z-image-turbo-q4.md) · [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md) · [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

---

## Audio y voz

### TTS (Text-to-Speech)
Convertir texto escrito en voz hablada. Entrada: texto. Salida: archivo de audio.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md)

### ASR (Automatic Speech Recognition)
El proceso inverso al TTS: convertir voz en texto. Whisper es un ejemplo.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md) (como contraste) · [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

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
Representación del sonido como intensidad de cada frecuencia a lo largo del tiempo. Es la "imagen" intermedia que muchos modelos de voz generan antes de llegar a la onda de audio. Whisper hace lo contrario: convierte el audio en un espectrograma log-Mel (frecuencias en la escala Mel, más cercana al oído humano) y lee el texto a partir de él.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md) · [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

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

### Codificador-decodificador (sequence-to-sequence)
Un Transformer con dos partes: el codificador lee toda la entrada (en Whisper, 30 segundos de audio) y el decodificador escribe la salida token a token mientras la consulta. Whisper large-v3-turbo mantiene 32 capas de codificador y recorta el decodificador a 4.
Aparece en: [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

### RTF (factor de tiempo real)
Tiempo de procesamiento dividido entre la duración del audio. Por debajo de 1, el sistema va más rápido que el tiempo real; 1 significa que tarda lo mismo que dura el audio.
Aparece en: [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

### Alucinación (en reconocimiento de voz)
Texto de una transcripción que nunca se dijo en el audio. La ficha de Whisper lo atribuye al entrenamiento con grandes cantidades de datos ruidosos.
Aparece en: [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

### Poda (pruning)
Quitar partes de un modelo ya entrenado (capas, neuronas) para hacerlo más pequeño y rápido, normalmente seguido de más entrenamiento para recuperar calidad. Whisper large-v3-turbo es un large-v3 podado.
Aparece en: [011 · Whisper large-v3-turbo](posts/011-04-NU-P-whisper-large-v3-turbo.md)

### Modelado físico (síntesis articulatoria)
Crear una voz simulando el cuerpo que la produce (pulmones, cuerdas vocales, garganta, lengua, labios, nariz) en lugar de reproducir grabaciones o aprender de datos. Cada control tiene un significado físico, como la posición de la lengua.
Aparece en: [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md)

### Tracto vocal y glotis
La **glotis** es la abertura entre las cuerdas vocales; al abrirse y cerrarse produce el zumbido de la voz. El **tracto vocal** es el tubo que hay encima (garganta, boca, nariz), cuya forma filtra ese zumbido en vocales y consonantes.
Aparece en: [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md)

### Formante
Una resonancia del tracto vocal: una banda de frecuencias que la forma del tracto refuerza. Los dos primeros formantes son los que distinguen una vocal de otra.
Aparece en: [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md)

### FDTD (diferencias finitas en el dominio del tiempo)
Método numérico que simula una onda paso a paso en el tiempo y el espacio. CHIMERA lo usa para calcular la presión y el flujo de aire a lo largo de las secciones del tracto vocal.
Aparece en: [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md)

### WebAssembly y AudioWorklet
**WebAssembly** (wasm) es un formato de código compilado que los navegadores ejecutan a velocidad casi nativa. Un **AudioWorklet** es el hilo de audio en tiempo real del navegador; necesita un contexto seguro (HTTPS o localhost).
Aparece en: [010 · CHIMERA](posts/010-04-NU-B-chimera-vocal-synth.md)

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
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md), [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md) · [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Thinking mode (modo de razonamiento)
El modelo genera un bloque de razonamiento antes de la respuesta. Da mejores resultados en matemáticas y código, pero produce salidas más largas y lentas. Qwen3 permite activarlo o desactivarlo.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Chat template
Plantilla que convierte la lista de mensajes (usuario, asistente, sistema) en el formato de tokens especiales que el modelo espera.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

---

## Fases de generación de una respuesta

Orden en que ocurren las fases al generar una respuesta. Cada entrada remite al diagrama de [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno).

1. Plantilla de chat → 2. Tokenización → 3. Embedding → 4. Bloques transformer (cada uno con 8 pasos internos, ver abajo) → 5. Logits → 6. Muestreo → 7. Fin o nuevo token.

### Plantilla de chat (fase 1)
Antes de tokenizar, la lista de mensajes se convierte en un único texto con las etiquetas de rol del modelo. Con `enable_thinking=False`, la plantilla añade un bloque `<think>` vacío para que el modelo responda directamente.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### Tokenización (fase 2)
Paso que convierte el texto en una lista de IDs de tokens, usando el vocabulario del tokenizador (151.669 entradas en Qwen3-8B). Es el mismo paso que hace el tokenizador antes de que el modelo vea nada. Ver [fundamentos-llm/01-tokenizacion.md](fundamentos-llm/01-tokenizacion.md).
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### Embedding (fase 3)
Tabla que cambia cada ID de token por un vector de números (4.096 valores en Qwen3-8B). Es lo primero que recibe el modelo.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### Bloque transformer (fase 4)
Cada bloque aplica las mismas operaciones, una tras otra. Qwen3-8B tiene 36 bloques, así que el vector de cada token pasa por todos ellos. Dentro de cada bloque:
1. **RMSNorm**: normaliza el vector antes de la atención.
2. **Proyecciones Q, K y V**: crean la consulta, la clave y el valor de cada token.
3. **QK-Norm**: normaliza Q y K de cada cabeza antes de comparar.
4. **RoPE**: codifica la posición del token dentro del vector de Q y K.
5. **Atención causal con caché KV**: cada token mira solo a los anteriores (ver las entradas siguientes).
6. **Conexión residual**: suma la entrada del bloque a la salida de la atención.
7. **RMSNorm** y **MLP SwiGLU**: un segundo bloque de cálculo, con una puerta que decide cuánta información pasa.
8. **Conexión residual**: suma otra vez, y el resultado es la entrada del bloque siguiente.

Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### RMSNorm
Normalización que escala cada vector por su raíz media cuadrática, sin restar la media. Es más simple que LayerNorm y se usa antes de cada subcapa de atención y de MLP.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### QK-Norm
Normalización extra que aplica RMSNorm a la consulta (Q) y a la clave (K) de cada cabeza. Ayuda a que el producto que mide la atención no se dispare en modelos grandes. Qwen3 la incluye en su implementación.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### RoPE (Rotary Position Embedding)
Forma de codificar la posición girando los pares de valores de Q y K según el número de token. La base usada en Qwen3-8B es theta = 1.000.000. Así el modelo sabe qué token va antes que otro sin necesitar una tabla de posiciones.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### Atención causal
Atención en la que cada token solo puede mirar a sí mismo y a los tokens anteriores, nunca a los siguientes. Es lo que permite generar texto de izquierda a derecha. Se calcula comparando la consulta del token actual con las claves de todos los anteriores, y usando el resultado para mezclar sus valores.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### Conexión residual
Suma la entrada de un bloque a su salida. La señal original sigue llegando a las capas profundas, y así se puede entrenar un modelo de 36 bloques.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### MLP SwiGLU
Parte del bloque que transforma cada vector token a token, sin mirar a otros tokens. Usa tres matrices: sube de 4.096 a 12.288 valores, multiplica dos caminos (uno pasado por SiLU, que hace de puerta) y vuelve a bajar a 4.096. En Qwen3-8B, SwiGLU es la forma del MLP.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### Prefill y decode
Dos modos de cálculo. En **prefill** el modelo procesa de una vez todos los tokens de la entrada y rellena la caché KV. En **decode** genera un token nuevo cada vez, usando la caché. La velocidad en tokens por segundo se mide sobre todo en la fase decode.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### LM head y logits (fase 5)
Última capa lineal: convierte el vector final de cada token en un número (logit) por cada token del vocabulario. Un logit alto indica que ese token es probable como siguiente. En Qwen3-8B, la capa tiene 151.936 salidas y no comparte pesos con el embedding.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### Muestreo: temperatura, top-p y top-k (fase 6)
Forma de elegir el siguiente token a partir de los logits:
- **Temperatura**: escala los logits. Valores bajos hacen la elección más conservadora; valores altos, más variada. La ficha de Qwen3 recomienda 0,6 en modo pensamiento.
- **Top-k**: solo se consideran los k tokens con logit más alto (20 en la recomendación de Qwen3).
- **Top-p**: se consideran los tokens más probables hasta que su probabilidad acumulada llega a p (0,95 en la recomendación de Qwen3).

La ficha pide no usar decodificación voraz (greedy), que elige siempre el token con mayor logit.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### Token de fin (EOS) (fase 7)
Token especial que indica que la respuesta ha terminado. Si el modelo lo genera, el bucle para. Si no, el token elegido se añade al contexto y se repite el proceso desde el embedding.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

### Decodificación
Último paso: convierte la lista de IDs generados de nuevo en texto. Con `skip_special_tokens=True` se quitan los tokens especiales, pero el texto de un bloque `<think>` se conserva.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md#proceso-interno)

---

## Modelos y pesos

### Parámetros
Números que el modelo aprende durante el entrenamiento. "82 M" significa 82 millones; "8,2 B" significa 8.200 millones. Más parámetros suelen significar más capacidad y más memoria necesaria.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Parámetros sin embeddings
Parámetros del modelo sin contar la tabla de embeddings (la que convierte tokens en vectores). Es una cifra más representativa de la parte "de razonamiento" del modelo cuando el vocabulario es grande. En Qwen3-0.6B, 0,44 B de 0,6 B.
Aparece en: [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md) · [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

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
Reducir la precisión de los pesos (por ejemplo, de BF16 a INT4) para que el modelo quepa en menos memoria. Nombres como Q8_0 o Q4_K_M indican el esquema de cuantización de un archivo GGUF.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md) · [005 · llama.cpp](posts/005-01-NU-S-llama-cpp.md) · [009 · Z-Image-Turbo Q4](posts/009-05-UU-P-z-image-turbo-q4.md)

### GGUF
Formato de archivo para guardar modelos cuantizados, con los pesos y los metadatos necesarios para ejecutarlos. Es el formato que lee llama.cpp.
Aparece en: [005 · llama.cpp](posts/005-01-NU-S-llama-cpp.md) · [009 · Z-Image-Turbo Q4](posts/009-05-UU-P-z-image-turbo-q4.md)

### Hardware: VRAM y RAM
- **VRAM**: memoria de la tarjeta gráfica. Es la que más rápido mueve los pesos.
- **RAM**: memoria del sistema. Permite ejecutar el modelo en CPU, pero es mucho más lento.
Aparece en: [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Estimación de hardware
Fórmula usada en la serie: memoria de pesos ≈ parámetros × bytes por parámetro, más un margen del 20–30 % para contexto y activaciones. Es una aproximación; la medida real depende del entorno.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

---

## Embeddings y similitud

### Embedding de frase (sentence embedding)
Vector de longitud fija que representa el significado de una frase o de un texto corto. Textos de significado parecido obtienen vectores cercanos entre sí. Es la salida de modelos de embeddings como all-MiniLM-L6-v2 (384 valores).
Aparece en: [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Similitud coseno (cosine similarity)
Medida de cuánto apuntan en la misma dirección dos vectores, de -1 (opuestos) a 1 (misma dirección). Es la forma habitual de comparar embeddings de frases.
Aparece en: [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Mean pooling
Convertir los vectores de todos los tokens en un único vector de frase haciendo su media, ignorando el relleno (con la máscara de atención). Lo usa all-MiniLM-L6-v2.
Aparece en: [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Entrenamiento contrastivo (contrastive training)
Entrenamiento que enseña al modelo a acercar los vectores de los pares que casan (por ejemplo, una pregunta y su respuesta) y a alejar los de los pares que no casan dentro del mismo lote.
Aparece en: [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Solo codificador (encoder-only)
Transformer que lee la entrada completa y produce una representación de ella, sin generar texto token a token (a diferencia de un modelo decoder-only). BERT y all-MiniLM-L6-v2 son de este tipo.
Aparece en: [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

---

## Otros conceptos

### Difusión (diffusion)
Método generativo que parte de ruido y lo refina en varios pasos hasta obtener el resultado. Se usa en generación de imágenes y, en algunos TTS, para el estilo de la voz. Kokoro no lo usa.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md) · [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md) · [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md)

### DiT (Diffusion Transformer)
Modelo de difusión cuyo denoiser es un transformer en lugar de una red convolucional. Los tokens del texto y de la imagen pasan por el transformer, que predice el ruido que se quita en cada paso.
Aparece en: [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md)

### Destilación (distillation)
Entrenar un modelo más pequeño o rápido (el alumno) para reproducir el resultado de uno más grande (el maestro) con menos pasos o menos cálculo. Z-Image-Turbo se destila del modelo base Z-Image, de 50 pasos, a 8 pasos.
Aparece en: [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md)

### Guidance (classifier-free guidance, CFG)
Ajuste que hace que la imagen siga más de cerca el texto. Suele necesitar una segunda pasada del modelo en cada paso; el modelo Turbo, destilado, funciona con guidance 0, así que no necesita esa pasada.
Aparece en: [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md)

### VAE (variational autoencoder)
Red que comprime la imagen en una representación latente más pequeña y la descomprime de vuelta a píxeles. El modelo de difusión trabaja en ese espacio comprimido, lo que ahorra memoria y tiempo.
Aparece en: [007 · Z-Image-Turbo](posts/007-05-UU-P-z-image-turbo.md)

### Difusión latente (latent diffusion)
Difusión que trabaja en una representación comprimida (el latente) en lugar de en píxeles. Un VAE comprime la imagen antes de quitar el ruido y decodifica el resultado al final, lo que ahorra memoria y tiempo.
Aparece en: [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md)

### U-Net
Red convolucional con un codificador y un decodificador unidos por conexiones de salto. En Stable Diffusion 1.5 es el denoiser: en cada paso predice el ruido que hay que quitar.
Aparece en: [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md)

### CLIP (codificador de texto)
Codificador de texto entrenado para emparejar textos con imágenes. En Stable Diffusion 1.5 convierte el prompt en vectores que guían la eliminación de ruido.
Aparece en: [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md)

### stable-diffusion.cpp
Runtime de código abierto en C/C++ para modelos de difusión de imagen, con backend CPU, herramienta de línea de comandos y servidor HTTP. Es un runtime, no un modelo; los artículos 008 y 009 lo usan.
Aparece en: [008 · Stable Diffusion 1.5](posts/008-05-NU-S-stable-diffusion-1-5.md) · [009 · Z-Image-Turbo Q4](posts/009-05-UU-P-z-image-turbo-q4.md)

### llama.cpp
Motor de inferencia de código abierto en C/C++ que ejecuta modelos en formato GGUF, con una herramienta de línea de comandos y un servidor HTTP con API compatible con OpenAI. Es un runtime, no un modelo.
Aparece en: [005 · llama.cpp](posts/005-01-NU-S-llama-cpp.md) (también en [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md) y [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md) como opción para ejecutar el modelo)

### Gateway (proceso de control)
Programa local que se mantiene en ejecución y gestiona sesiones, herramientas, eventos y las conexiones con el exterior (por ejemplo, canales de mensajería). En OpenClaw, el Gateway es el plano de control; la Control UI, la CLI y la TUI se conectan a él. No es un modelo.
Aparece en: [006 · OpenClaw](posts/006-01-NU-S-openclaw.md)

### Familias (serie IA 365 modelos)
Clasificación propia de la serie, inspirada en cómo se agrupan los Pokémon: grupo (arquitectura), categoría (Starter, Legendary, etc.), tier según parámetros (NU, RU, UU, OU, Uber), tipo (modalidad) y línea evolutiva. Es un recurso de divulgación, no una clasificación oficial.
Aparece en: [003 · Qwen3-0.6B](posts/003-01-NU-S-qwen3-0-6b.md) · [004 · all-MiniLM-L6-v2](posts/004-02-NU-S-all-minilm-l6-v2.md)

### Model card
Ficha del modelo en Hugging Face, con descripción, uso, licencia y datos de entrenamiento. Es la fuente principal de los datos de la serie.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)

### Licencia Apache 2.0
Licencia permisiva que permite uso comercial, modificación y redistribución, con aviso de copyright. Es la que usan Kokoro y Qwen3-8B.
Aparece en: [001 · Kokoro-82M](posts/001-04-NU-S-kokoro-82m.md), [002 · Qwen3-8B](posts/002-01-UU-S-qwen3-8b.md)
