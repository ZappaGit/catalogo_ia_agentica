# 004 · all-MiniLM-L6-v2

**Fuente principal:** https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
**Licencia:** Apache 2.0
**Consultado:** 2026-11-08
**Código:** 02-NU-S-004 (catálogo 02 Embeddings y RAG · NU · Starter)
**Origen:** catálogo del vault `IA_Agentica/HuggingFace`, tabla "Top 10 global por descargas" (snapshot 2026-11-05), primer puesto por descargas. No es un modelo de generación de texto ni de voz, por eso se eligió para este hueco.
**Familias:** Starter · NU · Embeddings · Encoder (embeddings) · línea sentence-transformers (ver sección "Familias")

---

## Texto de LinkedIn

El modelo más descargado de nuestro snapshot de Hugging Face, y no escribe ni habla: convierte una frase en una lista de 384 números.

all-MiniLM-L6-v2 es un modelo de embeddings con 23 millones de parámetros. Asigna a una frase o a un párrafo corto un vector, de forma que los textos de significado parecido quedan cerca unos de otros. Es de código abierto, con licencia Apache 2.0.

🔧 **Tipo y tecnología:** embeddings de frases. Transformer solo codificador con 6 capas (la ficha no lo indica; ver Pendiente), pooling por media y normalización L2 de la salida. Implementado en Python sobre PyTorch.
📏 **Tamaño:** 22,7 M de parámetros, vectores de 384 dimensiones, entrada truncada a 256 piezas de palabra (word pieces). El repositorio ocupa unos 1,8 GB porque guarda varios formatos (safetensors, ONNX, OpenVINO, TensorFlow, Rust), pero el modelo en sí es pequeño.
💻 **Hardware mínimo:** cualquier CPU con unos 0,2 GB de RAM *(estimación nuestra; la ficha del modelo no lo indica)*.
🛠️ **Interfaces:** Python con `sentence-transformers` (`model.encode(frases)`), `transformers`, y runtimes de ONNX, OpenVINO o Rust; la ficha también lista text-embeddings-inference.
👥 **Quién lo usa y para qué:** la ficha no nombra empresas ni proyectos. Indica que los vectores sirven para recuperación de información, clustering y similitud de frases. Sus 178.968.052 descargas (a 2026-11-08) son la principal prueba de uso amplio.
💡 **Por qué importa:** es muy pequeño y funciona en la CPU de un portátil, así que se puede montar una búsqueda semántica o un prototipo de RAG sin GPU. Los modelos de embeddings más grandes suelen dar mejor calidad, a cambio de más memoria y tiempo *(lectura nuestra, no un benchmark de la ficha)*.
🏢 **Detrás del modelo:** el espacio `sentence-transformers` en Hugging Face. La ficha dice que se desarrolló durante una semana comunitaria de Hugging Face, con JAX/Flax, hardware TPU y apoyo del equipo de JAX y Cloud de Google.
🤓 **Curiosidad:** la ficha lista 1.170.060.424 pares de entrenamiento, y la fuente más grande son unos 726 millones de comentarios de Reddit. El modelo se entrenó para una tarea de similitud, no para escribir texto.

Ficha del modelo: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

#Embeddings #AI #OpenSource

---

## Qué es

all-MiniLM-L6-v2 es un **modelo de embeddings** (embeddings de frases). No genera texto: lee una frase y devuelve un vector de longitud fija de 384 números. Dos frases de significado parecido producen vectores que apuntan en direcciones parecidas, lo que se mide con la similitud coseno.

Según la ficha, es un codificador de frases y de párrafos cortos. Sus usos previstos son la recuperación de información, el clustering y la similitud de frases.

## Tipo y tecnología

- **Tarea:** embeddings de frases (extracción de características / similitud de frases; `pipeline_tag: sentence-similarity` en la API).
- **Arquitectura:** transformer solo codificador, derivado de `nreimers/MiniLM-L6-H384-uncased` (ficha). La ficha no indica el número de capas; el nombre del modelo base sugiere 6 capas, que es la "L6" del nombre, pero no se ha comprobado en `config.json`.
- **Pooling:** media (mean pooling) sobre las salidas de los tokens, usando la máscara de atención, seguida de normalización L2 (el ejemplo de Transformers de la ficha usa `mean_pooling` y `F.normalize(..., p=2, dim=1)`).
- **Tokenizador:** WordPiece, sin distinguir mayúsculas (el repositorio contiene `vocab.txt`).
- **Entrenamiento:** parte del modelo base preentrenado y se afina con un objetivo contrastivo: similitud coseno entre todos los pares del lote, con pérdida de entropía cruzada frente a los pares verdaderos. La ficha indica hardware TPU v3-8, 100 k pasos, tamaño de lote 1024, tasa de aprendizaje 2e-5 con AdamW y longitud de secuencia 128 durante el entrenamiento.
- **Lenguaje de implementación:** Python, sobre PyTorch a través de `sentence-transformers`. El repositorio incluye además exportaciones a TensorFlow, ONNX, OpenVINO y Rust (`rust_model.ot`).

