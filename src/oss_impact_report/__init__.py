"""Local-first impact reporting for open source maintainers."""

from .git_metrics import GitMetrics, collect_git_metrics
from .report import metrics_to_dict, render_markdown

__all__ = [
    "GitMetrics",
    "collect_git_metrics",
    "metrics_to_dict",
    "render_markdown",
]

__version__ = "0.1.0"
