# Bases de datos vectoriales

**Consultado:** 2026-11-08
**Relacionado con:** [posts/004-02-NU-S-all-minilm-l6-v2.md](../posts/004-02-NU-S-all-minilm-l6-v2.md) (modelo de embeddings), [fundamentos-llm/03-despliegue-e-integracion.md](../fundamentos-llm/03-despliegue-e-integracion.md) (búsqueda semántica y RAG).

Este documento explica qué es un almacén de vectores y compara algunas opciones. Las licencias vienen de búsquedas en fuentes secundarias y de la documentación pública; cuando las fuentes se contradicen, se indica y queda pendiente de verificar en el repositorio oficial.

---

## 1. Qué hace una base vectorial

Un modelo de embeddings convierte cada texto en un vector (en all-MiniLM-L6-v2, 384 números). Una base vectorial:

1. **Guarda** los vectores de los documentos, junto con sus metadatos (título, fecha, origen).
2. **Busca** los vectores más cercanos a un vector de consulta, normalmente por similitud coseno o producto interno.
3. **Filtra** a veces por metadatos (por ejemplo, solo documentos de 2026 o de un cliente concreto).

Sin base vectorial también se puede buscar: basta con calcular la similitud contra todos los vectores en memoria. Con pocos miles de documentos eso funciona bien. La base vectorial se vuelve útil cuando hay muchos documentos, cuando hace falta persistencia o cuando hay varios usuarios o filtros.

### Búsqueda exacta y aproximada

- **Exacta:** compara con todos los vectores. Resultado perfecto, coste proporcional al número de documentos.
- **Aproximada (ANN):** usa un índice (HNSW, IVF, etc.) que sacrifica un poco de precisión por mucha velocidad. Es lo habitual con millones de vectores.

---

## 2. Comparativa

| Opción | Tipo | Licencia (según fuente) | Cuándo tiene sentido |
|--------|------|-------------------------|----------------------|
| **FAISS** (Meta) | Biblioteca en Python/C++, sin servidor | MIT (repositorio `facebookresearch/faiss`) | Prototipos, pruebas de rendimiento, búsqueda dentro de tu propio programa. No guarda metadatos de forma nativa. |
| **pgvector** | Extensión de PostgreSQL | PostgreSQL License según la mayoría de fuentes; una fuente indica MIT. **Verificar `LICENSE`.** | Si ya usas PostgreSQL: vectores y datos en la misma base, con SQL y filtros normales. |
| **Chroma** | Base vectorial embebida o servidor | Apache 2.0 (página oficial) | Prototipos y aplicaciones pequeñas o medianas. Puede funcionar embebida, en un solo nodo o distribuida. |
| **Qdrant** | Servidor (escrito en Rust), API REST y gRPC | Apache 2.0 | Producción con filtros complejos sobre metadatos y varios usuarios. |
| **Milvus** | Servidor distribuido | Apache 2.0 | Volúmenes muy grandes (millones o miles de millones de vectores) y despliegues en clúster. |
| **Weaviate** | Servidor con búsqueda vectorial y de texto | **Fuentes en conflicto:** BSD 3-Clause en una y Apache 2.0 en otra. **Verificar `LICENSE`.** | Aplicaciones que combinan búsqueda vectorial y por palabras clave. |

Las licencias son orientativas: la fuente es una búsqueda, no el archivo `LICENSE` de cada proyecto. Antes de usar una en un producto comercial hay que comprobar el archivo del repositorio y sus dependencias opcionales (por ejemplo, las de GPU de FAISS).

---

## 3. Qué elegir según el caso

- **Ya tienes PostgreSQL** (una app de gestión, un CRM propio): pgvector. Menos piezas que mantener.
- **Quieres probar en un portátil en una tarde:** Chroma o FAISS.
- **Necesitas un servicio dedicado con filtros y varios usuarios:** Qdrant.
- **Volumen enorme y clúster:** Milvus.
- **Búsqueda vectorial mezclada con búsqueda de texto:** Weaviate, tras verificar la licencia.

Estas recomendaciones son orientativas y no se han medido en este equipo.

---

## 4. Relación con el modelo de embeddings

- **Mismo modelo en indexación y en consulta.** Los vectores de dos modelos distintos no son comparables.
- **Dimensión fija.** all-MiniLM-L6-v2 produce 384 dimensiones; la columna o el índice deben declararse con esa dimensión.
- **Métrica.** Los vectores de all-MiniLM-L6-v2 se normalizan (L2), así que la similitud coseno coincide con el producto interno. Hay que elegir la misma métrica en la base y en el modelo.
- **Límite de entrada.** Los textos largos se truncan (256 tokens por defecto). Para documentos largos hay que trocearlos (chunking) antes de indexar.

---

## 5. Pendiente de verificar

- Licencia de pgvector: el archivo `LICENSE` del repositorio `pgvector/pgvector`.
- Licencia de Weaviate: el archivo `LICENSE` del repositorio oficial.
- Licencia del modo distribuido de Chroma: el repositorio `chroma-core/chroma`.
- Dependencias de FAISS con GPU (CUDA, cuVS): licencias propias, no revisadas.
- Probar al menos una opción (por ejemplo, FAISS o Chroma) con all-MiniLM-L6-v2 en `lab-llm/` o en una carpeta de pruebas, y anotar tiempos y memoria. Hasta entonces, todo lo anterior es descriptivo.

## Fuentes consultadas

- Repositorio y documentación de pgvector (búsqueda, 2026-11-08).
- Repositorio `facebookresearch/faiss` y su README (licencia MIT, 2026-11-08).
- Página oficial de Chroma (licencia Apache 2.0, 2026-11-08).
- DB-Engines y ODBMS.org para Qdrant, Milvus y Weaviate (2026-11-08). Las licencias de Qdrant y Milvus coinciden en las fuentes; la de Weaviate no.
