# 02 · Tokens, límites de generación y razonamiento

**Consultado:** 2026-11-08
**Base:** las pruebas de `lab-llm/` (Qwen3-0.6B y Qwen3-8B) y la tokenización de [01-tokenizacion.md](01-tokenizacion.md).

---

## 1. Qué es un token, en la práctica

Un token es un trozo de texto que el modelo lee o escribe de una vez. Puede ser una palabra corta, una parte de una palabra o un signo (ver [01-tokenizacion.md](01-tokenizacion.md)).

Dos consecuencias:
- Un texto en español gasta más tokens que el mismo texto en inglés.
- Los límites de un modelo se miden en tokens, no en palabras ni en caracteres.

## 2. Qué hace `max_new_tokens`

`max_new_tokens` es el **tope de tokens que el modelo puede escribir** en una respuesta. Es una orden de parada, no un objetivo de longitud.

- Si el modelo termina su respuesta antes del tope, para solo. Así pasó con el 8B: escribió 127 tokens y terminó la frase con normalidad.
- Si llega al tope, **para aunque la frase no haya acabado**. La respuesta se queda cortada. No es un error; el programa hace lo que se le pidió.

Por eso una respuesta puede parecer "truncada" aunque el modelo funcione bien. La solución es subir el tope, no cambiar el modelo.

## 3. Qué es el razonamiento (modo `thinking`)

Qwen3 puede trabajar en dos modos:

- **Sin razonamiento** (`enable_thinking=False`): responde directamente.
- **Con razonamiento** (`enable_thinking=True`, el valor por defecto): antes de responder escribe un bloque `<think>...</think>` con sus pasos. Ese bloque también cuenta como tokens.

Con razonamiento, el modelo puede gastar cientos de tokens pensando antes de escribir la primera palabra de la respuesta. Si el tope se alcanza dentro del bloque `<think>`, **la respuesta nunca aparece**.

El bloque `<think>` también sale en el texto decodificado. Si solo quieres la respuesta, hay que cortar el texto después de `</think>`.

## 4. Cómo se vio en nuestras pruebas

Mismo prompt en español, "Dime cual es el mayor logro de la humanidad, en 5 lineas", en el mismo equipo.

| Ejecución | Modo | Tope | Tokens escritos | Resultado |
|-----------|------|------|-----------------|-----------|
| 0,6 B (primera versión del script) | sin razonamiento | 128 | 128 | Cortada en la línea 5: "…la conc" |
| 0,6 B (primera versión del script) | con razonamiento | 256 | 256 | Cortada dentro de la respuesta: solo aparece la línea 1 |
| 0,6 B (versión actual) | sin razonamiento | 256 | 149 | Completa, 5 líneas |
| 0,6 B (versión actual) | con razonamiento | 1024 | 335 | Completa: bloque `<think>` y después 5 líneas |
| 8B | sin razonamiento | 128 | 127 | Completa, 5 líneas (terminó sola antes del tope) |

Lo que se ve en la tabla:
- La misma respuesta sin razonamiento necesita unos 150 tokens. Con 128 no alcanza.
- El razonamiento es mucho más largo que la respuesta: 335 tokens para 5 líneas. Con 256 se agota pensando.
- El tope afecta al resultado, pero no a la calidad del modelo. El mismo modelo da la respuesta completa cuando el tope es suficiente.

Nota: la primera versión del script (128 y 256) es la que se ejecutó al pegar la salida de arriba. El archivo `lab-llm/test_qwen3_06b_es.py` tiene ahora 256 y 1024.

## 5. Cómo leer el tiempo

Velocidad = tokens escritos ÷ segundos. En el 0,6 B, unos 5 tokens por segundo. Como el razonamiento escribe más tokens, tarda más en terminar, aunque la velocidad sea la misma.

En el 8B, con el modelo partido entre RAM y disco, la velocidad fue de unos 0,1 tokens por segundo. Una respuesta de 127 tokens tardó 2.078 segundos (unos 35 minutos). Esa velocidad viene del disco, no del modelo.

## 6. Resumen para el artículo

- Un token es un trozo de texto. Los límites se miden en tokens.
- `max_new_tokens` es un tope: si se alcanza, la respuesta se corta.
- Con razonamiento, el bloque `<think>` gasta tokens antes de la respuesta. Hay que subir el tope o la respuesta no aparece.

## 6. Limitaciones observadas en la salida

Ejemplo de la ejecución del 0,6 B con razonamiento (tope 1024), prompt "Dime cual es el mayor logro de la humanidad, en 4 lineas". La respuesta llega completa, pero tiene dos tipos de fallo:

- **Errores de español:** "el primer computador permitió la procesamiento" (el artículo y el sustantivo no concuerdan) y el uso de "la internet" en un contexto que pide otro registro. Son fallos habituales en un modelo pequeño, aunque el texto se entiende.
- **Error de hecho:** la respuesta dice que el primer computador lo desarrolló Alan Turing en los años 30. Turing describió en 1936 el modelo teórico de la computación, pero no construyó el primer computador. El modelo lo presenta con la misma seguridad que el resto.

Lo que se deduce: una respuesta bien escrita y con tono seguro no garantiza que los datos sean ciertos. Para la serie, cualquier cifra o hecho de un modelo se debe comprobar en una fuente oficial, no en la salida del modelo.

---

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| 0,6 B con razonamiento, 4 líneas, error de Turing | Respuesta completa con errores de español y de hecho | Salida pegada por el usuario, `test_qwen3_06b_es.py` (versión con 4 líneas) | Sí (una ejecución) |
| Turing, modelo teórico de 1936 | Formalizó la máquina de Turing en "On Computable Numbers…" (presentado en 1936, publicado en 1937); la wiki describe a Turing como el formalizador del modelo de computador de propósito general, no como constructor de un computador | Wikipedia en inglés, artículos "Alan Turing" y "On Computable Numbers…" (consultados 2026-11-08) | Sí (fuente secundaria; no se ha consultado el artículo original) |
| 0,6 B sin razonamiento, tope 128 | 128 tokens, cortada | Salida pegada por el usuario, `test_qwen3_06b_es.py` (primera versión) | Sí (una ejecución) |
| 0,6 B con razonamiento, tope 256 | 256 tokens, cortada | Salida pegada por el usuario | Sí (una ejecución) |
| 0,6 B sin razonamiento, tope 256 | 149 tokens, 28,7 s | Ejecución de la versión actual | Sí (una ejecución) |
| 0,6 B con razonamiento, tope 1024 | 335 tokens, 60,6 s | Ejecución de la versión actual | Sí (una ejecución) |
| 8B sin razonamiento, tope 128 | 127 tokens, 2.078 s | Salida pegada por el usuario, `test_qwen3_8b.py` | Sí (una ejecución) |
| Razonamiento activado por defecto | Sí | Ficha de Qwen3-8B (ver [002](../posts/002-01-UU-S-qwen3-8b.md)) | Sí |

## Pendiente

- Medir cuántos tokens necesita el razonamiento en otras preguntas. Con una sola pregunta no se puede generalizar.
- Repetir con el tope de 1024 en el 8B, si se consigue una máquina que lo cargue.
