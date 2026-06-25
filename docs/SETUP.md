# Setup — AI OS (Local Edition)

This guide gets you from zero to a working AI OS in your editor. No server, no deployment. Everything runs on your computer.

Total time: about 10 minutes, most of it installing the prerequisites once.

---

## 1. Install the prerequisites (once)

You need three things:

1. **Python 3.9 or newer**
   - Windows / macOS: download from [python.org/downloads](https://www.python.org/downloads/). On Windows, tick **"Add python.exe to PATH"** during install.
   - Check it works: open a terminal and run `python --version` (Windows) or `python3 --version` (macOS / Linux).

2. **Claude Code**, logged into your Claude subscription
   - Install: [docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)
   - Log in with your Claude account (Pro / Max / Team). There is **no API key** to paste. The AI OS uses your subscription.

3. **VS Code** (recommended) — [code.visualstudio.com](https://code.visualstudio.com/)
   - Install the Claude Code extension, or just use the integrated terminal.

---

## 2. Get the project

Download or clone this folder anywhere on your machine, for example `Documents/ai-os`.

- **Download ZIP** (easiest for beginners): unzip it somewhere you can find it.
- **Or git clone** if you use git.

Then **open that folder in VS Code** (`File > Open Folder`).

---

## 3. Start Claude Code

Open the Claude Code panel in VS Code, or open a terminal **inside the project folder** and run:

```
claude
```

Claude Code loads `CLAUDE.md` automatically. You are now talking to your AI OS.

---

## 4. (Optional) Personalize it

Say, in the chat:

```
Set up my business
```

This runs the `business-setup` wizard. It asks a few questions and fills in
`context/my-business.md` and `context/my-voice.md` so every skill knows your
business and writes in your voice. You can skip this and do it later.

---

## 5. (Optional) Add API keys for power skills

The core works with **zero keys**. Some skills talk to outside services and need
a key. When you want one of those:

1. Copy `.env.example` to `.env` in the project root.
2. Uncomment and fill only the key you need (each key is labelled with the skill it unlocks).

For **Gmail, Google Calendar, and Google Drive**, the simplest path is the
built-in Claude connectors at [claude.ai/settings/connectors](https://claude.ai/settings/connectors).
No keys to manage: connect there, and the tools appear in your next message.

---

## Try it out

Ask for any of these in the chat:

- "Research my top 3 competitors in [industry]"
- "Write a LinkedIn post about [topic]"
- "Prep me for a meeting with [person/company]"
- "Add a task: follow up with [someone] on Friday"
- "What's on my plate this week?"
- "Do a weekly review"
- "Create a skill for [a workflow you repeat]"

---

## Windows note about hooks

The AI OS ships three small Python safety hooks (see `.claude/settings.json`).
They are invoked as `python3`. On Windows the Python launcher is usually
`python`, not `python3`. If you notice the hooks are not running:

- Easiest fix: make sure the **Python Launcher** is installed (it ships with the
  python.org installer) so `python3` resolves, **or**
- Create a `python3` alias, **or**
- Edit `.claude/settings.json` and change `python3` to `python` in the three
  hook commands.

The hooks are a safety net (blocking dangerous commands, keeping the daily log).
The system still works without them, but they are recommended.

---

## What's where

| Folder | What it holds |
|--------|---------------|
| `.claude/skills/` | Your skills (programs) |
| `.claude/agents/` | Subagents (workers) |
| `.claude/hooks/` | Safety hooks |
| `.claude/rules/` | System rules loaded every session |
| `config/preferences.yaml` | Language, timezone, model routing |
| `context/` | Your business + voice (filled by the wizard) |
| `memory/` | MEMORY.md + daily logs |
| `data/` | SQLite databases (tasks, etc.) |
| `docs/` | These guides |

That's it. No server to keep running, nothing to deploy. Close VS Code and your
data stays in the folder; reopen it and pick up where you left off.
