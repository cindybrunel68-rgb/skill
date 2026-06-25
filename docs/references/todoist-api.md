# Todoist — API Reference

> Accès direct via REST. Pas de MCP. Utiliser `curl` ou Python `urllib`.

## Auth

```
Authorization: Bearer {TODOIST_API_KEY}
Content-Type: application/json
```

Clé dans `.env` → `TODOIST_API_KEY`.

## Base URL

```
https://api.todoist.com/api/v1/
```

⚠️ `/rest/v2/` est déprécié — utiliser `/api/v1/` uniquement.

---

## Créer une tâche — POST /api/v1/tasks

### Champ obligatoire

| Champ | Type | Description |
|-------|------|-------------|
| `content` | String | **Titre** de la tâche. Markdown supporté. |

### Champs importants

| Champ | Type | Notes |
|-------|------|-------|
| `description` | String | Corps/détails. **Markdown supporté** (gras, listes, liens) |
| `due_datetime` | String | Date + heure en RFC3339 UTC : `"2026-03-11T09:00:00Z"` |
| `due_date` | String | Date seule : `"2026-03-11"` (sans heure) |
| `due_string` | String | Langage naturel : `"today at 10:00"`, `"March 11 at 14:00"` |
| `due_lang` | String | Langue du due_string : `"fr"` ou `"en"` |
| `priority` | Integer | `1`=normal, `2`=moyen, `3`=élevé, `4`=urgent (rouge) |
| `project_id` | String | Défaut : Inbox |
| `labels` | Array[String] | `["label1", "label2"]` |

⚠️ `due_string`, `due_date`, `due_datetime` sont **mutuellement exclusifs** — n'en utiliser qu'un seul.

### Timezone (IMPORTANT)

Check `config/preferences.yaml` for the user's timezone. For `due_datetime`, convert to UTC :
- Example CET (UTC+1) : 10h00 local → `"2026-03-11T09:00:00Z"`
- Example CEST (UTC+2) : 10h00 local → `"2026-03-11T08:00:00Z"`

Alternative simple : utiliser `due_string` avec `due_lang: "en"` → Todoist gère la timezone.

### Priorités

| Valeur API | Affichage Todoist | Usage |
|-----------|-------------------|-------|
| `4` | p1 🔴 | Critique / urgent |
| `3` | p2 🟠 | Important |
| `2` | p3 🔵 | Normal |
| `1` | p4 (défaut) | Faible |

---

## Exemples complets

### Créer une tâche avec date + heure + description

```bash
curl -s -X POST "https://api.todoist.com/api/v1/tasks" \
  -H "Authorization: Bearer $TODOIST_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "🎯 Appel client",
    "description": "Préparer les slides avant l'\''appel.\n\n**Points à couvrir :**\n- Budget\n- Timeline\n- Prochaines étapes",
    "due_datetime": "2026-03-11T09:00:00Z",
    "priority": 3
  }'
```

### Créer avec due_string (plus simple)

```bash
curl -s -X POST "https://api.todoist.com/api/v1/tasks" \
  -H "Authorization: Bearer $TODOIST_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "🎯 Appel client",
    "description": "Contexte et détails ici.",
    "due_string": "March 11 at 10:00",
    "due_lang": "en",
    "priority": 3
  }'
```

### Lister les tâches du jour

```bash
curl -s "https://api.todoist.com/api/v1/tasks?filter=today" \
  -H "Authorization: Bearer $TODOIST_API_KEY"
```
Retourne `{"results": [...], "next_cursor": null}`.

### Compléter une tâche

```bash
curl -s -X POST "https://api.todoist.com/api/v1/tasks/{id}/close" \
  -H "Authorization: Bearer $TODOIST_API_KEY"
```
Retourne `204 No Content`.

### Mettre à jour une tâche

```bash
curl -s -X POST "https://api.todoist.com/api/v1/tasks/{id}" \
  -H "Authorization: Bearer $TODOIST_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"due_string": "tomorrow at 14:00", "priority": 4}'
```

### Supprimer une tâche

```bash
curl -s -X DELETE "https://api.todoist.com/api/v1/tasks/{id}" \
  -H "Authorization: Bearer $TODOIST_API_KEY"
```

---

## Python helper

```python
import os, json, urllib.request
from datetime import datetime, timezone, timedelta

TODOIST_API_KEY = os.environ["TODOIST_API_KEY"]
BASE = "https://api.todoist.com/api/v1"

def todoist(method, path, data=None):
    url = BASE + path
    payload = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=payload, method=method,
        headers={"Authorization": f"Bearer {TODOIST_API_KEY}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read()) if r.status != 204 else None

# Convertir heure Paris → UTC (hiver +1h, été +2h)
def paris_to_utc(dt_str: str) -> str:
    """'2026-03-11T10:00:00' → '2026-03-11T09:00:00Z' (hiver CET)"""
    dt = datetime.fromisoformat(dt_str)
    # Détecter hiver/été manuellement ou utiliser due_string à la place
    utc = dt - timedelta(hours=1)  # CET hiver
    return utc.strftime("%Y-%m-%dT%H:%M:%SZ")

# Créer une tâche complète
todoist("POST", "/tasks", {
    "content": "🎯 Titre de la tâche",
    "description": "**Contexte** : détails ici.\n\n- Point 1\n- Point 2",
    "due_string": "today at 10:00",
    "due_lang": "en",
    "priority": 3
})

# Lister les tâches du jour
data = todoist("GET", "/tasks?filter=today")
tasks = data.get("results", [])
```

---

## Filtres utiles (paramètre `filter`)

| Filtre | Signification |
|--------|---------------|
| `today` | Tâches dues aujourd'hui |
| `overdue` | Tâches en retard |
| `today \| overdue` | Aujourd'hui + retard |
| `p1` | Priorité urgente |
| `p1 & today` | Urgentes ET aujourd'hui |
| `no date` | Sans date |
| `#NomProjet` | Par projet |
| `@nomLabel` | Par label |

---

## Objet tâche retourné (champs clés)

```json
{
  "id": "6g8HMxjg9w9JrXF3",
  "content": "🎯 Titre",
  "description": "Corps markdown",
  "due": {
    "date": "2026-03-11",
    "datetime": "2026-03-11T09:00:00.000000Z",
    "string": "March 11 at 10:00",
    "timezone": "USER_TIMEZONE",
    "is_recurring": false
  },
  "priority": 3,
  "checked": false,
  "project_id": "...",
  "labels": []
}
```
