# AI OS, Édition Locale

> Transforme Claude Code dans VS Code en ton système d'exploitation IA pour ton business. 100% local. Pas de serveur, pas de site web à héberger, aucun déploiement.

L'AI OS est un dossier que tu ouvres dans VS Code. Une fois ouvert, tu discutes avec ton assistant IA directement dans le chat, et il connaît ton business, écrit avec ta voix, fait tes recherches, gère tes tâches et apprend au fil du temps. Tu l'installes une fois, et tu t'en sers comme d'une conversation normale.

Aucune compétence technique requise. Si tu sais installer un logiciel et copier-coller, tu sais l'installer.

> [!NOTE]
> Cet AI OS a été conçu par **Thomas Berton**, fondateur de l'agence **Azuro AI**. Tous mes liens (chaîne YouTube, communauté, agence) sont en bas de ce guide, section [Créé par Thomas Berton](#créé-par-thomas-berton).

---

## Sommaire

- [Ce dont tu as besoin](#ce-dont-tu-as-besoin)
- [Installation pas à pas](#installation-pas-à-pas)
- [Ta première utilisation](#ta-première-utilisation)
- [Ce qu'il y a dedans](#ce-quil-y-a-dedans)
- [Connecter Gmail, Agenda, etc. (optionnel)](#connecter-gmail-agenda-etc-optionnel)
- [La mémoire](#la-mémoire)
- [En cas de souci](#en-cas-de-souci)
- [Pour aller plus loin](#pour-aller-plus-loin)
- [Créé par Thomas Berton](#créé-par-thomas-berton)

---

## Ce dont tu as besoin

Trois choses à installer une seule fois. Clique sur chaque lien, télécharge, installe.

| Outil | À quoi ça sert | Lien |
|-------|----------------|------|
| **Python 3.9 ou plus** | Fait tourner les scripts internes | [python.org/downloads](https://www.python.org/downloads/) |
| **Claude Code** | Le cerveau, connecté à ton abonnement Claude | [Installer Claude Code](https://docs.anthropic.com/en/docs/claude-code) |
| **VS Code** | L'éditeur dans lequel tu ouvres le dossier | [code.visualstudio.com](https://code.visualstudio.com/) |

> [!IMPORTANT]
> Sous **Windows**, pendant l'installation de Python, coche bien la case **"Add python.exe to PATH"** (ajouter Python au PATH). C'est important pour que tout fonctionne.

> [!NOTE]
> **Combien ça coûte ?** Rien de plus que ton abonnement Claude (Pro, Max ou Team). L'AI OS utilise ton compte Claude, il n'y a **aucune clé API Anthropic** à payer ou à coller. Tu es soumis aux mêmes limites d'usage que sur claude.ai.

---

## Installation pas à pas

### Étape 1 : Récupérer le dossier

Deux options, prends la plus simple pour toi :

- **Le plus facile :** sur la page GitHub du projet, clique sur le bouton vert **`Code`**, puis **`Download ZIP`**. Décompresse le fichier quelque part de facile à retrouver (par exemple dans `Documents`).
- **Si tu utilises git :** clone le dépôt.

```bash
git clone <url-du-depot> ai-os
```

### Étape 2 : Ouvrir le dossier dans VS Code

Ouvre VS Code, puis menu **`Fichier`** (File) > **`Ouvrir le dossier`** (Open Folder), et sélectionne le dossier que tu viens de décompresser.

### Étape 3 : Lancer Claude Code

Dans VS Code, ouvre le panneau Claude Code (ou ouvre un terminal **dans le dossier du projet** via le menu `Terminal` > `Nouveau terminal`, puis tape) :

```bash
claude
```

La première fois, Claude Code te demandera de te connecter à ton compte Claude. Suis les instructions à l'écran.

### Étape 4 : C'est prêt

Claude Code charge automatiquement le fichier `CLAUDE.md`. Tu parles maintenant à ton AI OS. Aucune autre configuration n'est nécessaire pour démarrer.

---

## Ta première utilisation

Pour commencer, dis-lui simplement, dans le chat :

```
Configure mon business
```

Cela lance l'assistant `business-setup` : il te pose quelques questions, puis remplit ton profil (ton business, ta voix, tes préférences) pour que tous les skills te connaissent. Tu peux aussi sauter cette étape et la faire plus tard.

Sinon, lance-toi directement. Quelques exemples à taper :

- `Recherche mes 3 principaux concurrents dans [ton secteur]`
- `Écris un post LinkedIn sur [ton sujet]`
- `Prépare-moi pour mon rendez-vous avec [personne ou entreprise]`
- `Ajoute une tâche : rappeler le client vendredi`
- `Qu'est-ce que j'ai au programme cette semaine ?`
- `Fais ma revue hebdomadaire`
- `Crée un skill pour [une tâche que tu répètes souvent]`

> [!TIP]
> Parle-lui normalement, en français. Pas besoin de commandes spéciales. Si tu ne sais pas quoi faire, demande-lui : *"Qu'est-ce que tu sais faire ?"*

---

## Ce qu'il y a dedans

### Les skills (tes programmes)

**Skills de base (aucune clé, fonctionnent tout de suite) :**

| Skill | Ce qu'il fait |
|-------|---------------|
| `business-setup` | Assistant de configuration de ton business |
| `research` | Recherche approfondie sur n'importe quel sujet (recherche web) |
| `content-writer` | Crée du contenu avec ta voix (LinkedIn, email, blog) |
| `meeting-prep` | Recherche + points de discussion pour tes rendez-vous |
| `email-assistant` | Trie tes emails, rédige des réponses, résume les fils |
| `weekly-review` | Revue hebdo structurée et plan de la semaine suivante |
| `task-manager` | Gestion de tâches et projets (base de données locale) |
| `scrum-master` | Stand-up quotidien, planning, suivi de projet |
| `analyst` | Audit du système et rapports |
| `skill-creator` | Crée tes propres skills sur mesure |
| `plugin-builder` | Empaquette tes skills en plugins distribuables |
| `build-website` | Méthode PRISM : sites web statiques premium |
| `build-app` | Méthode ATLAS : applications full-stack |

<details>
<summary><strong>Skills avancés (nécessitent une clé API, optionnels)</strong></summary>

| Skill | Ce qu'il fait | Clés nécessaires |
|-------|---------------|------------------|
| `research-lead` | URL LinkedIn vers dossier de recherche + message d'approche | Perplexity, OpenAI, Airtable |
| `content-pipeline` | Transcription YouTube vers posts LinkedIn + carrousels | variable |
| `email-digest` | Boîte mail vers analyse de sentiment + brief Slack | Gmail, Slack |
| `gamma-slides` | Markdown vers présentation pro | Gamma |
| `memory` | Mémoire sémantique, capture auto, déduplication | OpenAI, Pinecone |
| `scheduler` | Rappels et tâches récurrentes | variable |

Les clés se mettent dans un fichier `.env` (voir [Connecter des services](#connecter-gmail-agenda-etc-optionnel)).

</details>

### Les agents (tes assistants spécialisés)

| Agent | Modèle | Rôle |
|-------|--------|------|
| `researcher` | Sonnet | Recherche (lecture seule) |
| `content-writer` | Sonnet | Rédaction avec ta voix |
| `code-reviewer` | Opus | Analyse de qualité du code |

### Les hooks (ton filet de sécurité)

Trois petits gardes automatiques que l'IA ne peut pas contourner :

- **Avant action** : bloque les commandes dangereuses (`rm -rf`, etc.)
- **En fin de réponse** : tient à jour ton journal quotidien
- **Après un script** : vérifie que la sortie est correcte

---

## Connecter Gmail, Agenda, etc. (optionnel)

Le cœur fonctionne sans aucune clé. Quand tu veux brancher un service externe :

**Pour Gmail, Google Agenda et Google Drive**, le plus simple est d'utiliser les **connecteurs Claude** :

1. Va sur [claude.ai/settings/connectors](https://claude.ai/settings/connectors)
2. Connecte le service souhaité et autorise l'accès
3. Reviens dans Claude Code : les outils sont disponibles dès ton prochain message

Aucune clé à gérer.

**Pour les autres services** (Perplexity, Slack, Gamma, etc.) :

1. Copie le fichier `.env.example` et renomme la copie en `.env`
2. Décommente (retire le `#`) et remplis seulement la clé dont tu as besoin (chaque clé indique le skill qu'elle débloque)

> [!WARNING]
> Ne mets jamais de mot de passe dans ces fichiers, seulement des clés API. Et ne partage jamais ton fichier `.env` (il est déjà ignoré par git).

---

## La mémoire

L'AI OS se souvient des choses d'une session à l'autre, le tout en local, sans cloud :

1. **Mémoire native** : la mémoire de projet de Claude Code, chargée automatiquement à chaque session.
2. **Journaux quotidiens** : `memory/logs/` et l'index `memory/MEMORY.md` (les faits importants, toujours sous les yeux de l'IA).
3. **Mémoire vectorielle** (optionnelle, pour utilisateurs avancés) : recherche sémantique via le skill `memory`. Désactivée par défaut.

---

## En cas de souci

<details>
<summary><strong>Les hooks ne se déclenchent pas (surtout sous Windows)</strong></summary>

Les hooks sont appelés avec `python3`. Sous Windows, la commande est souvent `python` (et `python3` peut ouvrir le Microsoft Store par erreur). Si tu remarques que les hooks ne tournent pas :

- Solution la plus simple : réinstalle Python depuis [python.org](https://www.python.org/downloads/) en cochant **"Add python.exe to PATH"**. Le lanceur Python (`py`) est alors installé et `python3` fonctionne.
- Ou bien : ouvre `.claude/settings.json` et remplace les trois `python3` par `python`.

Bon à savoir : même si les hooks ne tournent pas, le reste du système fonctionne. Les hooks ne sont qu'un filet de sécurité.

</details>

<details>
<summary><strong>"claude : commande introuvable"</strong></summary>

Claude Code n'est pas installé ou pas dans le PATH. Reprends l'étape d'installation de [Claude Code](https://docs.anthropic.com/en/docs/claude-code) et relance VS Code après l'installation.

</details>

<details>
<summary><strong>"python : commande introuvable"</strong></summary>

Python n'est pas installé ou pas dans le PATH. Réinstalle-le depuis [python.org](https://www.python.org/downloads/) en cochant **"Add python.exe to PATH"** (Windows), puis relance VS Code.

</details>

<details>
<summary><strong>Un skill avancé renvoie une erreur de clé manquante</strong></summary>

C'est normal : ce skill a besoin d'une clé API. Soit tu l'ajoutes dans `.env` (voir la section connexion), soit tu utilises un skill de base qui ne demande aucune clé.

</details>

---

## Pour aller plus loin

- **Créer un skill sur mesure** : dis *"Crée un skill pour [ton process]"*. Voir [docs/SKILLS-GUIDE.md](docs/SKILLS-GUIDE.md).
- **Ajouter des serveurs MCP** (Notion, Perplexity, Slack...) : voir [docs/MCP-SERVERS.md](docs/MCP-SERVERS.md).
- **Activer la mémoire vectorielle** : voir [docs/MEMORY-UPGRADE.md](docs/MEMORY-UPGRADE.md).
- **Comprendre l'architecture** : voir [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
- **Guide de démarrage détaillé** : voir [docs/SETUP.md](docs/SETUP.md).

---

## Créé par Thomas Berton

Cet AI OS, c'est moi qui l'ai conçu. Je suis **Thomas Berton**, fondateur de l'agence **Azuro AI**. Je forme et j'accompagne au quotidien sur l'IA et Claude Code, sur ma chaîne YouTube et dans mes communautés.

Si tu veux aller plus loin :

- **Ma chaîne YouTube** (tutos Claude Code + AIOS, le meilleur endroit pour démarrer) : [youtube.com/@thomasbssh](https://youtube.com/@thomasbssh)
- **Me suivre sur LinkedIn** : [Thomas Berton](https://www.linkedin.com/in/thomas-berton-563894196/)
- **Le Club IA, gratuit** (la communauté pour débuter) : [skool.com/le-club-ia](https://skool.com/le-club-ia)
- **Le Club IA VIP** (hackathons, programme de certification, accompagnements) : [skool.com/le-club-ia-vip](https://skool.com/le-club-ia-vip)

### Travailler avec moi

- **Mon agence, Azuro AI** : on met en place l'IA sur mesure dans ton business. [azuro-ai.com](https://azuro-ai.com)
- **La version hébergée de l'AIOS** (branchée 24/7, gérée pour toi, pilotable depuis ton téléphone) : [azuro-ai.com/aios](https://azuro-ai.com/aios)
- **Une question, un projet ?** Écris-moi en DM sur LinkedIn, ou passe par [azuro-ai.com/contact](https://azuro-ai.com/contact).

---

## Structure du projet

```
ai-os/
├── CLAUDE.md              # Le noyau : les instructions du système
├── .claude/
│   ├── skills/            # Les skills (tes programmes)
│   ├── agents/            # Les 3 agents (tes assistants)
│   ├── hooks/             # Les 3 hooks (sécurité)
│   └── rules/             # Les règles chargées à chaque session
├── config/                # Préférences (langue, fuseau horaire...)
├── context/               # Ton business + ta voix (remplis par l'assistant)
├── memory/                # MEMORY.md + journaux quotidiens
├── data/                  # Bases de données locales (tâches, etc.)
└── docs/                  # Les guides
```

---

## Licence

Licence MIT : libre d'utilisation, de modification et de distribution. Voir [LICENSE](LICENSE).
