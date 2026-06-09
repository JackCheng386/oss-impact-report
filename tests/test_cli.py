import io
import json
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

from oss_impact_report.cli import main


class CliTests(unittest.TestCase):
    def test_cli_outputs_json_for_non_git_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = io.StringIO()

            with redirect_stdout(output):
                code = main(["--repo", tmp, "--format", "json"])

        self.assertEqual(code, 0)
        payload = json.loads(output.getvalue())
        self.assertEqual(payload["status"], "not_git_repository")

    def test_cli_writes_output_file_and_creates_parent_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "reports" / "impact.md"
            code = main([
                "--repo",
                tmp,
                "--format",
                "markdown",
                "--output",
                str(output_path),
                "--project-name",
                "Demo",
            ])

            self.assertEqual(code, 0)
            self.assertIn("# Demo Open Source Impact Report", output_path.read_text())

    def test_cli_rejects_non_positive_since_days(self):
        stderr = io.StringIO()
        with redirect_stdout(io.StringIO()), redirect_stderr(stderr):
            with self.assertRaises(SystemExit):
                main(["--since-days", "0"])

        self.assertIn("since_days must be greater than zero", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
