# Jira/Confluence Automation — Requirements Document

## 1. Weekly Stakeholder Status Report

**Goal:** Automatically summarize Jira sprint progress for stakeholders on a recurring basis.

| Requirement | Decision |
|---|---|
| Data source | Jira Cloud REST API |
| Output destination | Confluence page (overwritten each run) |
| Trigger | Scheduled weekly (Task Scheduler) |
| Scope | Single project/board: `SCRUM` |
| Sprint selection | Currently active sprint |
| Authentication | API token via `.env` (HTTP Basic Auth) |
| Language | Python |
| Jira site | `https://silpa-nair.atlassian.net` |
| Content | Sprint progress table (planned vs. completed story points/issues), blockers list |

**Implementation:** [jira_status_report/main.py](jira_status_report/main.py), [jira_status_report/report_builder.py](jira_status_report/report_builder.py)

## 2. Team Sprint Dashboard

**Goal:** Give the team ongoing visibility into sprint progress, including individual workload.

| Requirement | Decision |
|---|---|
| Format | Confluence page (separate, dedicated page) |
| Update frequency | Daily (scheduled) |
| Content | Sprint overview + per-assignee breakdown |
| Visual style | Plain tables (no charts, to keep automation simple/reliable) |
| Scope | Same project/board: `SCRUM`, active sprint |
| Authentication | Same API token/`.env` setup as the status report |

**Implementation:** [jira_status_report/dashboard_main.py](jira_status_report/dashboard_main.py), [jira_status_report/dashboard_builder.py](jira_status_report/dashboard_builder.py)

## 3. Shared Components

- [jira_client.py](jira_status_report/jira_client.py) — board lookup, active sprint lookup, sprint issue fetch (used by both automations)
- [confluence_client.py](jira_status_report/confluence_client.py) — overwrites a Confluence page's content by ID, auto-incrementing version
- [.env.example](jira_status_report/.env.example) — configuration template (site, project key, page IDs, story points field)

## 4. Open Items / Follow-ups

- Confirm actual Confluence page IDs for both the status report and dashboard pages, and set them in `.env`.
- Verify the correct Jira custom field ID for story points on this instance (`JIRA_STORY_POINTS_FIELD`, defaults to `customfield_10016`).
- Set up two separate scheduled tasks: weekly (status report) and daily (dashboard).
- Not yet in scope: burndown charts and multi-sprint velocity trends (would require storing historical snapshots) — deferred for a future iteration.
