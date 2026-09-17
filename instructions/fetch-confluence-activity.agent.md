- Use this when asked for Confluence page creates/edits/comments in a space over a date range.
- Tool: `tools/fetch_confluence_activity.py`.
- First follow `./instructions/follow-jira-confluence-conventions.agent.md` for `.env` configuration.
- Invocation:
  + Run via `python tools/fetch_confluence_activity.py <space_key> <start_date> <end_date>`.
  + `space_key` — Confluence space key, e.g. `RPP`.
  + `start_date` / `end_date` — `YYYY-MM-DD` format.
  + Credentials are read from `jira_status_report/.env` — never pass them as arguments.
- Processing:
  + The script runs a CQL search scoped to the space and date range, then lists matching content items.
  + Do not hand-count activity — always invoke the script and use its printed output.
- Output format:
  + Present the script's printed total count and per-item list verbatim.
- Constraints:
  + Never fabricate results — if the space key is unconfirmed, ask the user before running.
