# Module 09 Completion Report

## Tracked Files
```
WEEKLY_STATUS_REPORT_TEMPLATE.md
backlog.md
project_spec.md
```

## Backlog Commit History
```
e2d46d2 (HEAD -> master) Add implementation backlog for contributor analytics dashboard
```

## backlog.md Contents
```markdown
# Implementation Backlog: Contributor Analytics Dashboard

Derived from [project_spec.md](project_spec.md). Phases run in order (Setup → Core Features → Integration → Testing → Documentation). Tasks blocked on missing inputs are marked **(blocked)**.

## Phase 1: Setup

- [ ] Confirm the Confluence space key for the Regional Pricing Project **(blocked — needs input)**
- [ ] Provide the 15 team members' Jira account IDs (roster mapping) **(blocked — needs input)**
- [ ] Confirm which Confluence activity types to track (creates/edits/comments) **(blocked — needs input)**
- [ ] Verify the Jira story points custom field ID for this instance **(blocked — needs input)**
- [ ] Create the two target Confluence pages (aggregate + restricted detail) and record their page IDs **(blocked — needs page creation)**
- [ ] Add new `.env` variables for this project (space key, page IDs, roster file path) to `.env.example`
- [ ] Create a roster config file/module (Jira account ID → display name) once roster is provided

## Phase 2: Core Features

- [ ] Extend `jira_client.py` (or add a new module) to fetch time-in-status / cycle time per issue
- [ ] Add a Confluence activity client method to fetch page creates/edits/comments for a space over a sprint window
- [ ] Build a roster filter so only the 15 confirmed team members appear in per-contributor metrics
- [ ] Implement `aggregate_report_builder.py` — team-level totals only (no per-person data)
- [ ] Implement `detail_report_builder.py` — per-contributor breakdown (issues, points, cycle time, Confluence activity)
- [ ] Handle edge cases in report builders: no active sprint, contributor with zero activity, missing story points field

## Phase 3: Integration

- [ ] Wire aggregate builder + `ConfluenceClient.update_page` into a `main.py` entry point for the public page
- [ ] Wire detail builder + `ConfluenceClient.update_page` into a `main.py` entry point for the restricted page
- [ ] Apply Confluence page-level view restrictions to the detail page (Scrum master only) via API or manual UI step
- [ ] Manually verify restrictions in the Confluence UI after first publish (per spec's privacy requirement)
- [ ] Combine both entry points into a single daily-run script (or two scheduled tasks) matching the spec's daily cadence

## Phase 4: Testing

- [ ] Unit tests for cycle-time calculation logic (various status transition scenarios)
- [ ] Unit tests for aggregate report builder (totals, % complete, empty-sprint case)
- [ ] Unit tests for detail report builder (per-contributor breakdown, roster filtering, zero-activity contributor)
- [ ] Unit tests for Confluence activity fetching (mocked API responses)
- [ ] Manual end-to-end test: run both entry points against real Jira/Confluence data and confirm correct page content
- [ ] Manual verification that the restricted page is inaccessible to a non-Scrum-master test account

## Phase 5: Documentation

- [ ] Write a setup README covering: installing dependencies, configuring `.env`, running each entry point, and scheduling via Task Scheduler
- [ ] Document the roster config format and how to update it when team membership changes
- [ ] Document how to re-confirm/rotate the Confluence page IDs if pages are ever recreated
```
