<!-- Resumen publicable. Artículo completo: posts/010-04-NU-B-chimera-vocal-synth.md. Mantener sincronizado. -->

Una voz que canta, habla y hace beatbox sin red neuronal y sin muestras grabadas.

CHIMERA es un sintetizador de voz de código abierto (licencia MIT) que funciona en el navegador. Cada sonido sale de una vía respiratoria simulada: pulmones, cuerdas vocales, garganta, lengua, labios y nariz. Arrastras la lengua en un corte de la cabeza y oyes cómo cambia la vocal.

🔧 **Tipo:** sintetizador por modelado físico, no un modelo de IA. Motor en Rust compilado a WebAssembly. En palabras del README: "No samples, no neural audio."
💻 **Hardware:** sin pesos y sin GPU. El motor que descarga el navegador ocupa unos 1,1 MB y se ejecuta en tu propia CPU, en cualquier navegador moderno con HTTPS.
🛠️ **Qué puedes hacer:** tocar la boca a mano, escribir texto en inglés o IPA, cantar letras en un piano roll, hacer beatbox o cambiar a un pájaro cantor, una foca, un caimán o un elefante.
💡 **Por qué importa:** es lo contrario de un TTS neuronal como Kokoro. Simula el cuerpo que produce una voz en lugar de aprenderla de grabaciones, así que cada control tiene un significado físico.
🏢 **Detrás:** Jameson Hodge. La documentación del proyecto dice que el motor se escribió con agentes de programación de IA, pero la voz en sí no lleva IA.

Nuestras familias para este: Ultra Beast · tier NU (provisional, es una simulación, no un modelo) · Audio.

Demo: https://chimera-vocal-synth.vercel.app/
Repositorio: https://github.com/jamesondh/chimera-vocal-synth
