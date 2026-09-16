# TODO

## Phase 1: Gather Requirements & Inputs

- [ ] Confirm the Confluence space key for the Regional Pricing Project
- [ ] Confirm which Confluence activity types to track (page creates vs. edits vs. comments)
- [ ] Provide the 15 team members' Jira account IDs (roster mapping)
- [ ] Create/confirm Confluence page IDs for the aggregate and restricted-detail pages
- [ ] Verify the Jira story points custom field ID for this instance

## Phase 2: Build Core Automation

- [ ] Add cycle-time / time-in-status calculation to the Jira data pipeline
- [ ] Add Confluence activity fetching (page creates/edits/comments)
- [ ] Filter contributors to the confirmed 15-person roster
- [ ] Split dashboard builder into aggregate (team-facing) and detail (per-contributor) report builders

## Phase 3: Implement Privacy Model

- [ ] Create the two target Confluence pages (aggregate + restricted detail)
- [ ] Apply Confluence page-level view restrictions to the detail page (Scrum master only)
- [ ] Manually verify restrictions in the Confluence UI after first publish

## Phase 4: Deploy & Schedule

- [ ] Test both automations end-to-end against real data
- [ ] Schedule the daily dashboard job (Task Scheduler)
- [ ] Schedule the weekly status report job (Task Scheduler)
