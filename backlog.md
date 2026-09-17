# Implementation Backlog: Contributor Analytics Dashboard

Derived from [project_spec.md](project_spec.md). Phases run in order (Setup → Core Features → Integration → Testing → Documentation). Tasks blocked on missing inputs are marked **(blocked)**.

## Phase 1: Setup

- [ ] Confirm the Confluence space key for the Regional Pricing Project **(blocked — needs input)** — *custom skill*
- [ ] Provide the 15 team members' Jira account IDs (roster mapping) **(blocked — needs input)** — *custom skill*
- [ ] Confirm which Confluence activity types to track (creates/edits/comments) **(blocked — needs input)** — *custom skill*
- [ ] Verify the Jira story points custom field ID for this instance **(blocked — needs input)** — *MCP*
- [ ] Create the two target Confluence pages (aggregate + restricted detail) and record their page IDs **(blocked — needs page creation)** — *MCP*
- [ ] Add new `.env` variables for this project (space key, page IDs, roster file path) to `.env.example` — *custom skill*
- [ ] Create a roster config file/module (Jira account ID → display name) once roster is provided — *custom skill*

## Phase 2: Core Features

- [ ] Extend `jira_client.py` (or add a new module) to fetch time-in-status / cycle time per issue — *MCP for the raw fetch, custom skill for the cycle-time calculation*
- [ ] Add a Confluence activity client method to fetch page creates/edits/comments for a space over a sprint window — *MCP*
- [ ] Build a roster filter so only the 15 confirmed team members appear in per-contributor metrics — *custom skill*
- [ ] Implement `aggregate_report_builder.py` — team-level totals only (no per-person data) — *custom skill*
- [ ] Implement `detail_report_builder.py` — per-contributor breakdown (issues, points, cycle time, Confluence activity) — *custom skill*
- [ ] Handle edge cases in report builders: no active sprint, contributor with zero activity, missing story points field — *custom skill*

## Phase 3: Integration

- [ ] Wire aggregate builder + `ConfluenceClient.update_page` into a `main.py` entry point for the public page — *custom skill*
- [ ] Wire detail builder + `ConfluenceClient.update_page` into a `main.py` entry point for the restricted page — *custom skill*
- [ ] Apply Confluence page-level view restrictions to the detail page (Scrum master only) via API or manual UI step — *MCP*
- [ ] Manually verify restrictions in the Confluence UI after first publish (per spec's privacy requirement) — *custom skill*
- [ ] Combine both entry points into a single daily-run script (or two scheduled tasks) matching the spec's daily cadence — *custom skill*

## Phase 4: Testing

- [ ] Unit tests for cycle-time calculation logic (various status transition scenarios) — *custom skill*
- [ ] Unit tests for aggregate report builder (totals, % complete, empty-sprint case) — *custom skill*
- [ ] Unit tests for detail report builder (per-contributor breakdown, roster filtering, zero-activity contributor) — *custom skill*
- [ ] Unit tests for Confluence activity fetching (mocked API responses) — *custom skill*
- [ ] Manual end-to-end test: run both entry points against real Jira/Confluence data and confirm correct page content — *custom skill*
- [ ] Manual verification that the restricted page is inaccessible to a non-Scrum-master test account — *custom skill*

## Phase 5: Documentation

- [ ] Write a setup README covering: installing dependencies, configuring `.env`, running each entry point, and scheduling via Task Scheduler — *custom skill*
- [ ] Document the roster config format and how to update it when team membership changes — *custom skill*
- [ ] Document how to re-confirm/rotate the Confluence page IDs if pages are ever recreated — *custom skill*
