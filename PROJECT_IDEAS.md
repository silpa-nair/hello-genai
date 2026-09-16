# Jira/Confluence Automation Ideas

## 1. Automated Sprint Health Report

**Problem it solves:** Managers spend time manually checking sprint boards to answer
"are we on track?" before standups and sprint reviews. This automation pulls sprint
data on a schedule and posts a summary (story points completed vs. planned, blocked
issues, overdue tasks) to a Confluence page or Slack/email, saving manual status-gathering.

**Data needed:**
- Jira: sprint ID, issue status, story points/estimate, assignee, due date, blocker
  flags/labels (via Jira REST API `/rest/agile/1.0/sprint/{id}/issue`)
- Confluence: target page ID to publish the report to (via `/wiki/rest/api/content/{id}`)
- Historical velocity data (previous sprints' completed points) for trend comparisons

## 2. Stale Ticket / Inactivity Alert

**Problem it solves:** Tickets often sit "In Progress" with no updates for days,
hiding real blockers until it's too late. This automation scans for issues that
haven't been updated in N days and notifies the assignee and manager, reducing
tickets that silently stall.

**Data needed:**
- Jira: issue `updated` timestamp, status, assignee, project/board filter
  (via JQL query, e.g. `status = "In Progress" AND updated <= -3d`)
- Notification target: assignee email/Slack ID and manager's contact info
- Configurable staleness threshold (e.g., 3 business days) per project or issue type

## 3. Meeting Notes → Action Items Sync

**Problem it solves:** Action items captured in Confluence meeting notes often
never make it into Jira as trackable tickets, so follow-ups get lost. This
automation parses a Confluence meeting-notes page for an "Action Items" section
and auto-creates corresponding Jira tickets, linked back to the source page.

**Data needed:**
- Confluence: page content/body (storage format) of meeting notes, specifically
  a recognizable "Action Items" section (via `/wiki/rest/api/content/{id}?expand=body.storage`)
- Parsed fields per action item: description, owner, due date
- Jira: target project key, issue type (e.g., Task), and a custom field or link
  to store the originating Confluence page URL for traceability
