# 006 · OpenClaw

**Fuente principal:** https://github.com/openclaw/openclaw (README, metadatos del repositorio) y https://www.npmjs.com/package/openclaw (metadatos del paquete)
**Documentación:** https://docs.openclaw.ai
**Licencia:** MIT (© OpenClaw Foundation). Verificada en el enlace `LICENSE` del README y en los metadatos del paquete npm.
**Consultado:** 2026-11-08
**Código:** 01-NU-S-006 (catálogo 01 Texto y LLM · tier NU, *provisional: OpenClaw es un gateway de asistente, no un modelo, así que no tiene tier por parámetros* · Starter; ver la sección "Familias")
**Pokémon asociado:** — (no se usa para herramientas)

---

## Resumen

Un asistente de IA que vive en tu propio ordenador y responde en las aplicaciones de mensajería que ya usas.

OpenClaw es un asistente de código abierto (licencia MIT) que se ejecuta en tu propio hardware. Un Gateway local lo conecta con canales como Telegram, WhatsApp, Slack o Discord, y los modelos que usa, en la nube o en local, son plugins que se pueden cambiar.

🔧 **Tipo y tecnología:** gateway de asistente de IA (no es un modelo). Paquete de Node.js, instalado con un script de instalación o con `npm`.
📏 **Tamaño:** el paquete npm se llama `openclaw`. Nuestra instalación de prueba usó unos 400 MB de RAM para el proceso del Gateway en una Raspberry Pi 5.
💻 **Hardware mínimo:** una versión de Node.js compatible (los metadatos de npm exigen 24.16.0 o posterior en la rama 24.x, o 26.1.0 o posterior). El README no da una cifra de hardware; nuestra máquina de prueba fue una Raspberry Pi 5 con 8 GB de RAM.
🛠️ **Interfaces:** canales de mensajería, una Control UI en el navegador, la línea de comandos `openclaw` y una interfaz de terminal.
🏢 **Detrás:** OpenClaw Foundation, con un repositorio público en GitHub.

Nuestras familias para este: Starter · tier NU (provisional, es un asistente, no un modelo) · Texto.

Repositorio: https://github.com/openclaw/openclaw

---

## Qué es

OpenClaw es un asistente que se ejecuta en la máquina del usuario y recibe peticiones a través de canales de mensajería. Su pieza central es el **Gateway**, un proceso de control local que gestiona sesiones, herramientas, eventos y las conexiones con los canales. La Control UI, la CLI y la TUI se conectan a él. El README indica que el estado, la memoria y las credenciales se quedan en el hardware del usuario, y que los modelos y los arneses de agente (Claude, Codex, modelos locales) son plugins.

No es un modelo de lenguaje. Usa los modelos que configura el usuario.

## Tipo y tecnología

- **Tipo:** gateway de asistente de IA personal. No es un modelo.
- **Runtime:** Node.js. El repositorio es un workspace de pnpm; `npm install` simple en la raíz no está soportado (README). No se ha comprobado el lenguaje de implementación para este artículo.
- **Instalación:** un script de instalación (`openclaw.ai/install.sh` para macOS y Linux, `openclaw.ai/install.ps1` para Windows) que instala también una versión compatible de Node.js si hace falta, o `npm install -g openclaw@latest`.
- **Puesta en marcha:** `openclaw onboard --install-daemon` (o el asistente que abre el instalador). Comprueba el acceso al modelo, crea el espacio de trabajo y configura el Gateway. `openclaw gateway status` muestra su estado.
- **Servicio:** con `--install-daemon` el Gateway se ejecuta como servicio. En la Raspberry Pi es una unidad de usuario de systemd con `Restart=always`.

## Tamaño

- **Paquete:** `openclaw` en npm, licencia MIT. Última versión en npm en el momento de la consulta: 2026.11.2 (registro de npm, 2026-11-08).
- **Versión de nuestra prueba:** 2026.5.27 (commit `27ae826`), que informa `openclaw --version` en la Raspberry Pi.
- **Requisito de motor (metadatos de npm):** Node.js `>=24.16.0 <25 || >=26.1.0`.

## Hardware mínimo

