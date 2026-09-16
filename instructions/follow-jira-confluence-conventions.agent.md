- Use this as the shared baseline for any Jira/Confluence automation script or module in this project (report builders, entry points, dashboards).
- Configuration:
  + Read all secrets/config from `.env` via `load_dotenv()`: `JIRA_SITE`, `JIRA_EMAIL`, `JIRA_API_TOKEN`, `JIRA_PROJECT_KEY`, `JIRA_STORY_POINTS_FIELD` (defaults to `customfield_10016`), and one `*_PAGE_ID` variable per target Confluence page.
  + Never hard-code tokens, page IDs, or site URLs anywhere in code — always read from environment variables.
- Client reuse:
  + Always reuse `JiraClient` (`jira_status_report/jira_client.py`) and `ConfluenceClient` (`jira_status_report/confluence_client.py`) for API access — never re-implement Jira/Confluence API calls inline.
- Issue completion check:
  + An issue is "done" when `fields.status.statusCategory.key == "done"` — use this exact check everywhere completion is determined, do not match on status name strings.
- Confluence output format:
  + Any HTML published to Confluence must be plain Confluence storage format: only `<h1>`/`<h2>`/`<table>` (and similar basic) tags, no external CSS/JS.
  + When a report section has no data, render a single placeholder row (e.g. `<tr><td colspan="N">None</td></tr>`) instead of an empty table.
