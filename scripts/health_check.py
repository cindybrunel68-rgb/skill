from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    checks = []
    required_paths = [
        ROOT / "CLAUDE.md",
        ROOT / "config" / "preferences.yaml",
        ROOT / "memory" / "MEMORY.md",
        ROOT / ".claude" / "settings.json",
        ROOT / ".claude" / "skills" / "analyst" / "scripts" / "run_analysis.py",
    ]

    for path in required_paths:
        checks.append({"path": str(path.relative_to(ROOT)), "exists": path.exists()})

    report = {
        "timestamp": datetime.now().isoformat(timespec="minutes"),
        "status": "ok" if all(item["exists"] for item in checks) else "warning",
        "checks": checks,
        "message": "Health check completed",
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
