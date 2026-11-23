# 010 · CHIMERA (sintetizador de voz)

**Fuente principal:** https://github.com/jamesondh/chimera-vocal-synth (README, `docs/architecture.md`, metadatos del repositorio)
**Demo:** https://chimera-vocal-synth.vercel.app/
**Licencia:** MIT. Los archivos de terceros incluidos mantienen sus licencias: el CMU Pronouncing Dictionary (BSD) y las fuentes tipográficas (README).
**Consultado:** 2026-11-13
**Código:** 04-NU-B-010 (catálogo 04 Voz y audio · tier NU, *provisional: CHIMERA es una simulación física, no un modelo, así que no tiene tier de parámetros* · Ultra Beast; ver la sección "Familias")
**Pokémon asociado:** — (no se usa para herramientas)
**Origen:** no sale del catálogo del vault (`IA_Agentica/HuggingFace`). Lo propone el autor de la serie después de probar la demo web.

---

## Texto para LinkedIn

Una voz que canta, habla y hace beatbox sin red neuronal y sin muestras grabadas.

CHIMERA es un sintetizador de voz que funciona en el navegador. Cada sonido sale de una vía respiratoria simulada: pulmones, cuerdas vocales, garganta, lengua, labios y nariz. Arrastras la lengua en un corte de la cabeza y oyes cómo cambia la vocal.

🔧 **Tipo y tecnología:** sintetizador por modelado físico (no un modelo de IA). El motor está escrito en Rust y compilado a WebAssembly; la interfaz es React y TypeScript. El README dice: "No samples, no neural audio."
📏 **Tamaño:** el archivo del motor que descarga el navegador ocupa unos 1,1 MB (1.075.770 bytes, medido el 2026-11-13). No hay pesos.
💻 **Hardware mínimo:** un navegador moderno con WebAssembly y AudioWorklet, abierto por HTTPS. El README no da ninguna cifra de hardware.
🛠️ **Interfaces:** la aplicación web (tocar, hablar, cantar, beatbox y un bestiario de animales), el teclado del ordenador o Web MIDI, y una línea de comandos `chimera` que genera archivos WAV.
💡 **Por qué importa:** es el enfoque opuesto a un TTS neuronal como Kokoro (artículo 001). En lugar de aprender una voz a partir de datos, simula el cuerpo que produce la voz, así que cada parámetro tiene un significado físico.
🏢 **Detrás:** Jameson Hodge (GitHub `jamesondh`). La documentación de arquitectura dice que el autor escribió el motor trabajando con agentes de programación de IA.
🤓 **Curiosidad:** el mismo motor hace un pájaro cantor, una foca, un caimán y un elefante. La trompeta del elefante se modela como una lengüeta labial en la base de un tubo nasal largo.

Repositorio y demo: https://github.com/jamesondh/chimera-vocal-synth

#VoiceSynthesis #WebAssembly #OpenSource

---

## Qué es

CHIMERA es un sintetizador de voz basado en **modelado físico**. No reproduce grabaciones ni genera audio con una red neuronal. Simula en tiempo real el aire que recorre un tracto vocal: los pulmones empujan el aire, las cuerdas vocales (o la siringe de un pájaro) se abren y cierran, y la forma de la garganta, la lengua, los labios y la nariz filtra el sonido. El README lo resume así: "Every sound comes from a simulated airway (lungs, vocal folds or syrinx, a branched vocal tract, lips, nose), not from samples."

No es un modelo de IA generativa. Está en la serie como contraste: una voz hecha simulando un cuerpo, frente a voces aprendidas de datos (artículo 001).

## Tipo y tecnología

- **Tipo:** sintetizador de voz por modelado físico. No es un modelo y no tiene parámetros que entrenar.
- **Motor:** crate de Rust `chimera`, compilado a WebAssembly y ejecutado dentro de un **AudioWorklet** (el hilo de audio en tiempo real del navegador). El mismo código se ejecuta de forma nativa para los tests y para la línea de comandos `chimera` (README). Sus únicas dependencias son los crates `libm` y `serde` (`docs/architecture.md`).
- **Interfaz:** React y TypeScript, con dibujos en canvas que se animan con el estado en vivo del motor: presión en la vía respiratoria, flujo de aire, cuerdas vocales, espectros y formantes (README).
- **Modelo acústico** (`docs/architecture.md`):
  - **Vía respiratoria:** una red ramificada de secciones de tubo simulada con **FDTD** (diferencias finitas en el dominio del tiempo). El documento explica que la eligió frente al modelo de Kelly-Lochbaum porque resuelve en un solo marco las longitudes de tubo variables, la presión que se acumula detrás de un cierre, las pérdidas en las constricciones, las paredes blandas y las ramas (nariz, senos).
  - **Fuentes:** una glotis paramétrica por defecto (tono exacto), con jitter, shimmer, vibrato y voz de fry. Para los pájaros, una siringe de dos labios. Válvulas para las vibrantes y el zumbido de labios.
  - **Turbulencia:** ruido inyectado después de una constricción, según el número de Reynolds del flujo. Así se producen las fricativas (*s*, *f*) y la aspiración.
  - **Control:** cada fonema es un conjunto de **gestos** articulatorios (lengua, labios, mandíbula, velo…), al estilo de la Fonología Articulatoria.
  - **Texto:** inglés con el CMU Pronouncing Dictionary y reglas de respaldo, o IPA. Letras de canciones en inglés o coreano.
  - **Frecuencia interna:** 96 kHz para una voz humana adulta, 192 kHz para pájaros pequeños, y luego se diezma a la frecuencia de salida.

