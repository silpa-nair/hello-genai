from detail_report_builder import build_detail_report


SPRINT = {"name": "Sprint 12"}
STORY_POINTS_FIELD = "customfield_10016"


def _issue(points, done, assignee_name, key="ISSUE-1"):
    return {
        "key": key,
        "fields": {
            STORY_POINTS_FIELD: points,
            "status": {"statusCategory": {"key": "done" if done else "indeterminate"}},
            "assignee": {"displayName": assignee_name} if assignee_name else None,
        },
    }


def test_build_detail_report_per_contributor_breakdown():
    issues = [
        _issue(3, True, "Alice", "A-1"),
        _issue(5, False, "Bob", "A-2"),
    ]

    html = build_detail_report(SPRINT, issues, STORY_POINTS_FIELD)

    assert "Alice" in html
    assert "Bob" in html
    assert "<td>Alice</td><td>1</td><td>1</td><td>100.0%</td><td>3.0</td>" in html


def test_build_detail_report_zero_activity_contributor():
    html = build_detail_report(SPRINT, [], STORY_POINTS_FIELD)

    assert '<tr><td colspan="5">None</td></tr>' in html


def test_build_detail_report_unassigned_issue():
    html = build_detail_report(SPRINT, [_issue(2, False, None, "A-1")], STORY_POINTS_FIELD)

    assert "Unassigned" in html
