- Use this when asked to build a new report-builder module that turns Jira/Confluence data into a Confluence page (e.g. aggregate vs. per-contributor detail views).
- First follow `./instructions/follow-jira-confluence-conventions.agent.md` for completion-check and Confluence output-format conventions shared across this project's automations.
- Input format:
  + A list of Jira issue dicts (from `JiraClient.get_sprint_issues`), each with `fields.status`, `fields.assignee`, `fields.summary`, and a configurable story-points field.
  + The active `sprint` dict (from `JiraClient.get_active_sprint`) for the report title/date.
  + Optional: Confluence activity data (page creates/edits/comments) if the report scope includes it.
  + A `story_points_field` string identifying the custom field ID to read points from.
- Processing steps:
  + Iterate all issues once; classify each for completion per the shared conventions instruction.
  + Aggregate totals for the report's declared scope only — team-level reports must not include any per-person breakdown; per-contributor reports must not leak data outside the intended roster.
  + Compute percentages as `round(completed / planned * 100, 1)`, guarding against division by zero (default to `0.0`).
  + Group any per-contributor data with a `defaultdict`, keyed by resolved display name (`fields.assignee.displayName` or `"Unassigned"`).
- Output format:
  + Return a single HTML string per the shared Confluence output-format conventions.
  + Always include a title heading, a "last updated"/date line, and one `<table>` per metric group.
- Constraints:
  + One file per builder, named `[scope]_report_builder.py` (e.g. `aggregate_report_builder.py`, `detail_report_builder.py`), following the existing style of `jira_status_report/report_builder.py` and `jira_status_report/dashboard_builder.py`.
  + Keep builders pure functions of their inputs — no network calls, no file I/O inside the builder itself.
  + Never merge aggregate and per-contributor data into the same output — they are published to different Confluence pages under different visibility rules.
