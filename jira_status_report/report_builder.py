from datetime import date


def build_report(sprint, issues, story_points_field):
    """Compute sprint progress metrics and render them as Confluence storage-format HTML."""
    total_points = 0.0
    completed_points = 0.0
    completed_count = 0
    blockers = []

    for issue in issues:
        fields = issue["fields"]
        points = fields.get(story_points_field) or 0
        status = fields["status"]["name"]
        is_done = fields["status"]["statusCategory"]["key"] == "done"

        total_points += points
        if is_done:
            completed_points += points
            completed_count += 1
        if any(label.lower() in ("blocked", "blocker") for label in fields.get("labels", [])):
            blockers.append((issue["key"], fields["summary"], status))

    points_percent = round((completed_points / total_points) * 100, 1) if total_points else 0.0
    issues_percent = round((completed_count / len(issues)) * 100, 1) if issues else 0.0

    blocker_rows = "".join(
        f"<tr><td>{key}</td><td>{summary}</td><td>{status}</td></tr>"
        for key, summary, status in blockers
    ) or '<tr><td colspan="3">None</td></tr>'

    return f"""<h1>Weekly Sprint Status Report</h1>
<p><strong>Sprint:</strong> {sprint['name']}</p>
<p><strong>Reporting date:</strong> {date.today().isoformat()}</p>

<h2>Sprint Progress</h2>
<table>
<tr><th>Metric</th><th>Planned</th><th>Completed</th><th>% Complete</th></tr>
<tr><td>Story points</td><td>{total_points}</td><td>{completed_points}</td><td>{points_percent}%</td></tr>
<tr><td>Issues</td><td>{len(issues)}</td><td>{completed_count}</td><td>{issues_percent}%</td></tr>
</table>

<h2>Blockers</h2>
<table>
<tr><th>Key</th><th>Summary</th><th>Status</th></tr>
{blocker_rows}
</table>
"""