## Tamaño

- **Parámetros:** 22.713.728 según la API (tensores `safetensors`: 22.713.216 F32 + 512 I64). La página de la ficha muestra "22.7M params".
- **Dimensión de salida:** 384.
- **Longitud de entrada:** la ficha indica que, por defecto, el texto de más de 256 piezas de palabra se trunca. El entrenamiento usó 128 tokens.
- **Formato:** safetensors (F32). La API no da el tamaño en bytes de `model.safetensors`; el almacenamiento total del repositorio es 1.845.474.494 bytes (unos 1,8 GB, con todos los formatos).

## Hardware mínimo

| Precisión | Pesos | Con margen | Referencia |
|-----------|-------|------------|------------|
| FP32 (como se publica) | 22,7 M × 4 B ≈ 91 MB | ≈ 0,15–0,2 GB | Cualquier CPU con 1 GB de RAM |
| FP16 / INT8 | ≈ 45 MB / ≈ 23 MB | < 0,1 GB | No medido; no se ha analizado ninguna variante cuantizada |

El margen cubre el runtime, el tokenizador y las activaciones de un lote de frases. Son estimaciones; no se ha hecho ninguna medición en la máquina de referencia.

## Interfaces

- `sentence-transformers` (`SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')` y después `encode`), el ejemplo de uso de la ficha.
- `transformers` (`AutoTokenizer`, `AutoModel`, con mean pooling explícito).
- Exportaciones a ONNX, OpenVINO, Rust y TensorFlow que lista la ficha; text-embeddings-inference aparece en las etiquetas.
- Las etiquetas de despliegue para endpoints de SageMaker y Azure aparecen en el modelo; no se han explorado.

## Quién lo usa y para qué

- La ficha no nombra empresas, productos ni artículos que lo usen.
- Cifra de popularidad (consultada el 2026-11-08): 178.968.052 descargas y 6.079 "me gusta" en Hugging Face (API). El snapshot del vault del 2026-11-05 da 180,2 M descargas; la diferencia es el tiempo entre las dos lecturas. Las descargas son acumulativas y favorecen a los modelos antiguos, así que miden alcance, no calidad.
- Usos típicos según la ficha: búsqueda semántica, agrupación de textos y similitud de frases. El catálogo del vault lista un reranker cross-encoder (`ms-marco-MiniLM-L6-v2`) entre las descargas más altas, que es el complemento habitual para reordenar resultados (lectura nuestra del catálogo, no una afirmación de esta ficha).

## Por qué importa

Es el tipo más pequeño de modelo de embeddings útil: 22,7 M de parámetros, 384 dimensiones y velocidad apta para CPU. Por eso es un punto de partida común para probar una búsqueda semántica o un pipeline de RAG (documentos, vectores, vecinos más cercanos) antes de elegir un modelo más grande. Frente a los modelos de embeddings multilingües más grandes del mismo catálogo (por ejemplo BGE-M3), es un modelo centrado en inglés, con entrada más corta y mucho más pequeño *(lectura nuestra de las fichas, no un benchmark)*.

## Detrás del modelo

- **Organización:** el espacio `sentence-transformers` en Hugging Face. La ficha dice que el modelo se desarrolló durante una semana comunitaria de Hugging Face, con 7 TPU v3-8 y apoyo de los equipos de JAX, Flax y Cloud de Google.
- **Autores:** la ficha no incluye nombres de autores individuales.
- **Modelo base:** `nreimers/MiniLM-L6-H384-uncased`, citado como punto de partida en la ficha.

## Curiosidades

- Los datos de entrenamiento son muy grandes y muy variados: la tabla de la ficha suma 1.170.060.424 pares. Las fuentes principales son comentarios de Reddit (2015–2018, unos 726 millones de pares), pares de citas de S2ORC (unos 116 millones), preguntas duplicadas de WikiAnswers (unos 77 millones) y pares pregunta–respuesta de PAQ (unos 64 millones).
- El modelo no tiene cabeza generativa: no puede responder una pregunta, solo devolver un vector que se puede comparar con otros vectores.

