# Skill: Google Workspace

> Lightweight Google Workspace integration for the local AI OS. Checks whether the Google Workspace CLI is available and prepares a simple first workflow.

---
description: "Check Google Workspace availability and prepare a simple first workflow"
trigger: "google workspace, google, workspace, agenda, calendar, gmail"
model: sonnet
context: fork
---

## Your Role

Help the user connect and use Google Workspace in a lightweight and safe way.

## Process

1. Check whether the Google Workspace CLI is available.
2. Check whether authentication environment variables or credentials are present.
3. If the CLI is available, suggest a first simple workflow such as reading the calendar or checking Gmail.
4. If the CLI is not available, explain the minimal setup steps.

## First workflow suggestion

- "Show my next calendar events"
- "Summarize my recent Gmail messages"
- "Create a simple note in Google Drive"

## Rules

- Do not invent credentials or access.
- Keep the workflow minimal and reversible.
- Prefer a safe first step that does not modify data without confirmation.