El README no da una cifra de hardware mínimo. La tabla muestra lo que observamos; no es un requisito.

| Configuración | Memoria | Referencia |
|---------------|---------|------------|
| Proceso del Gateway, unos 18 minutos después del reinicio | unos 400 MB (RSS 403.984 KB, 2,7 % de CPU en el momento de la medida) | Raspberry Pi 5, 8 GB de RAM |
| Proceso del Gateway, tras unos 14 días en marcha (observación anterior) | unos 530 MB (RSS 546.496 KB) | La misma Raspberry Pi 5 |

El modelo no está incluido en estas cifras: el asistente llama al modelo configurado en cada caso, en la nube o en local. Un modelo local añadiría su propio coste de memoria (ver el artículo 005 sobre llama.cpp).

## Interfaces

- **Canales de mensajería:** el README enumera WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Teams y más.
- **Control UI:** interfaz web que se abre con `openclaw gateway status` o desde la CLI.
- **CLI:** `openclaw` con subcomandos como `onboard`, `gateway` y `pairing`.
- **TUI:** interfaz de terminal conectada al Gateway.
- **Apps nativas y nodos:** las apps complementarias para macOS, iOS y otras plataformas añaden voz, Canvas, cámara y acciones del dispositivo (README y documentación).

## Quién lo usa y para qué

- El README describe un uso personal: un asistente que trabaja con los canales que el usuario ya tiene.
- No hemos verificado una lista de organizaciones o proyectos que lo usen, así que este artículo no cita ninguno.

## Por qué importa

Muestra un asistente cuyo estado, memoria y credenciales se quedan en la máquina del usuario, con modelos que se pueden cambiar. En nuestra prueba funcionó como servicio en una Raspberry Pi 5 de 8 GB, sin GPU, junto a otros procesos.

## Detrás del proyecto

- **Organización:** OpenClaw Foundation (línea de licencia del README).
- **Desarrollo:** el repositorio tuvo un push el 2026-11-08, el día de la consulta, y el README incluye una lista pública de contribuyentes.

## Curiosidades

- El README dice que las herramientas se ejecutan en el host para la sesión principal, salvo que se configure un sandbox. La guía de seguridad y un runbook de exposición están enlazados desde el README.
- El Gateway escucha en el puerto que indica `--port`. En nuestra prueba, `ss` lo mostró escuchando en `0.0.0.0:18789`, es decir, en todas las interfaces de red de la máquina y no solo en localhost.

---

## Familias

| Familia | Valor | Motivo |
|---------|-------|--------|
| Grupo (arquitectura) | No aplica: software de asistente, no una red neuronal | Usa modelos (transformers decoder) a través de plugins. |
| Categoría | Starter | La puesta en marcha personal más sencilla de un asistente en hardware propio. |
| Tier (parámetros) | NU (< 1 B) — *provisional* | OpenClaw no tiene parámetros. Se asigna el código NU por el esquema de códigos de la serie, como en el artículo 005; ver "Pendiente". |
| Tipo (modalidad) | Texto (mensajes) y voz en las plataformas compatibles | El README describe canales de mensajería y apps complementarias. |
| Línea evolutiva | No aplica | — |
| Ditto | No aplica | — |

---

## Cómo ejecutarlo

**Estado: instalado y ejecutado en una Raspberry Pi 5 (8 GB de RAM, Linux, Node.js 22.22.1 mediante nvm).** El servicio se paró y se arrancó con `systemctl --user` durante las pruebas de llama.cpp y volvió a estar `active` tras el reinicio. No probado en el equipo de referencia con Windows. La versión de Node.js de nuestra prueba (22.22.1) es inferior a la de 24.16.0 que exigen los metadatos de npm; el servicio funcionó igualmente (es una observación, no una recomendación).

### a. Requisitos previos

- Una versión de Node.js compatible (ver "Tamaño"). El README recomienda, por seguridad, 24.22.1 o posterior en la rama 24.x, o 26.12.1 o posterior en la 26.x.
- Linux (servicios de usuario de systemd), macOS o Windows.
- Un modelo: una cuenta en la nube o un modelo local, configurado durante la puesta en marcha.

