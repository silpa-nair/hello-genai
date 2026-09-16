# Project Specification: Contributor Analytics Dashboard

## 1. Overview

**Purpose:** Give the Scrum master (managing 15 people on the Regional Pricing Project) visibility into team activity across Jira and Confluence, primarily to support **workload balancing** decisions.

**Owner/audience:** Scrum master (primary user); team sees aggregate-only data.

## 2. Goals

- Surface per-sprint activity and workload signals to help redistribute work fairly.
- Combine signal from both Jira (issue delivery, cycle time) and Confluence (collaboration activity).
- Keep individual-level data private to the Scrum master; team-facing views show aggregates only.

## 3. Data Sources & Scope

| Source | Data used |
|---|---|
| Jira Cloud REST API | Issues completed, story points delivered, time-in-status / cycle time per issue |
| Confluence REST API | (Combined with Jira per stakeholder decision — specific Confluence activity types TBD, see Open Items) |
| Project | Jira project key: `SCRUM` (Regional Pricing Project) |
| Confluence space | Same Atlassian site (`https://silpa-nair.atlassian.net`) — **space key to be confirmed** (see Open Items) |
| Team roster | Fixed list of 15 team members' Jira account IDs — to be supplied as a mapping file/config |

## 4. Metrics

Per contributor, per sprint:
- Issues completed
- Story points delivered
- Average/total time-in-status (cycle time) per issue

Team-level aggregates (visible to everyone):
- Total issues completed, total story points, sprint completion %
- No per-person breakdown in the aggregate view

## 5. Granularity & Refresh

- **Granularity:** Per sprint (aligned with active sprint, matching existing sprint automations)
- **Update frequency:** Daily (scheduled job re-publishes both pages using the latest data for the active sprint)

## 6. Output Format & Visibility Model

**Format:** Confluence pages (reusing the existing Jira/Confluence API integration already built for the status report and team dashboard).

**Two-page model to protect privacy:**
1. **Team-facing aggregate page** — sprint-level totals only, no per-person data, visible to the whole team/space.
2. **Restricted individual-detail page** — per-contributor breakdown (issues, points, cycle time), Confluence page-level view restriction limited to the Scrum master only.

> Page-level restrictions must be configured in Confluence (Page → Restrictions → Viewers) to enforce that only the Scrum master account can view the individual-detail page. This should be verified manually after each page is created, since the REST API can set restrictions but they should be double-checked in the UI initially.

## 7. Authentication

- Reuses the existing API token approach: Atlassian API token + email via HTTP Basic Auth, loaded from `.env` (not committed to git).

## 8. Non-Goals / Explicitly Out of Scope (for now)

- Full transparency of individual metrics to the whole team.
- Historical multi-sprint trend charts (deferred, would require persisting daily/sprint snapshots).
- Any automated performance scoring or ranking — this dashboard surfaces raw activity data only, not judgments.

## 9. Open Items / Inputs Needed Before Build

- [ ] Confirm the actual Confluence **space key** for the Regional Pricing Project (a site URL was provided, not a space key).
- [ ] Confirm the exact Confluence activity types to track (e.g., page creates vs. edits vs. comments) — noted as "combine both" but specific metrics weren't finalized.
- [ ] Provide the 15 team members' Jira account IDs (roster mapping) so the dashboard can reliably resolve display names / filter out non-team assignees.
- [ ] Confluence page IDs for the two target pages (aggregate + restricted detail) — created once, then reused/updated on each run.
- [ ] Verify the Jira custom field ID for story points on this instance (defaults to `customfield_10016` in existing automations).

## 10. Relationship to Existing Automations

This dashboard extends the same integration pattern used by:
- [jira_status_report/jira_client.py](jira_status_report/jira_client.py) — board/active sprint/issue lookups (reused as-is)
- [jira_status_report/confluence_client.py](jira_status_report/confluence_client.py) — page update logic (reused as-is)
- [jira_status_report/dashboard_builder.py](jira_status_report/dashboard_builder.py) — existing per-assignee breakdown logic is a starting point, but will need a privacy-aware split into two report builders (aggregate vs. restricted detail) plus cycle-time and Confluence-activity calculations.
