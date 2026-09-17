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

- [`./instructions/calculate-compound-interest.agent.md`](./calculate-compound-interest.agent.md) — invoke `tools/compound_interest.py` to calculate compound interest and present its output.
  + Keywords: compound interest, final amount, total interest, principal, annual rate

- [`./instructions/fetch-jira-cycle-time.agent.md`](./fetch-jira-cycle-time.agent.md) — invoke `tools/fetch_cycle_time.py` to compute time-in-status/cycle time for a Jira issue.
  + Keywords: cycle time, time in status, issue changelog, status transitions

- [`./instructions/fetch-confluence-activity.agent.md`](./fetch-confluence-activity.agent.md) — invoke `tools/fetch_confluence_activity.py` to list Confluence page creates/edits/comments in a space over a date range.
  + Keywords: confluence activity, page creates, page edits, comments, CQL search

- [`./instructions/calculate-sprint-totals.agent.md`](./calculate-sprint-totals.agent.md) — invoke `tools/calculate_sprint_totals.py` to compute team-level sprint totals without per-contributor detail.
  + Keywords: sprint totals, story points, team progress, active sprint
