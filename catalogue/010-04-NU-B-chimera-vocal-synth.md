<!-- Publishable summary. Full article: posts/010-04-NU-B-chimera-vocal-synth.md. Keep in sync. -->

A voice that sings, speaks and beatboxes with no neural network and no recorded samples.

CHIMERA is an open-source voice synthesizer (MIT license) that runs in the browser. Every sound comes from a simulated airway: lungs, vocal folds, throat, tongue, lips and nose. Drag the tongue in a cutaway of the head and you hear the vowel change.

🔧 **Type:** physical-modelling synthesizer, not an AI model. Rust engine compiled to WebAssembly. In the README's words: "No samples, no neural audio."
💻 **Hardware:** no weights and no GPU. The engine your browser downloads is about 1.1 MB, and it runs on your own CPU in any modern browser over HTTPS.
🛠️ **What you can do:** play the mouth by hand, type English text or IPA, sing lyrics on a piano roll, beatbox, or switch to a songbird, a seal, an alligator or an elephant.
💡 **Why it matters:** it is the opposite of a neural TTS like Kokoro. It simulates the body that makes a voice instead of learning one from recordings, so every control has a physical meaning.
🏢 **Behind it:** Jameson Hodge. The project's docs say the engine was written with AI coding agents, but the voice itself has no AI in it.

Our families for this one: Ultra Beast · NU tier (provisional, it is a simulation, not a model) · Audio.

Demo: https://chimera-vocal-synth.vercel.app/
Repository: https://github.com/jamesondh/chimera-vocal-synth
