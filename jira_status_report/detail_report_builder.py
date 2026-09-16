from collections import defaultdict
from datetime import date


def _assignee_name(fields):
    assignee = fields.get("assignee")
    return assignee["displayName"] if assignee else "Unassigned"


def build_detail_report(sprint, issues, story_points_field):
    """Compute per-contributor breakdown only, rendered as Confluence storage-format HTML."""
    by_assignee = defaultdict(lambda: {"total": 0, "completed": 0, "points": 0.0})

    for issue in issues:
        fields = issue["fields"]
        points = fields.get(story_points_field) or 0
        is_done = fields["status"]["statusCategory"]["key"] == "done"
        name = _assignee_name(fields)

        by_assignee[name]["total"] += 1
        by_assignee[name]["points"] += points
        if is_done:
            by_assignee[name]["completed"] += 1

    assignee_rows = "".join(
        f"<tr><td>{name}</td><td>{stats['total']}</td><td>{stats['completed']}</td>"
        f"<td>{round((stats['completed'] / stats['total']) * 100, 1) if stats['total'] else 0}%</td>"
        f"<td>{stats['points']}</td></tr>"
        for name, stats in sorted(by_assignee.items())
    ) or '<tr><td colspan="5">None</td></tr>'

    return f"""<h1>Per-Contributor Detail</h1>
<p><strong>Sprint:</strong> {sprint['name']}</p>
<p><strong>Last updated:</strong> {date.today().isoformat()}</p>

<h2>Per-Assignee Breakdown</h2>
<table>
<tr><th>Assignee</th><th>Issues</th><th>Completed</th><th>% Complete</th><th>Story Points</th></tr>
{assignee_rows}
</table>
"""
