import argparse
import os
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "jira_status_report", ".env"))

STATUS_CATEGORY_DONE = "done"


def fetch_issue_changelog(site, email, api_token, issue_key):
    """Fetch an issue with its full changelog from the Jira REST API."""
    response = requests.get(
        f"{site.rstrip('/')}/rest/api/3/issue/{issue_key}",
        params={"expand": "changelog"},
        auth=(email, api_token),
    )
    response.raise_for_status()
    return response.json()


def _parse_timestamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def compute_time_in_status(issue):
    """Return a dict of status name -> hours spent in that status, based on changelog transitions."""
    created = _parse_timestamp(issue["fields"]["created"])
    histories = sorted(issue["changelog"]["histories"], key=lambda h: h["created"])

    time_in_status = {}
    current_status = issue["fields"]["status"]["name"]
    last_change_at = created

    status_transitions = []
    for history in histories:
        changed_at = _parse_timestamp(history["created"])
        for item in history["items"]:
            if item["field"] == "status":
                status_transitions.append((changed_at, item["fromString"], item["toString"]))

    status_sequence = [(created, None, issue["fields"].get("status", {}).get("name"))]
    running_status = None
    running_start = created
    for changed_at, from_status, to_status in status_transitions:
        running_status = from_status
        duration_hours = (changed_at - running_start).total_seconds() / 3600
        time_in_status[running_status] = time_in_status.get(running_status, 0.0) + duration_hours
        running_start = changed_at

    final_status = issue["fields"]["status"]["name"]
    now = datetime.now(timezone.utc)
    duration_hours = (now - running_start).total_seconds() / 3600
    time_in_status[final_status] = time_in_status.get(final_status, 0.0) + duration_hours

    return time_in_status


def parse_args():
    parser = argparse.ArgumentParser(description="Fetch time-in-status / cycle time for a Jira issue.")
    parser.add_argument("issue_key", help="Jira issue key, e.g. SCRUM-123")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    site = os.environ["JIRA_SITE"]
    email = os.environ["JIRA_EMAIL"]
    api_token = os.environ["JIRA_API_TOKEN"]

    issue = fetch_issue_changelog(site, email, api_token, args.issue_key)
    time_in_status = compute_time_in_status(issue)

    print(f"Time in status for {args.issue_key}:")
    for status, hours in time_in_status.items():
        print(f"  {status}: {hours:.1f}h")
