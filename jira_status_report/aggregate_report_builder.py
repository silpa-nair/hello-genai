from datetime import date


def build_aggregate_report(sprint, issues, story_points_field):
    """Compute team-level sprint totals only, rendered as Confluence storage-format HTML."""
    total_points = 0.0
    completed_points = 0.0
    completed_count = 0

    for issue in issues:
        fields = issue["fields"]
        points = fields.get(story_points_field) or 0
        is_done = fields["status"]["statusCategory"]["key"] == "done"

        total_points += points
        if is_done:
            completed_points += points
            completed_count += 1

    points_percent = round((completed_points / total_points) * 100, 1) if total_points else 0.0
    issues_percent = round((completed_count / len(issues)) * 100, 1) if issues else 0.0

    return f"""<h1>Sprint Overview</h1>
<p><strong>Sprint:</strong> {sprint['name']}</p>
<p><strong>Last updated:</strong> {date.today().isoformat()}</p>

<h2>Team Progress</h2>
<table>
<tr><th>Metric</th><th>Planned</th><th>Completed</th><th>% Complete</th></tr>
<tr><td>Story points</td><td>{total_points}</td><td>{completed_points}</td><td>{points_percent}%</td></tr>
<tr><td>Issues</td><td>{len(issues)}</td><td>{completed_count}</td><td>{issues_percent}%</td></tr>
</table>
"""