## Tamaño

- **Sin pesos.** El sonido sale de ecuaciones, no de parámetros entrenados.
- **Archivos descargados (medido el 2026-11-13):** motor `chimera-*.wasm` de 1.075.770 bytes; módulo principal de la interfaz de 274.143 bytes; vista de anatomía de 64.498 bytes. El diccionario de pronunciación se carga bajo demanda; no se midió su tamaño.
- **Lenguajes del repositorio (API de GitHub):** sobre todo Rust (unos 951 KB de código) y TypeScript (unos 555 KB).

## Hardware mínimo

El README no da ninguna cifra de hardware y no medimos el uso de CPU.

| Configuración | Requisito | Fuente |
|---------------|-----------|--------|
| Aplicación web | Navegador con WebAssembly y AudioWorklet, en HTTPS o localhost (contexto seguro) | README ("The AudioWorklet needs a secure context") |
| Compilar desde el código | Rust con el target `wasm32-unknown-unknown`, y Bun | README |

La simulación corre a 96 kHz o más por cada voz, en la CPU del usuario. No se ha comprobado cómo se comporta en un móvil o un portátil modesto.

## Interfaces

- **Tocar:** arrastrar la lengua, los labios y la mandíbula en un corte de la cabeza en vivo; pad de vocales, teclado del ordenador y Web MIDI.
- **Hablar:** texto en inglés o IPA, mostrado como partitura gestual con una tabla de consonantes.
- **Cantar:** un piano roll con letra por nota.
- **Beatbox:** pads y un secuenciador por pasos, con cada tambor como un gesto articulatorio.
- **Bestiario:** pájaro cantor, foca, caimán y elefante.
- **Cuerpos:** voces de hombre, mujer y niño que se mezclan de forma continua.
- **Línea de comandos:** `chimera render speech|text|song|notes|beatbox|creature|vowels` genera archivos WAV; `chimera diagnose` y `chimera compare` miden la voz.
- **Plugin:** el README dice que un plugin CLAP/VST3/AU "still ships, but it's secondary". No comprobado.

## Quién lo usa y para qué

- El README lo describe como un instrumento para hacer canciones en la aplicación web "without an LLM's help".
- No verificamos ninguna organización o proyecto que lo use, así que este artículo no nombra ninguno.

## Por qué importa

Los TTS neuronales como Kokoro aprenden una voz a partir de grabaciones y producen un audio muy parecido al de una persona real. CHIMERA sigue el camino antiguo de la **síntesis articulatoria**: simula el tracto vocal, así que la voz suena más robótica, pero cada control tiene un significado físico (posición de la lengua, presión de los pulmones, tamaño de la abertura nasal) y el mismo motor puede modelar animales. El README dice que "the robotic, primitive sound people like today stays available" a medida que mejora el realismo.

También se mide contra voces reales: la línea de comandos lo compara con el Children's Song Dataset y con 23 hablantes reales de la base de datos de voz TSP (README).

## Detrás del proyecto

- **Autor:** Jameson Hodge (usuario de GitHub `jamesondh`, nombre tomado del perfil de GitHub).
- **Cómo se hizo:** "written for this project, first in TypeScript and then ported to Rust, by the owner working with AI coding agents (the commit history shows both)" (`docs/architecture.md`).
- **Repositorio:** creado el 2026-11-05, último push el 2026-11-12, unas 2.200 estrellas (dato del 2026-11-13).
- **Base científica que cita el proyecto:** paredes de la vía respiratoria según Ishizaka, French y Flanagan (1975); carga de radiación de Flanagan; objetivos de vocales de Hillenbrand et al. (1995); duraciones de segmentos de Klatt (1979); gestos al estilo de Browman y Goldstein, Saltzman y Munhall, y Öhman. El documento enumera lo que no está atribuido, como el modelo de vía respiratoria en su conjunto y el pulso glótico.

## Curiosidades

