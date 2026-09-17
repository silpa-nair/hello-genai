# Module 10 Completion Report

## Instruction Files
```
build-confluence-report-builder.agent.md
create-status-report.agent.md
creating-instructions.agent.md
follow-jira-confluence-conventions.agent.md
main.agent.md
wire-confluence-publish-entrypoint.agent.md
write-module-unit-tests.agent.md
```

## main.agent.md Contents
```markdown
# Instructions Catalog

Each entry below is an instruction file with a one-line description. Optional sub-fields after `+`:
- **Keywords** — trigger words/phrases: if user's request matches, load this instruction.
- **Target** — file glob pattern: if current file or context matches, consider this instruction relevant.
- **Exceptions** — edge cases or clarifications that don't fit in the one-liner.

---

- [`./instructions/creating-instructions.agent.md`](./creating-instructions.agent.md) — how to create, structure, and wire up new instruction files and skills across IDEs (Copilot, Cursor, Claude Code).
  + Keywords: create instruction, new instruction, bootstrap instructions, instruction catalog, main.agent.md

- [`./instructions/create-status-report.agent.md`](./create-status-report.agent.md) — generates a weekly status report (Markdown, Accomplishments/Blockers/Next Week sections, bullet points only, max 20 lines, professional tone, no fluff).
  + Keywords: status report, weekly update, sprint summary, accomplishments, blockers

- [`./instructions/build-confluence-report-builder.agent.md`](./build-confluence-report-builder.agent.md) — build a report-builder module that turns Jira/Confluence data into a Confluence storage-format HTML page (aggregate or per-contributor detail).
  + Keywords: report builder, aggregate report, detail report, per-contributor breakdown, dashboard builder

- [`./instructions/wire-confluence-publish-entrypoint.agent.md`](./wire-confluence-publish-entrypoint.agent.md) — wire a report builder into a runnable `main.py` entry point that publishes to a Confluence page.
  + Keywords: entry point, main.py, publish to Confluence, wire builder, scheduled job

- [`./instructions/follow-jira-confluence-conventions.agent.md`](./follow-jira-confluence-conventions.agent.md) — shared baseline conventions (env vars, client reuse, completion check, output format) referenced by the report-builder and entry-point instructions.
  + Keywords: jira conventions, confluence conventions, shared conventions, env vars, story points field

- [`./instructions/write-module-unit-tests.agent.md`](./write-module-unit-tests.agent.md) — write unit tests for a project module, covering normal/edge cases with mocked API calls.
  + Keywords: unit tests, test coverage, pytest, mock API, edge cases
```

## Sample Instruction
- File: build-confluence-report-builder.agent.md
- Contents:
```markdown
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
```
