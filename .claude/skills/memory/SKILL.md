---
name: memory
description: Query and manage the AIOS long-term memory (mem0 + Pinecone) and the daily logs. Layer 1 is owned by Claude Code natively.
---

# Memory Skill

Operates on layers 2 and 3 of the AIOS memory stack. Layer 1 (native auto-memory) is managed by Claude Code itself; see `.claude/rules/memory-protocol.md` for the full architecture.

## When to use this skill

- The user references something from a past session that is not in the native auto-memory topic files → search layer 3.
- The user asks "what have you got on me?" or wants an export → list layer 3.
- You want to manually add a fact you judge important enough → add to layer 3.
- You want to append a chronological event to today's log → write to layer 2.
- A skill (weekly-review, meeting-prep, business-setup) needs to persist project facts → use the Write tool against layer 1 topic files directly. Do NOT use this skill for layer 1 writes.

## Layer 3 operations (mem0 + Pinecone)

### Search (recommended: smart_search)
```bash
python3 .claude/skills/memory/scripts/smart_search.py --query "topic" --limit 5
```
Hybrid retrieval: BM25 keyword (30%) + vector similarity (70%) + temporal decay + MMR diversity. First run on a fresh install requires `--rebuild-index` to populate the FTS5 keyword index.

### Search (basic vector only)
```bash
python3 .claude/skills/memory/scripts/mem0_search.py --query "topic" --limit 10
```

### Rebuild keyword index
```bash
python3 .claude/skills/memory/scripts/smart_search.py --rebuild-index
```
Repopulates FTS5 from the history DB. Run after installation or to fix drift.

### Add a fact manually
```bash
python3 .claude/skills/memory/scripts/mem0_add.py --content "User prefers Pinecone over Supabase for vectors"
```

### Add from conversation messages
```bash
python3 .claude/skills/memory/scripts/mem0_add.py --messages '[{"role":"user","content":"I switched to ClickUp"}]'
```

### List all memories
```bash
python3 .claude/skills/memory/scripts/mem0_list.py --limit 50
```

### Delete a memory
```bash
python3 .claude/skills/memory/scripts/mem0_delete.py --memory-id "abc123"
python3 .claude/skills/memory/scripts/mem0_delete.py --all --confirm
```

## Layer 2 operation (daily logs)

### Append to today's session log
```bash
python3 .claude/skills/memory/scripts/daily_log.py --content "Completed memory system overhaul" --type event
```

## Deprecated

`mem0_sync_md.py` was used to regenerate the legacy `/root/aios/memory/MEMORY.md` from Pinecone. Since the May 2026 migration, layer 1 is Claude Code's native auto-memory (claude-managed). Running this script would clobber claude's writes. The script is kept on disk only for one-shot manual exports if explicitly needed.

```bash
# DO NOT RUN under normal circumstances
# python3 .claude/skills/memory/scripts/mem0_sync_md.py
```

## Auto-capture (background, no action needed)

Stop hook `auto_capture.py` runs after every response cycle. It reads new transcript messages, feeds them to mem0 for fact extraction and dedup against Pinecone, and appends a session summary to today's daily log. Logs at `data/auto_capture.log`.

## Config

- mem0 config: `.claude/skills/memory/references/mem0_config.yaml`
- LLM for extraction: GPT-4.1 Nano
- Embeddings: text-embedding-3-small (OpenAI)
- Vector store: Pinecone (cloud, free tier, serverless), index name `aios-memory`
- History DB: `data/mem0_history.db` (SQLite, auto-managed)
- Capture markers: `data/capture_markers/` (tracks transcript position per session)

## Security

What's protected:
- `sanitize_text()` in `mem0_client.py` strips secrets (API keys, tokens, JWTs, connection strings) from all text before it leaves the machine.
- Applied in both `auto_capture.py` (automatic) and `mem0_add.py` (manual).
- The extraction prompt explicitly tells GPT-4.1 Nano to skip passwords, keys, tokens, credentials.
- `prepare_messages()` strips code blocks before sending to OpenAI.
- System tags and reminders are stripped from transcripts.
- `.gitignore` excludes `.env`, `data/`, `memory/logs/`, `.claude/settings.local.json`.

What to be aware of:
- Conversation snippets are sent to the OpenAI API for fact extraction (per Anthropic and OpenAI policy these are not used for training).
- Extracted facts plus vectors are stored in Pinecone cloud.
- Local files (SQLite history DB, daily logs) are plaintext on disk.
- For maximum security, swap to local Qdrant plus a local LLM (mem0 config supports this as a one-line change per component).

## Known issues

1. **mem0 v1.0.4 + Pinecone**: `get_all()` and `delete_all()` have upstream bugs. `mem0_list.py` and `mem0_delete.py --all` fall back to the local history DB.
2. **Complex markdown content**: GPT-4.1 Nano can fail to return valid JSON when processing messages with heavy markdown. `prepare_messages()` strips most of this, but some batches may still fail. Failed batches are not lost; the underlying transcript is preserved.
3. **First run with a large backlog**: incremental runs (2-4 messages) are reliable; first-time runs over a long conversation can have failed batches on complex content.

## Two-tier reality on clients

- **Phil's AIOS** runs the full Tier 3 stack (mem0 + Pinecone + OpenAI). All operations above are available.
- **Client AIOSes** by default run Tier 1+2 only: no Pinecone, no semantic search. Layer 2 (daily logs) and layer 1 (native auto-memory) work everywhere, requiring no external services. Clients opt into Tier 3 by following `docs/MEMORY-UPGRADE.md`.
