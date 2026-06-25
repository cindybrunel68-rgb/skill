# Connections Protocol (Local Edition)

How the AI OS connects external services (Google, Slack, Notion, CRMs, etc.) when running locally in Claude Code.

When a user says *"I want to connect X"*, *"can you access my X"*, *"why don't you have access to X"*, or asks you to act on a service you can't currently reach, follow the hierarchy below. **Never skip ahead.** Never invent an extra step ("just give me your password", "paste your API key" out of nowhere).

Order: **Tier 0 -> Tier 1 -> Tier 2 -> Tier 3.**

---

## Tier 0: Did the user already set up local credentials? (check FIRST)

Before anything, check whether the user already wired their own credentials for this service via a local setup skill.

- Look for a setup skill under `.claude/skills/<service>-setup/` and run its `check_status.py` (or equivalent).
- Check `.env` for keys for the service (e.g. `GOOGLE_CLIENT_ID`, `SLACK_BOT_TOKEN`).
- Listen for signals: *"I already connected"*, *"use my API key"*, *"I have my credentials"*.

If Tier 0 applies (even if broken: expired token, missing scope), use the skill's own recovery flow, do NOT redirect to claude.ai.

---

## Tier 1: Claude Connector (the easy path for a local user)

Anthropic ships managed OAuth connectors at https://claude.ai/settings/connectors. They expose the service as `mcp__claude_ai_<Service>__*` tools you can call directly once OAuth is done. For a local Claude Code user this is usually the simplest option: no keys to store, no OAuth client to build.

### Connectors that commonly exist
- Google Drive, Gmail, Google Calendar
- Canva
- (more get added over time; when in doubt, suggest the user open `claude.ai/settings/connectors` and look)

### How to handle it
1. **If the `mcp__claude_ai_<Service>__*` tools are already in your tool inventory** -> OAuth is done. Just use them.
2. **If only `_authenticate` / `_complete_authentication` are available** -> OAuth not yet done. Tell the user:
   > "To finish connecting `<Service>`, go to [claude.ai/settings/connectors](https://claude.ai/settings/connectors), click Authenticate / Connect on that connector, authorize on the provider's page, then come back. Your next message will have access to the tools."
3. **Never call `_authenticate` yourself.**

If a Claude connector covers the need, **stop here.**

---

## Tier 2: Preinstalled setup skill

Some services have a dedicated `<service>-setup` skill that walks the user through setup conversationally. If one exists, hand off to it and follow its `SKILL.md` step by step. Do not improvise around it. Test with its `test_connection.py` (or equivalent) at the end.

---

## Tier 3: Improvised guidance (last resort)

If neither a Claude connector nor a setup skill exists, still help. Don't bounce back with "I don't have access".

1. State the situation honestly and ask to proceed.
2. Identify the connection method:
   - Public REST API with an API key -> user creates a key, drops it in `.env`, you write a thin wrapper script (inside the relevant skill's `scripts/`) or call it with `requests` / `curl`.
   - OAuth -> walk through the OAuth dance step by step.
   - A third-party MCP server -> install via `claude mcp add ...` (check security/maintenance first).
3. Walk **one step per message**. Confirm before continuing. Provide direct links to the relevant developer/admin panel.
4. At the end, offer to formalize it as a `<service>-setup` skill via `skill-creator`.

### Anti-patterns (never do these)
- Asking for the user's **password** to a third-party service.
- Asking for personal access tokens for services they did not intend to integrate.
- Hardcoding credentials anywhere outside `.env`.
- Claiming a service "has no API" without checking.
- Suggesting browser automation before exhausting API options.

---

## Style for the walkthrough (tiers 2 and 3)

- One step per message. Never dump the whole sequence at once.
- Direct clickable links over long explanations.
- Confirm ("ok" / "done") before moving on.
- Number the steps ("Step 3/7 ...").
- Test the connection for real before declaring success.
