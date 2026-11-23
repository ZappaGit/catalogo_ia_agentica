# Fundamentos de LLM

Textos de apoyo sobre cómo funcionan los modelos de lenguaje, en general y sin depender de un modelo concreto. Son material interno para preparar los artículos de la serie (`posts/`), no son publicaciones.

Idioma: español. Cada tema lleva su fecha de consulta y sus fuentes.

## Índice

1. [Tokenización](01-tokenizacion.md): cómo se pasa de texto a IDs, qué entra y qué sale, algoritmos (BPE, Unigram, WordPiece, SentencePiece) y un ejemplo real con Qwen3-8B.
2. [Tokens, límites y razonamiento](02-limites-y-razonamiento.md): qué hace `max_new_tokens`, por qué una respuesta puede salir cortada y qué es el bloque `<think>`, con las pruebas de `lab-llm/`.
3. [Desplegar un LLM e integrarlo](03-despliegue-e-integracion.md): opciones de despliegue (transformers, Ollama, llama.cpp, vLLM, SGLang), cómo llamarlo desde código, integración con embeddings, herramientas y visión, y el paso texto → TTS (Kokoro).
4. [Herramientas para desplegar](04-herramientas-de-despliegue.md): ficha de cada herramienta (licencia, instalación, arranque de Qwen3, puerto, hardware) y cómo elegir una.

## Archivos de apoyo

- [demo_tokenizacion.py](demo_tokenizacion.py): script que muestra los tokens e IDs de varias frases con el tokenizador de Qwen3-8B. Requiere `tokenizers`.

## Pendiente de hacer

- Embeddings y transformer como fases separadas (hoy están resumidos en el glosario y en el artículo 002).
- Muestreo (temperatura, top-p, top-k) con ejemplos numéricos.
