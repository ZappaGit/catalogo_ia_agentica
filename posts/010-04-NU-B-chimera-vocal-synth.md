# 010 · CHIMERA (vocal synthesizer)

**Main source:** https://github.com/jamesondh/chimera-vocal-synth (README, `docs/architecture.md`, repository metadata)
**Demo:** https://chimera-vocal-synth.vercel.app/
**License:** MIT. Bundled third-party files keep their own licenses: the CMU Pronouncing Dictionary (BSD) and the fonts (README).
**Consulted:** 2026-11-13
**Code:** 04-NU-B-010 (catalogue 04 Voice and audio · tier NU, *provisional: CHIMERA is a physical simulation, not a model, so it has no parameter tier* · Ultra Beast; see the "Families" section)
**Associated Pokémon:** — (not used for tools)
**Origin:** not from the vault catalogue (`IA_Agentica/HuggingFace`). Proposed by the author of the series after trying the web demo.

---

## LinkedIn text

A voice that sings, speaks and beatboxes with no neural network and no recorded samples.

CHIMERA is a voice synthesizer that runs in the browser. Every sound comes from a simulated airway: lungs, vocal folds, throat, tongue, lips and nose. Drag the tongue in a cutaway of the head and you hear the vowel change.

🔧 **Type and technology:** physical-modelling synthesizer (not an AI model). The engine is written in Rust and compiled to WebAssembly; the interface is React and TypeScript. The README states: "No samples, no neural audio."
📏 **Size:** the engine file the browser downloads is about 1.1 MB (1,075,770 bytes, measured on 2026-11-13). There are no weights.
💻 **Minimum hardware:** a modern browser with WebAssembly and AudioWorklet, opened over HTTPS. The README gives no hardware figure.
🛠️ **Interfaces:** the web app (play, speak, sing, beatbox and a bestiary of animals), a computer keyboard or Web MIDI, and a `chimera` command line that renders WAV files.
💡 **Why it matters:** it is the opposite approach to a neural TTS such as Kokoro (article 001). Instead of learning a voice from data, it simulates the body that makes the voice, so every parameter has a physical meaning.
🏢 **Behind it:** Jameson Hodge (GitHub `jamesondh`). The architecture doc says the engine was written by the owner working with AI coding agents.
🤓 **Curiosity:** the same engine does a songbird, a seal, an alligator and an elephant. The elephant's trumpet is modelled as a lip reed at the base of a long nasal tube.

Repository and demo: https://github.com/jamesondh/chimera-vocal-synth

#VoiceSynthesis #WebAssembly #OpenSource

---

## What it is

