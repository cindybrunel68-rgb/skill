import subprocess
import sys
import unittest
from pathlib import Path


class HealthCheckScriptTests(unittest.TestCase):
    def test_health_check_script_runs(self):
        repo_root = Path(__file__).resolve().parents[1]
        script = repo_root / "scripts" / "health_check.py"
        self.assertTrue(script.exists(), "Le script de santé doit exister")

        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("Health check completed", completed.stdout)


if __name__ == "__main__":
    unittest.main()
