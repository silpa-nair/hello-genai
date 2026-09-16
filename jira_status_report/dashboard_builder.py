from collections import defaultdict
from datetime import date


def _assignee_name(fields):
    assignee = fields.get("assignee")
    return assignee["displayName"] if assignee else "Unassigned"


def build_dashboard(sprint, issues, story_points_field):
    """Compute sprint overview and per-assignee breakdown, rendered as Confluence storage-format HTML."""
    total_points = 0.0
    completed_points = 0.0
    completed_count = 0
    by_assignee = defaultdict(lambda: {"total": 0, "completed": 0, "points": 0.0})

    for issue in issues:
        fields = issue["fields"]
        points = fields.get(story_points_field) or 0
        is_done = fields["status"]["statusCategory"]["key"] == "done"
        name = _assignee_name(fields)

        total_points += points
        by_assignee[name]["total"] += 1
        by_assignee[name]["points"] += points
        if is_done:
            completed_points += points
            completed_count += 1
            by_assignee[name]["completed"] += 1

    points_percent = round((completed_points / total_points) * 100, 1) if total_points else 0.0
    issues_percent = round((completed_count / len(issues)) * 100, 1) if issues else 0.0

    assignee_rows = "".join(
        f"<tr><td>{name}</td><td>{stats['total']}</td><td>{stats['completed']}</td>"
        f"<td>{round((stats['completed'] / stats['total']) * 100, 1) if stats['total'] else 0}%</td>"
        f"<td>{stats['points']}</td></tr>"
        for name, stats in sorted(by_assignee.items())
    ) or '<tr><td colspan="5">No issues in sprint</td></tr>'

    return f"""<h1>Sprint Dashboard</h1>
<p><strong>Sprint:</strong> {sprint['name']}</p>
<p><strong>Last updated:</strong> {date.today().isoformat()}</p>

<h2>Sprint Overview</h2>
<table>
<tr><th>Metric</th><th>Planned</th><th>Completed</th><th>% Complete</th></tr>
<tr><td>Story points</td><td>{total_points}</td><td>{completed_points}</td><td>{points_percent}%</td></tr>
<tr><td>Issues</td><td>{len(issues)}</td><td>{completed_count}</td><td>{issues_percent}%</td></tr>
</table>

<h2>Per-Assignee Breakdown</h2>
<table>
<tr><th>Assignee</th><th>Issues</th><th>Completed</th><th>% Complete</th><th>Story Points</th></tr>
{assignee_rows}
</table>
"""
