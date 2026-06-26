from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def _check_gws() -> dict:
    gws_bin = shutil.which("gws")
    if gws_bin:
        return {"available": True, "path": gws_bin}
    cmd_path = os.path.expandvars(r"%APPDATA%\npm\gws.cmd")
    return {"available": Path(cmd_path).exists(), "path": cmd_path}


def _check_auth_env() -> dict:
    env = {
        "GOOGLE_WORKSPACE_CLI_TOKEN": bool(os.getenv("GOOGLE_WORKSPACE_CLI_TOKEN")),
        "GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE": bool(os.getenv("GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE")),
    }
    return env


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Google Workspace availability")
    parser.add_argument("--action", choices=["check"], default="check")
    args = parser.parse_args()

    gws_result = _check_gws()
    auth_result = _check_auth_env()

    report = {
        "status": "ready" if gws_result["available"] else "missing",
        "gws": gws_result,
        "auth": auth_result,
        "message": "Google Workspace CLI is installed and ready for use" if gws_result["available"] else "Google Workspace CLI is not available",
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
