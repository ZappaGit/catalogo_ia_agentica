# IA 365 modelos

Serie de publicaciones en LinkedIn para divulgar modelos generativos: uno por día, aproximadamente.

## Objetivo

Explicar qué es cada modelo, con datos verificados, de forma que cualquiera lo entienda y pueda decidir si le sirve. Cada publicación sale de un artículo en esta carpeta.

## Qué se cuenta de cada modelo

1. **Qué es**: tipo (texto, imagen, vídeo, audio, multimodal, embeddings) y tarea principal.
2. **Tecnología**: arquitectura (transformer, difusión, MoE…), lenguaje de implementación y librerías.
3. **Tamaño**: parámetros, contexto máximo y formato de pesos.
4. **Hardware mínimo**: RAM/VRAM aproximada para ejecutarlo, con el método de cálculo indicado.
5. **Interfaces**: cómo se usa (API, Python, UI, CLI, ComfyUI…).
6. **Quién lo usa y para qué**: casos reales o proyectos conocidos.
7. **Por qué importa**: qué aporta frente a alternativas.
8. **Quién está detrás**: organización y autores.
9. **Curiosidades**.
10. **Pokémon**: asociación para el gancho visual (ver convención abajo).

## Convenciones

- **Verificación**: cada dato sale de la ficha del modelo en Hugging Face u otra fuente oficial, citada en el artículo. Lo que sea estimación se marca como estimación. Si algo no está verificado, se pone como pendiente.
- **Licencia**: se indica explícitamente, porque condiciona el uso comercial.
- **Fecha de snapshot**: los datos de descargas o popularidad cambian; se indica la fecha de consulta.
- **Idioma**: español.
- **Pokémon**: cada modelo recibe un Pokémon cuyo tipo o rasgo encaje con lo que hace el modelo (por ejemplo, un TTS puede ser un Pokémon "de voz"). La asociación es un recurso de divulgación; no implica relación oficial con The Pokémon Company ni con Nintendo. Pokémon es marca registrada de sus propietarios: no se usan sprites ni artes oficiales en las publicaciones, solo el nombre y la idea.
- **Formato LinkedIn**: un gancho en la primera línea, 4–6 bloques cortos, un dato de hardware destacado y un enlace a la ficha. Sin más de 3 hashtags.

## Código de identificación

Cada modelo tiene un código corto, `CC-TIER-FAM-NNN`, que se escribe en la cabecera del artículo, en la plantilla y en `indice.md`:

- **CC** (catálogo, dos dígitos): categoría del catálogo del vault, de `01` a `08` (01 Texto y LLMs, 02 Embeddings y RAG, 03 NLP clásico, 04 Voz y audio, 05 Imagen, vídeo y 3D, 06 Multimodal, 07 Series temporales, 08 Sin etiqueta).
- **TIER** (parámetros): `UB` ≥ 100 B, `OU` 14–100 B, `UU` 4–14 B, `RU` 1–4 B, `NU` < 1 B.
- **FAM** (familia): `S` Starter, `L` Legendary, `M` Mythical, `B` Ultra Beast, `P` Paradox.
- **NNN**: número del artículo. El nombre del archivo empieza por NNN, seguido del código y del slug del modelo.

Ejemplo: `01-UU-S-002` es Qwen3-8B (texto, 8,2 B, Starter).

## Estructura

- `README.md`: este documento.
- `plantilla.md`: plantilla para cada artículo.
- `indice.md`: calendario y estado de cada modelo.
- `posts/`: un archivo por modelo, con nombre `NNN-CC-TIER-FAM-slug-del-modelo.md`.

## Origen de los modelos

Se parte del catálogo del vault (`IA_Agentica/HuggingFace`), que lista los modelos más descargados del Hub. Los modelos de la serie se pueden elegir de ahí o de otras fuentes; cada artículo indica de dónde sale.

## Glosario

`glosario.md` explica los términos técnicos que aparecen en los artículos (TTS, ISTFTNet, GQA, KV cache, cuantización…), con enlaces a los artículos donde se usan. Hay que mantenerlo al añadir un artículo nuevo.

## Idioma

- Artículo completo (`posts/`): español, fuente de verdad.
- Versión para publicar (`catalogue/`): inglés, resumen del artículo completo.

## Equipo de trabajo

Equipo donde se ejecutan las pruebas de la serie (`lab-tts/` y los siguientes labs):

| Componente | Detalle |
|------------|---------|
| Equipo | Portátil con Windows 11 Home (10.0.26200) |
| CPU | Intel Core i7-1355U (13.ª generación), 10 núcleos y 12 hilos |
| RAM | 16 GB (15,7 GB utilizables), 3200 MHz |
| GPU | Intel UHD Graphics integrada, sin CUDA. Usa memoria compartida con la RAM del sistema |
| Disco | C: de 952,5 GB, con 528,8 GB libres (dato de la fecha de consulta) |
| Python | 3.12.10 (instalado en el sistema) |
| Git | 2.46.0 |

Consecuencias para los artículos:

- Todos los modelos de la serie que se prueben aquí corren en CPU. Los modelos de más de unos pocos miles de millones de parámetros no caben en la RAM disponible en BF16.
- El hardware mínimo que cite un artículo debe marcarse como **estimación** si no se ha medido en este equipo.
- Para modelos grandes (por ejemplo, Qwen3-8B), la prueba se hará con una versión más pequeña o cuantizada, o en otra máquina con GPU NVIDIA.