CHIMERA is a voice synthesizer based on **physical modelling**. It does not play back recordings or generate audio with a neural network. It simulates the air moving through a vocal tract in real time: the lungs push air, the vocal folds (or a bird's syrinx) open and close, and the shape of the throat, tongue, lips and nose filters the sound. The README sums it up: "Every sound comes from a simulated airway (lungs, vocal folds or syrinx, a branched vocal tract, lips, nose), not from samples."

It is not a generative AI model. It is in the series as a contrast: a voice made by simulating a body, set against voices learned from data (article 001).

## Type and technology

- **Type:** physical-modelling voice synthesizer. Not a model and with no parameters to train.
- **Engine:** Rust crate `chimera`, compiled to WebAssembly and run inside an **AudioWorklet** (the browser's real-time audio thread). The same code runs natively for tests and for the `chimera` command line (README). Its only dependencies are the `libm` and `serde` crates (`docs/architecture.md`).
- **Interface:** React and TypeScript, with canvas drawings that animate from the engine's live state: airway pressure, airflow, the vocal folds, spectra and formants (README).
- **Acoustic model** (`docs/architecture.md`):
  - **Airway:** a branched network of tube sections simulated with **FDTD** (finite-difference time-domain). The doc says it chose this over the Kelly-Lochbaum model because it handles changing tube lengths, pressure building up behind a closure, losses at constrictions, soft walls and branches (nose, sinuses) in one framework.
  - **Sources:** a parametric glottis by default (exact pitch), with jitter, shimmer, vibrato and vocal fry. For birds, a two-labia syrinx. Valves for trills and the lip buzz.
  - **Turbulence:** noise injected after a constriction, based on the Reynolds number of the airflow. This produces the fricatives (*s*, *f*) and the aspiration.
  - **Control:** each phoneme is a set of articulatory **gestures** (tongue, lips, jaw, velum…), in the style of Articulatory Phonology.
  - **Text:** English through the CMU Pronouncing Dictionary with a letter-to-sound fallback, or IPA. Song lyrics in English or Korean.
  - **Internal rate:** 96 kHz for an adult human voice, 192 kHz for small birds, then decimated to the output rate.

## Size

- **No weights.** The sound comes from equations, not from trained parameters.
- **Downloaded files (measured 2026-11-13):** engine `chimera-*.wasm` of 1,075,770 bytes; main interface module of 274,143 bytes; anatomy view of 64,498 bytes. The pronunciation dictionary is lazy-loaded; its size was not measured.
- **Repository languages (GitHub API):** mainly Rust (about 951 KB of code) and TypeScript (about 555 KB).

## Minimum hardware

The README gives no hardware figure, and we did not measure CPU use.

| Configuration | Requirement | Source |
|---------------|-------------|--------|
| Web app | Browser with WebAssembly and AudioWorklet, on HTTPS or localhost (secure context) | README ("The AudioWorklet needs a secure context") |
| Build from source | Rust with the `wasm32-unknown-unknown` target, and Bun | README |

The simulation runs at 96 kHz or more for each voice, on the CPU of the user's machine. How it behaves on a low-end phone or laptop has not been checked.

## Interfaces

- **Play:** drag the tongue, lips and jaw in a live cutaway of the head; vowel pad, computer keyboard and Web MIDI.
- **Speak:** English text or IPA, shown as a gestural score with a consonant chart.
- **Sing:** a piano roll with lyrics per note.
- **Beatbox:** pads and a step sequencer, with each drum as an articulatory gesture.
- **Bestiary:** songbird, seal, alligator and elephant.
- **Bodies:** male, female and child voices blend continuously.
- **Command line:** `chimera render speech|text|song|notes|beatbox|creature|vowels` renders WAV files; `chimera diagnose` and `chimera compare` measure the voice.
- **Plugin:** the README says a CLAP/VST3/AU plugin "still ships, but it's secondary". Not checked.

## Who uses it and for what

- The README describes it as an instrument for making songs in the web app "without an LLM's help".
- We did not verify any organization or project that uses it, so this article does not name any.

## Why it matters

Neural TTS models such as Kokoro learn a voice from recordings and produce audio that is very close to a real speaker. CHIMERA takes the old route of **articulatory synthesis**: it simulates the vocal tract, so the voice sounds more robotic, but each control has a physical meaning (tongue position, lung pressure, size of the nasal opening) and the same engine can model animals. The README states that "the robotic, primitive sound people like today stays available" as realism improves.

It is also measured against real voices: the CLI compares it with the Children's Song Dataset and with 23 real speakers of the TSP speech database (README).

## Behind the project

- **Author:** Jameson Hodge (GitHub user `jamesondh`, name from the GitHub profile).
- **How it was built:** "written for this project, first in TypeScript and then ported to Rust, by the owner working with AI coding agents (the commit history shows both)" (`docs/architecture.md`).
- **Repository:** created on 2026-11-05, last push on 2026-11-12, about 2,200 stars (snapshot 2026-11-13).
- **Scientific basis cited by the project:** airway walls from Ishizaka, French & Flanagan (1975); Flanagan's radiation load; vowel targets from Hillenbrand et al. (1995); segment durations from Klatt (1979); gestures in the style of Browman & Goldstein, Saltzman & Munhall and Öhman. The doc lists what is not attributed, such as the airway model as a whole and the glottal pulse.

## Curiosities

- The voice of an AI-free instrument was written with AI coding agents. The voice itself contains no neural network.
- The elephant's trumpet is a lip-reed valve at the base of the trunk, modelled as a long nasal tube (`docs/architecture.md`).
- The engine can make sounds with negative lung pressure (ingressive), ejectives, implosives and clicks, all through the same airway simulation and "no special-cased samples" (`docs/architecture.md`).
- The doc says it "isn't a port of another synthesizer" and contains no other synthesizer's code.

---

## Families

| Family | Value | Reason |
|--------|-------|--------|
| Group (architecture) | Not applicable: physical simulation (FDTD), not a neural network | It has no learned weights. |
| Category | Ultra Beast — *provisional* | Experimental research project, one week old at consulting time. |
| Tier (parameters) | NU (< 1 B) — *provisional* | CHIMERA has no parameters. The NU code is assigned for the series' code scheme, as in articles 005 and 006. |
| Type (modality) | Audio (voice) | Speech, singing, beatboxing and animal sounds. |
| Evolutionary line | Not applicable | The doc says it is not a port of another synthesizer. |
| Ditto | Not applicable | — |

---

## How to run it

**Status: not run on the machine.** The web app and its files were downloaded on 2026-11-13 to read the code and measure the sizes, but the sound was not tested in a browser here, and the CLI was not built.

### a. Web app

Open https://chimera-vocal-synth.vercel.app/ in a modern browser. It needs no installation.

### b. From source (README)

```sh
bun install
bun run dev        # builds the wasm, then Vite on 127.0.0.1:5317
bun run test       # wasm build, cargo test --workspace, bun test tests
```

### c. Offline renders (README)

```sh
cargo run --release -p chimera-cli -- render speech|text|song|notes|beatbox|creature|vowels …
```

### d. Warnings

- **Secure context:** the AudioWorklet only works on HTTPS or localhost.
- **Languages:** speech is English text or IPA; singing accepts English or Korean lyrics. There is no Spanish front end.
- **Young project:** the repository is one week old and changes every day. Features in `docs/architecture.md` such as the two-mass vocal folds and in-app WAV export are listed as "not built (yet)".

## Verification notes

| Data | Value | Source | Verified? |
|------|-------|--------|-----------|
| License | MIT | GitHub API (`licenseInfo`) and README | Yes |
| No neural audio, no samples | "No samples, no neural audio." | README, "Vision & scope" | Yes |
| Engine | Rust compiled to WebAssembly, run in an AudioWorklet | README | Yes |
| Engine dependencies | `libm` and `serde` | `docs/architecture.md` | Yes |
| Acoustic model | Branched FDTD airway, parametric glottis, syrinx, turbulence noise | `docs/architecture.md` | Yes |
| Internal rate | 96 kHz adult human, 192 kHz small birds | `docs/architecture.md` | Yes |
| Engine file size | 1,075,770 bytes | Download of `chimera-BQPB1CRl.wasm`, 2026-11-13 | Yes (measured) |
| Repository languages | Rust 951,476 B; TypeScript 555,130 B | GitHub API, 2026-11-13 | Yes |
| Created / last push | 2026-11-05 / 2026-11-12 | GitHub API | Yes |
| Stars | 2,202 | GitHub API, snapshot 2026-11-13 | Yes |
| Author | Jameson Hodge (`jamesondh`) | GitHub profile | Yes |
| Built with AI coding agents | as quoted | `docs/architecture.md`, "References and credits" | Yes (project statement) |
| Bestiary | songbird, seal, alligator, elephant | README and `docs/architecture.md` | Yes |
| Minimum hardware | — | — | **Not verified** (not stated in the README) |
| Users or organizations | — | — | **Not verified** |

## Pending

- **Tier, category and code:** CHIMERA has no parameters and is not a model, so NU and Ultra Beast are provisional. Confirm before publication.
- **Origin:** it does not come from the vault catalogue. Decide whether tools outside AI models fit the series (articles 005 and 006 are tools, but they run AI models; CHIMERA does not).
- **Hardware:** CPU use in the browser was not measured.
- **Card:** no LaTeX card in `carta/` yet (it would use tone 04, turquoise, and `\artwave`).
- **Plugin:** the CLAP/VST3/AU plugin mentioned in the README was not checked.
