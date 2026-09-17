- Use this when asked to find how long a Jira issue spent in each status (time-in-status / cycle time).
- Tool: `tools/fetch_cycle_time.py`.
- First follow `./instructions/follow-jira-confluence-conventions.agent.md` for `.env` configuration.
- Invocation:
  + Run via `python tools/fetch_cycle_time.py <issue_key>`.
  + `issue_key` — the Jira issue key, e.g. `SCRUM-123`.
  + Credentials (`JIRA_SITE`, `JIRA_EMAIL`, `JIRA_API_TOKEN`) are read from `jira_status_report/.env` — never pass them as arguments.
- Processing:
  + The script fetches the issue with its changelog and computes hours spent in each distinct status from the transition history.
  + Do not hand-calculate cycle time — always invoke the script and use its printed output.
- Output format:
  + Present the script's printed lines verbatim: one line per status with hours spent.
- Constraints:
  + Never fabricate an issue's history — if the script errors (e.g. issue not found), report the error instead of guessing values.
  + If no issue key is provided, ask the user rather than guessing one.