---

## Familias

| Familia | Valor | Motivo |
|---------|-------|--------|
| Grupo (arquitectura) | Encoder (embeddings) | Transformer solo codificador; produce un vector por entrada, sin generar tokens. |
| Categoría | Starter | Modelo pequeño, fácil de ejecutar en una máquina modesta y de probar un pipeline de recuperación. |
| Tier (parámetros) | NU (< 1 B) | 22,7 M de parámetros. |
| Tipo (modalidad) | Embeddings | Entrada de texto, salida de vector. |
| Línea evolutiva | Línea sentence-transformers (base MiniLM → all-MiniLM-L6-v2) | El modelo es un fine-tune de `nreimers/MiniLM-L6-H384-uncased`. Otros miembros de la línea (por ejemplo `all-MiniLM-L12-v2`) son hermanos, no evoluciones; no comprobado en este artículo. |
| Ditto | No asignado | La ficha no lo presenta como base general para fine-tuning; ya está entrenado para similitud. |

---

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Parámetros | 22,7 M (22.713.728) | API de HF, `safetensors.parameters`; ficha "22.7M params" | Sí |
| Licencia | Apache 2.0 | YAML de la ficha (`license: apache-2.0`) | Sí |
| Dimensión de salida | 384 | Ficha ("384 dimensional dense vector space") | Sí |
| Truncamiento de entrada | 256 piezas de palabra por defecto | Ficha, "Intended uses" | Sí |
| Longitud de secuencia de entrenamiento | 128 tokens | Ficha, hiperparámetros de entrenamiento | Sí |
| Pooling y normalización | Mean pooling + normalización L2 | Código de ejemplo de la ficha | Sí |
| Número de capas | 6 (nombre "L6") | La ficha no lo indica; solo el nombre del base | **No**, ver Pendiente |
| Arquitectura | Transformer solo codificador, a partir de `nreimers/MiniLM-L6-H384-uncased` | Ficha | Sí |
| Librerías | sentence-transformers, transformers, ONNX, OpenVINO, Rust, TF, TEI | Ficha y etiquetas | Sí |
| Datos de entrenamiento | 1.170.060.424 pares; Reddit ≈ 726 M | Tabla de la ficha | Sí |
| Hardware de entrenamiento | 7 TPU v3-8 (semana comunitaria) | Ficha | Sí |
| Organización | Espacio `sentence-transformers`; semana comunitaria de Hugging Face | Ficha | Sí |
| Descargas / me gusta | 178.968.052 / 6.079 | API de HF, 2026-11-08 | Sí (snapshot) |
| Descargas en el vault | 180,2 M | Catálogo del vault, snapshot 2026-11-05 | Sí (otro snapshot) |
| Almacenamiento del repositorio | 1.845.474.494 bytes | API de HF, `usedStorage` | Sí |
| Tamaño de `model.safetensors` en bytes | No disponible | La API de HF no da tamaños por archivo | **No**, ver Pendiente |
| Acceso restringido | No | API de HF, `gated: false` | Sí |
| Hardware (FP32) | ≈ 0,15–0,2 GB | Cálculo: 22,7 M × 4 B + margen | **Estimación** |
| Categoría Starter | Criterio de la serie (`CLAUDE.md`) | Clasificación propia | Propuesta |
| Tier NU | < 1 B según `CLAUDE.md` | Clasificación propia | Sí |

## Pendiente

- **Número de capas:** la ficha no lo indica. Revisar `config.json` del repositorio (o la pestaña Files) antes de publicar "6 capas".
- **Tamaño en bytes de `model.safetensors`:** la API no da tamaños por archivo. Revisar la pestaña Files.
- **Hardware medido:** ejecutar el ejemplo en la máquina de referencia y anotar la memoria antes de cambiar el estado a `probado`.
- **Quién lo usa:** la ficha no nombra proyectos. Cualquier afirmación sobre usuarios concretos necesita una fuente fuera de la ficha.
- **Comparación de calidad con modelos de embeddings más grandes:** la frase de "Por qué importa" es lectura nuestra; debería respaldarse con un benchmark (por ejemplo MTEB) antes de presentarla como hecho.
- **Detalles de la semana comunitaria:** la ficha solo da la descripción del evento; no indica fecha de publicación.
