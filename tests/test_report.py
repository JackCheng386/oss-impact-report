import json
import unittest

from oss_impact_report.git_metrics import Contributor, GitMetrics
from oss_impact_report.report import metrics_to_dict, render_json, render_markdown


class ReportTests(unittest.TestCase):
    def sample_metrics(self) -> GitMetrics:
        return GitMetrics(
            repository="C:\\work\\example",
            branch="main",
            head="abc1234",
            since_days=90,
            commit_count=12,
            contributor_count=2,
            top_contributors=[
                Contributor(name="Ada Lovelace", email="ada@example.com", commits=8),
                Contributor(name="Grace Hopper", email=None, commits=4),
            ],
            latest_tags=["v0.1.0"],
            latest_commit_date="2026-06-07T18:33:21+00:00",
        )

    def test_metrics_to_dict_serializes_contributors(self):
        data = metrics_to_dict(self.sample_metrics())

        self.assertEqual(data["head"], "abc1234")
        self.assertEqual(data["top_contributors"][0]["name"], "Ada Lovelace")
        self.assertEqual(data["top_contributors"][1]["email"], None)

    def test_render_json_is_valid_json(self):
        data = json.loads(render_json(self.sample_metrics()))

        self.assertEqual(data["commit_count"], 12)
        self.assertEqual(data["latest_tags"], ["v0.1.0"])

    def test_render_markdown_contains_core_sections(self):
        markdown = render_markdown(self.sample_metrics(), project_name="Example")

        self.assertIn("# Example Open Source Impact Report", markdown)
        self.assertIn("## Recent Contributors", markdown)
        self.assertIn("| Ada Lovelace <ada@example.com> | 8 |", markdown)
        self.assertIn("- `v0.1.0`", markdown)


if __name__ == "__main__":
    unittest.main()
