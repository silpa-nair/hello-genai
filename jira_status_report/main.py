import os

from dotenv import load_dotenv

from confluence_client import ConfluenceClient
from jira_client import JiraClient
from report_builder import build_report

load_dotenv()


def main():
    site = os.environ["JIRA_SITE"]
    email = os.environ["JIRA_EMAIL"]
    api_token = os.environ["JIRA_API_TOKEN"]
    project_key = os.environ["JIRA_PROJECT_KEY"]
    confluence_page_id = os.environ["CONFLUENCE_PAGE_ID"]
    story_points_field = os.environ.get("JIRA_STORY_POINTS_FIELD", "customfield_10016")

    jira = JiraClient(site, email, api_token)
    confluence = ConfluenceClient(site, email, api_token)

    board_id = jira.get_board_id(project_key)
    sprint = jira.get_active_sprint(board_id)
    if not sprint:
        print(f"No active sprint found for project '{project_key}'.")
        return

    issues = jira.get_sprint_issues(sprint["id"])
    report_html = build_report(sprint, issues, story_points_field)

    confluence.update_page(confluence_page_id, f"Weekly Status Report - {sprint['name']}", report_html)
    print(f"Report published to Confluence page {confluence_page_id}.")


if __name__ == "__main__":
    main()
