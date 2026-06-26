import subprocess
import sys
import unittest
from pathlib import Path


class GoogleWorkspaceSkillTests(unittest.TestCase):
    def test_check_script_runs(self):
        repo_root = Path(__file__).resolve().parents[3]
        script = repo_root / ".claude" / "skills" / "google-workspace" / "scripts" / "check_google_workspace.py"
        self.assertTrue(script.exists(), "Le script de vérification Google Workspace doit exister")

        completed = subprocess.run(
            [sys.executable, str(script), "--action", "check"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("status", completed.stdout)


if __name__ == "__main__":
    unittest.main()
