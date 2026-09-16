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

- [`./instructions/write-module-unit-tests.agent.md`](./write-module-unit-tests.agent.md) — write unit tests for a project module, covering normal/edge cases with mocked API calls.
  + Keywords: unit tests, test coverage, pytest, mock API, edge cases
