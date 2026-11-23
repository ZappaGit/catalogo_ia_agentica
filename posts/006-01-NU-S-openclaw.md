# 006 · OpenClaw

**Main source:** https://github.com/openclaw/openclaw (README, repository metadata) and https://www.npmjs.com/package/openclaw (package metadata)
**Documentation:** https://docs.openclaw.ai
**License:** MIT (© OpenClaw Foundation). Verified in the repository `LICENSE` link and the npm package metadata.
**Consulted:** 2026-11-08
**Code:** 01-NU-S-006 (catalogue 01 Text and LLMs · tier NU, *provisional: OpenClaw is an assistant gateway, not a model, so it has no parameter tier* · Starter; see the "Families" section)
**Associated Pokémon:** — (not used for tools)

---

## LinkedIn text

An AI assistant that lives on your own computer and answers in the messaging apps you already use.

OpenClaw is an open-source AI assistant that runs on your own hardware. A local Gateway connects it to channels such as Telegram, WhatsApp, Slack or Discord, and the models it uses (cloud or local) are plugins that can be swapped.

🔧 **Type and technology:** AI assistant gateway (not a model). Node.js package, installed with `npm` or with an installer script. The Gateway is a local control process with a Control UI, CLI and TUI.
📏 **Size:** the npm package is published as `openclaw`. Our test install (version 2026.5.27) used about 400 MB of RAM for the Gateway process on the Raspberry Pi 5.
💻 **Minimum hardware:** a machine with a supported Node.js version (24.16.0 or later on the 24.x line, or 26.1.0 or later). Our test machine was a Raspberry Pi 5 with 8 GB of RAM.
🛠️ **Interfaces:** messaging channels (Telegram, WhatsApp, Slack, Discord, Teams, iMessage and others listed in the README), the Control UI in the browser, the `openclaw` CLI, and a TUI.
🏢 **Behind it:** OpenClaw Foundation, with a public repository on GitHub. Repository created on 2025-11-24.
🤓 **Curiosity:** the project has about 394,000 stars on GitHub (snapshot 2026-11-08). The README says inbound messages from unknown senders are treated as untrusted and are paired before use.

Repository: https://github.com/openclaw/openclaw

#AI #Agents #OpenSource

---

## What it is

OpenClaw is an assistant that runs on the user's machine and receives requests through messaging channels. Its central piece is the **Gateway**, a local control process that manages sessions, tools, events and the channel connections. The Control UI, the CLI and the TUI connect to it. The README states that state, memory and credentials stay on the user's hardware, and that the models and agent harnesses (Claude, Codex, local models) are plugins.

It is not a language model. It uses models that the user configures.

## Type and technology

- **Type:** personal AI assistant gateway. Not a model.
- **Runtime:** Node.js. The repository is a pnpm workspace; plain `npm install` at the root is not supported (README). The implementation language was not checked for this article.
- **Installation:** an installer script (`openclaw.ai/install.sh` for macOS and Linux, `openclaw.ai/install.ps1` for Windows) that also provisions a supported Node.js when needed, or `npm install -g openclaw@latest`.
- **Onboarding:** `openclaw onboard --install-daemon` (or the wizard opened by the installer). It checks model access, creates the workspace and configures the Gateway. `openclaw gateway status` shows its state.
- **Service:** with `--install-daemon` the Gateway runs as a service. On the Raspberry Pi it is a systemd user unit with `Restart=always`.

## Size

- **Package:** `openclaw` on npm, MIT license. Latest version on npm at consulting time: 2026.11.2 (npm registry, 2026-11-08).
- **Version in our test:** 2026.5.27 (commit `27ae826`), reported by `openclaw --version` on the Raspberry Pi.
- **Engine requirement (npm metadata):** Node.js `>=24.16.0 <25 || >=26.1.0`.

## Minimum hardware

The README does not give a minimum hardware figure. The table shows what we observed; it is not a requirement.

| Configuration | Memory | Reference |
|---------------|--------|-----------|
| Gateway process, about 18 minutes after restart | about 400 MB (RSS 403,984 KB, 2.7 % CPU at the moment of measurement) | Raspberry Pi 5, 8 GB RAM |
| Gateway process, after about 14 days running (earlier observation) | about 530 MB (RSS 546,496 KB) | Same Raspberry Pi 5 |

The model is not included in these figures: the assistant calls the model configured in each case, cloud or local. A local model would add its own memory cost (see article 005 for llama.cpp).

## Interfaces

- **Messaging channels:** the README lists WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Teams and more.
- **Control UI:** a web interface opened by `openclaw gateway status` or by the CLI.
- **CLI:** `openclaw` with subcommands such as `onboard`, `gateway` and `pairing`.
- **TUI:** a terminal interface connected to the Gateway.
- **Native apps and nodes:** companion apps for macOS, iOS and other platforms add voice, Canvas, camera and device actions (README and docs).

## Who uses it and for what

- The README describes personal use: an assistant that works with the channels the user already has.
- We did not verify a list of organizations or projects that use it, so this article does not name any.

## Why it matters

It shows an assistant whose state, memory and credentials stay on the user's machine, with models that can be swapped. In our test it ran as a service on an 8 GB Raspberry Pi 5 without a GPU, next to other processes.

