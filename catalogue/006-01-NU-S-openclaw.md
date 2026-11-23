<!-- Publishable summary. Full article (Spanish): posts/006-01-NU-S-openclaw.md. Keep in sync. -->

An AI assistant that runs on your own computer and answers in the messaging apps you already use.

OpenClaw is an open-source assistant (MIT license). A local Gateway connects it to channels such as Telegram, WhatsApp, Slack or Discord, and the models it uses, cloud or local, are plugins that can be swapped.

🔧 **Type:** AI assistant gateway (not a model). Node.js package, installed with an installer script or with `npm`.
📏 **Size:** the npm package is `openclaw`. Our test install used about 400 MB of RAM for the Gateway process on a Raspberry Pi 5.
💻 **Minimum hardware:** a supported Node.js version (the npm metadata requires 24.16.0 or later on 24.x, or 26.1.0 or later). The README gives no hardware figure; our test machine was a Raspberry Pi 5 with 8 GB of RAM.
🛠️ **Interfaces:** messaging channels, a Control UI in the browser, the `openclaw` command line, and a terminal interface.
🏢 **Behind it:** OpenClaw Foundation, with a public repository on GitHub.

Our families for this one: Starter · NU tier (provisional, it is an assistant, not a model) · Text.

Repository: https://github.com/openclaw/openclaw
