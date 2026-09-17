- Use this when asked for team-level sprint totals (story points, issues, % complete) without per-contributor detail.
- Tool: `tools/calculate_sprint_totals.py`.
- First follow `./instructions/follow-jira-confluence-conventions.agent.md` for `.env` configuration and completion-check rules.
- Invocation:
  + Run via `python tools/calculate_sprint_totals.py <project_key>`.
  + `project_key` — Jira project key, e.g. `SCRUM`.
  + Credentials are read from `jira_status_report/.env` — never pass them as arguments.
- Processing:
  + The script resolves the board and active sprint for the project, fetches its issues, and sums story points/issues per the shared completion check.
  + If no active sprint exists, the script prints a clear message and exits without error — treat this as a valid result, not a failure.
- Output format:
  + Present the script's printed lines verbatim: sprint name, story points ratio/%, issues ratio/%.
- Constraints:
  + Never hand-calculate totals — always invoke the script and use its printed output.
  + Do not publish these totals to Confluence from this tool — that is the responsibility of `wire-confluence-publish-entrypoint.agent.md`.