## Behind the project

- **Organization:** OpenClaw Foundation (README license line).
- **Development:** the repository was pushed on 2026-11-08, the day of consulting, and has a public contributors list in the README.

## Curiosities

- The README says tools run on the host for the main session unless sandboxing is configured. The security guide and an exposure runbook are linked from the README.
- The Gateway listens on the port set by `--port`. In our test, `ss` showed it listening on `0.0.0.0:18789`, that is, on every network interface of the machine, not only on localhost.

---

## Families

| Family | Value | Reason |
|--------|-------|--------|
| Group (architecture) | Not applicable: assistant software, not a neural network | It uses models (transformer decoders) through plugins. |
| Category | Starter | The simplest personal setup for an assistant on your own hardware. |
| Tier (parameters) | NU (< 1 B) — *provisional* | OpenClaw has no parameters. The NU code is assigned for the series' code scheme, as in article 005; see "Pending". |
| Type (modality) | Text (messages) and voice on supported platforms | The README describes messaging channels and companion apps. |
| Evolutionary line | Not applicable | — |
| Ditto | Not applicable | — |

---

## How to run it

**Status: installed and run on a Raspberry Pi 5 (8 GB RAM, Linux, Node.js 22.22.1 via nvm).** The service was stopped and started with `systemctl --user` during the llama.cpp tests and it returned to `active` after the restart. Not tested on the reference Windows machine. The Node.js version used in our test (22.22.1) is below the 24.16.0 required by the npm metadata; the service nevertheless ran (this is an observation, not a recommendation).

### a. Prerequisites

- A supported Node.js version (see "Size"). Recommended by the README: 24.22.1 or later on 24.x, or 26.12.1 or later on 26.x, for security.
- Linux (systemd user services), macOS or Windows.
- A model: a cloud account or a local model, configured during onboarding.

### b. Installation

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

On Windows, the README gives `iwr -useb https://openclaw.ai/install.ps1 | iex`. To use npm directly:

```bash
npm install -g openclaw@latest --allow-scripts=openclaw
```

(The README notes that `--allow-scripts` is for npm 11.16 or later and for npm 12; older versions use a different flag, see the installation guide.)

### c. Onboarding and check

```bash
openclaw onboard --install-daemon
openclaw gateway status
```

The last command opens the Control UI. Send a message there to confirm that the assistant responds.

### d. Control on the Raspberry Pi

```bash
systemctl --user stop openclaw-gateway     # stop
systemctl --user start openclaw-gateway    # start again
systemctl --user is-active openclaw-gateway
```

The unit is `openclaw-gateway.service`, enabled, with `Restart=always`. Stopping it does not disable it, so it starts again at boot.

### e. Warnings

- **Security:** treat inbound messages as untrusted input. Channels that accept direct messages pair unknown senders by default; approve a pairing with `openclaw pairing approve <channel> <code>`.
- **Exposure:** the Gateway listened on `0.0.0.0:18789` in our test. Check the exposure guide in the documentation before leaving it reachable from the local network.
- **Tools:** tools run on the host for the main session unless sandboxing is configured.
- **Credentials:** the configuration and the credentials are stored on the machine; do not copy them into articles or repositories.

## Verification notes

| Data | Value | Source | Verified? |
|------|-------|--------|-----------|
| License | MIT | `LICENSE` link in README; npm metadata | Yes |
| Repository created | 2025-11-24 | GitHub API (`openclaw/openclaw`) | Yes |
| Stars | about 394,215 | GitHub API, snapshot 2026-11-08 | Yes |
| Latest npm version | 2026.11.2 | npm registry (`openclaw/latest`), 2026-11-08 | Yes |
| Version in our test | 2026.5.27 (commit `27ae826`) | `openclaw --version` on the Pi and `package.json` | Yes (measured) |
| Node.js requirement | `>=24.16.0 <25 \|\| >=26.1.0` | npm metadata (`engines`) | Yes |
| Installer and onboarding commands | as in the README | README (2026-11-08) | Yes |
| Channels | WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Teams and more | README | Yes |
| Gateway port in our test | 18789, listening on `0.0.0.0` | `ExecStart` of the unit and `ss -ltn` on the Pi | Yes (measured) |
| Memory of the Gateway | 403,984 KB about 18 min after restart; 546,496 KB after about 14 days running | `ps` on the Pi | Yes (measured, two moments) |
| Systemd unit | `openclaw-gateway.service`, enabled, `Restart=always` | `systemctl --user` on the Pi | Yes (measured) |
| Behind the project | OpenClaw Foundation | README license line | Yes |
| Minimum hardware | — | — | **No verified** (not stated in the README) |
| Users or organizations | — | — | **No verified** |

## Pending

- **Tier and code:** OpenClaw has no parameters, so the NU tier and the Starter category are provisional, as agreed for article 005. They should be confirmed before publication.
- **Node.js version:** our test ran on Node.js 22.22.1, below the version in the npm metadata. The service ran; this has not been checked against the official requirement in a clean install.
- **Exposure:** the Gateway listens on all interfaces. Whether it should be restricted to localhost, and how, is pending the review of the exposure guide.
- **Version gap:** the test used 2026.5.27 and npm offers 2026.11.2. An update has not been tested.
