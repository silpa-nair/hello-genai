import argparse
import os
import sys

from dotenv import load_dotenv

_JIRA_STATUS_REPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "jira_status_report")
load_dotenv(os.path.join(_JIRA_STATUS_REPORT_DIR, ".env"))
sys.path.insert(0, _JIRA_STATUS_REPORT_DIR)

from jira_client import JiraClient  # noqa: E402


def calculate_sprint_totals(jira, project_key, story_points_field):
    """Fetch the active sprint's issues and return (total_points, completed_points, total_issues, completed_issues)."""
    board_id = jira.get_board_id(project_key)
    sprint = jira.get_active_sprint(board_id)
    if not sprint:
        return None

    issues = jira.get_sprint_issues(sprint["id"])

    total_points = 0.0
    completed_points = 0.0
    completed_issues = 0

    for issue in issues:
        fields = issue["fields"]
        points = fields.get(story_points_field) or 0
        is_done = fields["status"]["statusCategory"]["key"] == "done"

        total_points += points
        if is_done:
            completed_points += points
            completed_issues += 1

    return sprint["name"], total_points, completed_points, len(issues), completed_issues


def parse_args():
    parser = argparse.ArgumentParser(description="Calculate team-level sprint totals (story points, issues, % complete).")
    parser.add_argument("project_key", help="Jira project key, e.g. SCRUM")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    site = os.environ["JIRA_SITE"]
    email = os.environ["JIRA_EMAIL"]
    api_token = os.environ["JIRA_API_TOKEN"]
    story_points_field = os.environ.get("JIRA_STORY_POINTS_FIELD", "customfield_10016")

    jira = JiraClient(site, email, api_token)
    result = calculate_sprint_totals(jira, args.project_key, story_points_field)

    if result is None:
        print(f"No active sprint found for project '{args.project_key}'.")
        sys.exit(0)

    sprint_name, total_points, completed_points, total_issues, completed_issues = result
    points_percent = round((completed_points / total_points) * 100, 1) if total_points else 0.0
    issues_percent = round((completed_issues / total_issues) * 100, 1) if total_issues else 0.0

    print(f"Sprint: {sprint_name}")
    print(f"Story points: {completed_points}/{total_points} ({points_percent}%)")
    print(f"Issues: {completed_issues}/{total_issues} ({issues_percent}%)")
