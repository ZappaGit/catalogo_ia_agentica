# Muestra cómo el tokenizador de Qwen3-8B convierte frases en tokens e IDs.
# Requiere: pip install tokenizers
# Ejecutar fuera del proyecto (p. ej. en la carpeta scratchpad), para no llenar el repositorio de entornos.
# Uso: python demo_tokenizacion.py

import sys

from tokenizers import Tokenizer

# En Windows la consola usa cp1252 por defecto; forzamos UTF-8 para ver los tokens sin error.
sys.stdout.reconfigure(encoding="utf-8")

MODELO = "Qwen/Qwen3-8B"

frases = [
    "Hola, ¿qué tal?",
    "Large language models are powerful.",
    "Tokenización",
    "hugs",
    "Ñandú 🤗",
    " hola",
    "1234567",
]

tokenizador = Tokenizer.from_pretrained(MODELO)

for frase in frases:
    # add_special_tokens=False: solo el texto, sin tokens de inicio o fin de la plantilla
    codificado = tokenizador.encode(frase, add_special_tokens=False)
    print(repr(frase), "->", len(codificado), "tokens")
    print("  tokens:", codificado.tokens)
    print("  ids:   ", codificado.ids)

print("Entradas del vocabulario (incluye tokens añadidos):", tokenizador.get_vocab_size())