- La voz de un instrumento sin IA se escribió con agentes de programación de IA. La voz en sí no contiene ninguna red neuronal.
- La trompeta del elefante es una válvula de lengüeta labial en la base de la trompa, modelada como un tubo nasal largo (`docs/architecture.md`).
- El motor puede producir sonidos con presión pulmonar negativa (ingresivos), eyectivas, implosivas y clics, todo con la misma simulación de la vía respiratoria y "no special-cased samples" (`docs/architecture.md`).
- El documento dice que "isn't a port of another synthesizer" y que no contiene código de otro sintetizador.

---

## Familias

| Familia | Valor | Motivo |
|---------|-------|--------|
| Grupo (arquitectura) | No aplica: simulación física (FDTD), no una red neuronal | No tiene pesos aprendidos. |
| Categoría | Ultra Beast — *provisional* | Proyecto de investigación experimental, con una semana de vida en la fecha de consulta. |
| Tier (parámetros) | NU (< 1 B) — *provisional* | CHIMERA no tiene parámetros. El código NU se asigna por el esquema de códigos de la serie, como en los artículos 005 y 006. |
| Tipo (modalidad) | Audio (voz) | Habla, canto, beatbox y sonidos de animales. |
| Línea evolutiva | No aplica | El documento dice que no es un port de otro sintetizador. |
| Ditto | No aplica | — |

---

## Cómo ejecutarlo

**Estado: no ejecutado en la máquina.** El 2026-11-13 se descargaron la aplicación web y sus archivos para leer el código y medir los tamaños, pero el sonido no se probó aquí en un navegador y no se compiló la línea de comandos.

### a. Aplicación web

Abrir https://chimera-vocal-synth.vercel.app/ en un navegador moderno. No necesita instalación.

### b. Desde el código (README)

```sh
bun install
bun run dev        # compila el wasm y lanza Vite en 127.0.0.1:5317
bun run test       # compila el wasm, cargo test --workspace, bun test tests
```

### c. Renders sin conexión (README)

```sh
cargo run --release -p chimera-cli -- render speech|text|song|notes|beatbox|creature|vowels …
```

### d. Avisos

- **Contexto seguro:** el AudioWorklet solo funciona en HTTPS o localhost.
- **Idiomas:** el habla es texto en inglés o IPA; el canto acepta letras en inglés o coreano. No hay soporte para español.
- **Proyecto joven:** el repositorio tiene una semana y cambia cada día. Funciones de `docs/architecture.md` como las cuerdas vocales de dos masas o la exportación a WAV desde la aplicación figuran como "not built (yet)".

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Licencia | MIT | API de GitHub (`licenseInfo`) y README | Sí |
| Sin audio neuronal ni muestras | "No samples, no neural audio." | README, "Vision & scope" | Sí |
| Motor | Rust compilado a WebAssembly, ejecutado en un AudioWorklet | README | Sí |
| Dependencias del motor | `libm` y `serde` | `docs/architecture.md` | Sí |
| Modelo acústico | Vía respiratoria FDTD ramificada, glotis paramétrica, siringe, ruido de turbulencia | `docs/architecture.md` | Sí |
| Frecuencia interna | 96 kHz humano adulto, 192 kHz pájaros pequeños | `docs/architecture.md` | Sí |
| Tamaño del motor | 1.075.770 bytes | Descarga de `chimera-BQPB1CRl.wasm`, 2026-11-13 | Sí (medido) |
| Lenguajes del repositorio | Rust 951.476 B; TypeScript 555.130 B | API de GitHub, 2026-11-13 | Sí |
| Creado / último push | 2026-11-05 / 2026-11-12 | API de GitHub | Sí |
| Estrellas | 2.202 | API de GitHub, dato del 2026-11-13 | Sí |
| Autor | Jameson Hodge (`jamesondh`) | Perfil de GitHub | Sí |
| Hecho con agentes de programación de IA | según la cita | `docs/architecture.md`, "References and credits" | Sí (declaración del proyecto) |
| Bestiario | pájaro cantor, foca, caimán, elefante | README y `docs/architecture.md` | Sí |
| Hardware mínimo | — | — | **No verificado** (el README no lo indica) |
| Usuarios u organizaciones | — | — | **No verificado** |

## Pendiente

- **Tier, categoría y código:** CHIMERA no tiene parámetros y no es un modelo, así que NU y Ultra Beast son provisionales. Confirmar antes de publicar.
- **Origen:** no sale del catálogo del vault. Decidir si caben en la serie herramientas que no son modelos de IA (los artículos 005 y 006 son herramientas, pero ejecutan modelos de IA; CHIMERA no).
- **Hardware:** no se midió el uso de CPU en el navegador.
- **Carta:** todavía no hay carta LaTeX en `carta/` (usaría el tono 04, turquesa, y `\artwave`).
- **Plugin:** no se comprobó el plugin CLAP/VST3/AU que menciona el README.
