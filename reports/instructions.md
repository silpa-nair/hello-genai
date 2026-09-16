# How to Fill Out the Status Report Template

Use [template.md](template.md) as your starting point for each new report. Copy it, rename it (e.g., `2026-09-17-status-report.md`), and fill in each section as follows.

## Header fields

- **Project:** The name of the project or workstream being reported on.
- **Reporting period:** The date range this report covers (e.g., a sprint or a week).
- **Prepared by:** Your name.
- **Date:** The date you're writing the report (usually the last day of the period).

## 1. Summary

Write one short paragraph a non-technical stakeholder could read in 10 seconds. State whether things are **on track**, **at risk**, or **delayed**, and why, in plain language.

## 2. Progress

Fill in one row per metric you're tracking (e.g., story points, tasks, features). For each:
- **Planned:** The target value for this period.
- **Completed:** What was actually achieved.
- **% Complete:** `Completed / Planned * 100`, rounded to one decimal place.

Add more rows if you track multiple metrics; delete the placeholder row if not needed.

## 3. Key Accomplishments

List concrete, specific things that were finished — not vague statements. Prefer "Shipped login page redesign" over "Made progress on UI."

## 4. Blockers & Risks

One row per blocker or risk. Fill in:
- **Issue:** A short ID or name (e.g., a ticket key).
- **Description:** What's blocking or at risk, in one sentence.
- **Impact:** What happens if it isn't resolved (e.g., "sprint goal missed").
- **Owner:** Who is responsible for resolving or tracking it.
- **Mitigation:** The plan or next step to address it.

If there are no blockers, replace the table with "No current blockers."

## 5. Upcoming Work

Bullet list of what's planned for the next period. Keep it high-level — this isn't a full task breakdown.

## 6. Action Items

Anything you need from the reader: a decision, an approval, input, or a resource. If there's nothing needed, remove this section.

## General tips

- Keep the whole report skimmable in under two minutes.
- Avoid jargon or internal ticket IDs without context — assume the reader doesn't have full project background.
- Be honest about risks; a report that hides problems is worse than no report at all.
