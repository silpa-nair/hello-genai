- Use this when asked to wire a report builder into a runnable entry point that publishes to a Confluence page.
- Input format:
  + An existing report-builder function (e.g. `build_dashboard(sprint, issues, story_points_field)`) that returns a Confluence storage-format HTML string.
  + Environment variables from `.env`: `JIRA_SITE`, `JIRA_EMAIL`, `JIRA_API_TOKEN`, `JIRA_PROJECT_KEY`, a `*_PAGE_ID` variable for the target page, and `JIRA_STORY_POINTS_FIELD`.
- Processing steps:
  + Load env vars with `load_dotenv()` before reading `os.environ`.
  + Construct `JiraClient` and `ConfluenceClient` from the existing modules (`jira_status_report/jira_client.py`, `jira_status_report/confluence_client.py`) — do not duplicate their logic.
  + Resolve the board via `get_board_id(project_key)`, then the active sprint via `get_active_sprint(board_id)`.
  + If no active sprint exists, print a clear message and return without publishing.
  + Fetch issues via `get_sprint_issues(sprint["id"])`, then call the report builder to get the HTML body.
  + Publish via `ConfluenceClient.update_page(page_id, title, html_body)`.
- Output format:
  + A `main.py`-style script with a single `main()` function and `if __name__ == "__main__": main()` guard.
  + On success, print a one-line confirmation including the page ID that was updated.
- Constraints:
  + One entry point per target page — do not combine multiple report scopes (e.g. aggregate + detail) into a single script, since they publish to different pages with different visibility.
  + Never hard-code tokens, page IDs, or site URLs — always read from environment variables.
  + Reuse the shared `JiraClient`/`ConfluenceClient` classes; do not re-implement API calls inline.
