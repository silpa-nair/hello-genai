- Use this when asked to wire a report builder into a runnable entry point that publishes to a Confluence page.
- First follow `./instructions/follow-jira-confluence-conventions.agent.md` for configuration and client-reuse conventions shared across this project's automations.
- Input format:
  + An existing report-builder function (e.g. `build_dashboard(sprint, issues, story_points_field)`) that returns a Confluence storage-format HTML string.
  + A `*_PAGE_ID` environment variable identifying the target page for this entry point.
- Processing steps:
  + Load env vars with `load_dotenv()` before reading `os.environ`.
  + Construct `JiraClient` and `ConfluenceClient` per the shared conventions instruction.
  + Resolve the board via `get_board_id(project_key)`, then the active sprint via `get_active_sprint(board_id)`.
  + If no active sprint exists, print a clear message and return without publishing.
  + Fetch issues via `get_sprint_issues(sprint["id"])`, then call the report builder to get the HTML body.
  + Publish via `ConfluenceClient.update_page(page_id, title, html_body)`.
- Output format:
  + A `main.py`-style script with a single `main()` function and `if __name__ == "__main__": main()` guard.
  + On success, print a one-line confirmation including the page ID that was updated.
- Constraints:
  + One entry point per target page — do not combine multiple report scopes (e.g. aggregate + detail) into a single script, since they publish to different pages with different visibility.
