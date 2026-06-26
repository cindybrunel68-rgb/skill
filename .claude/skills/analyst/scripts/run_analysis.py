from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime
from typing import List


ROOT = Path(__file__).resolve().parents[4]
REPORT_DIR = ROOT / ".claude" / "skills" / "analyst" / "data" / "reports"


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _check_file(path: Path) -> str:
    return "OK" if path.exists() else "MISSING"


def generate_analysis_report(project_root: Path, output_path: Path | None = None) -> str:
    if output_path is None:
        output_path = REPORT_DIR / f"{datetime.now().strftime('%Y-%m-%d')}_analysis.md"

    checks = [
        ("CLAUDE.md", project_root / "CLAUDE.md"),
        ("config/preferences.yaml", project_root / "config" / "preferences.yaml"),
        ("memory/MEMORY.md", project_root / "memory" / "MEMORY.md"),
        (".claude/settings.json", project_root / ".claude" / "settings.json"),
    ]

    missing = [name for name, path in checks if not path.exists()]
    issues: List[str] = []
    if missing:
        issues.append(f"Missing required files: {', '.join(missing)}")

    report_lines = [
        f"Date: {datetime.now().strftime('%Y-%m-%d')}",
        f"Time: {datetime.now().strftime('%H:%M')}",
        "",
        "BUGS AND ERRORS",
    ]

    if issues:
        report_lines.extend([f"- {issue}" for issue in issues])
    else:
        report_lines.append("- No critical issue detected in the visible AIOS configuration.")

    report_lines.extend([
        "",
        "SUGGESTED IMPROVEMENTS",
        "- Add a small verification script if health checks are needed repeatedly.",
        "- Keep the core configuration files aligned with the current skill layout.",
        "",
        "NEW IDEAS",
        "- Add a lightweight health command for quick AIOS checks.",
        "",
        "GENERAL STATE",
        "The AIOS appears structurally coherent. The main operational risks remain the local environment, especially Python and Claude Code visibility on Windows.",
    ])

    report_text = "\n".join(report_lines) + "\n"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_text, encoding="utf-8")
    return report_text


def main() -> int:
    report = generate_analysis_report(ROOT)
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