### b. Instalación

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

En Windows, el README indica `iwr -useb https://openclaw.ai/install.ps1 | iex`. Para usar npm directamente:

```bash
npm install -g openclaw@latest --allow-scripts=openclaw
```

(El README indica que `--allow-scripts` es para npm 11.16 o posterior y para npm 12; las versiones anteriores usan otro flag, ver la guía de instalación.)

### c. Puesta en marcha y comprobación

```bash
openclaw onboard --install-daemon
openclaw gateway status
```

El último comando abre la Control UI. Envía un mensaje allí para comprobar que el asistente responde.

### d. Control en la Raspberry Pi

```bash
systemctl --user stop openclaw-gateway     # parar
systemctl --user start openclaw-gateway    # arrancar de nuevo
systemctl --user is-active openclaw-gateway
```

La unidad es `openclaw-gateway.service`, habilitada, con `Restart=always`. Pararla no la deshabilita, así que arranca de nuevo al iniciar la máquina.

### e. Avisos

- **Seguridad:** trata los mensajes entrantes como entrada no fiable. Los canales que aceptan mensajes directos emparejan por defecto a los remitentes desconocidos; aprueba un emparejamiento con `openclaw pairing approve <canal> <código>`.
- **Exposición:** en nuestra prueba el Gateway escuchaba en `0.0.0.0:18789`. Revisa la guía de exposición de la documentación antes de dejarlo accesible desde la red local.
- **Herramientas:** las herramientas se ejecutan en el host para la sesión principal, salvo que se configure sandbox.
- **Credenciales:** la configuración y las credenciales se guardan en la máquina; no las copies en artículos ni en repositorios.

## Notas de verificación

| Dato | Valor | Fuente | ¿Verificado? |
|------|-------|--------|--------------|
| Licencia | MIT | Enlace `LICENSE` del README; metadatos de npm | Sí |
| Repositorio creado | 2025-11-24 | API de GitHub (`openclaw/openclaw`) | Sí |
| Estrellas | unas 394.215 | API de GitHub, foto del 2026-11-08 | Sí |
| Última versión en npm | 2026.11.2 | Registro de npm (`openclaw/latest`), 2026-11-08 | Sí |
| Versión de nuestra prueba | 2026.5.27 (commit `27ae826`) | `openclaw --version` en la Pi y `package.json` | Sí (medido) |
| Requisito de Node.js | `>=24.16.0 <25 \|\| >=26.1.0` | Metadatos de npm (`engines`) | Sí |
| Comandos de instalación y puesta en marcha | como en el README | README (2026-11-08) | Sí |
| Canales | WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Teams y más | README | Sí |
| Puerto del Gateway en nuestra prueba | 18789, escuchando en `0.0.0.0` | `ExecStart` de la unidad y `ss -ltn` en la Pi | Sí (medido) |
| Memoria del Gateway | 403.984 KB unos 18 min tras el reinicio; 546.496 KB tras unos 14 días en marcha | `ps` en la Pi | Sí (medido, dos momentos) |
| Unidad de systemd | `openclaw-gateway.service`, habilitada, `Restart=always` | `systemctl --user` en la Pi | Sí (medido) |
| Detrás del proyecto | OpenClaw Foundation | Línea de licencia del README | Sí |
| Hardware mínimo | — | — | **No verificado** (no lo indica el README) |
| Usuarios u organizaciones | — | — | **No verificado** |

## Pendiente

- **Tier y código:** OpenClaw no tiene parámetros, así que el tier NU y la categoría Starter son provisionales, como se acordó para el artículo 005. Deben confirmarse antes de publicar.
- **Versión de Node.js:** nuestra prueba usó Node.js 22.22.1, inferior a la versión de los metadatos de npm. El servicio funcionó; no se ha comprobado el requisito oficial con una instalación limpia.
- **Exposición:** el Gateway escucha en todas las interfaces. Si debe restringirse a localhost, y cómo, queda pendiente de revisar la guía de exposición.
- **Diferencia de versión:** la prueba usó la 2026.5.27 y npm ofrece la 2026.11.2. No se ha probado la actualización.
