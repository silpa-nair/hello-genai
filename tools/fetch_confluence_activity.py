import argparse
import os

import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "jira_status_report", ".env"))


def fetch_confluence_activity(site, email, api_token, space_key, start_date, end_date):
    """Fetch Confluence content (pages/comments) created in a space within a date range via CQL search."""
    cql = f'space="{space_key}" AND created>="{start_date}" AND created<="{end_date}"'
    response = requests.get(
        f"{site.rstrip('/')}/wiki/rest/api/content/search",
        params={"cql": cql, "limit": 100},
        auth=(email, api_token),
    )
    response.raise_for_status()
    return response.json()["results"]


def parse_args():
    parser = argparse.ArgumentParser(description="Fetch Confluence page creates/edits/comments for a space over a date range.")
    parser.add_argument("space_key", help="Confluence space key, e.g. RPP")
    parser.add_argument("start_date", help="Start date, format YYYY-MM-DD")
    parser.add_argument("end_date", help="End date, format YYYY-MM-DD")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    site = os.environ["JIRA_SITE"]
    email = os.environ["JIRA_EMAIL"]
    api_token = os.environ["JIRA_API_TOKEN"]

    results = fetch_confluence_activity(site, email, api_token, args.space_key, args.start_date, args.end_date)

    print(f"Confluence activity in space '{args.space_key}' from {args.start_date} to {args.end_date}:")
    print(f"  Total items: {len(results)}")
    for item in results:
        print(f"  - [{item['type']}] {item['title']}")
