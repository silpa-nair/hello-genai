from aggregate_report_builder import build_aggregate_report


SPRINT = {"name": "Sprint 12"}
STORY_POINTS_FIELD = "customfield_10016"


def _issue(points, done, key="ISSUE-1"):
    return {
        "key": key,
        "fields": {
            STORY_POINTS_FIELD: points,
            "status": {"statusCategory": {"key": "done" if done else "indeterminate"}},
        },
    }


def test_build_aggregate_report_normal_case():
    issues = [_issue(3, True, "A-1"), _issue(5, False, "A-2")]

    html = build_aggregate_report(SPRINT, issues, STORY_POINTS_FIELD)

    assert "Sprint 12" in html
    assert "<td>8.0</td>" in html
    assert "<td>3.0</td>" in html
    assert "37.5%" in html


def test_build_aggregate_report_empty_sprint():
    html = build_aggregate_report(SPRINT, [], STORY_POINTS_FIELD)

    assert "<td>0</td><td>0</td><td>0.0%</td>" in html
    assert "0.0" in html


def test_build_aggregate_report_missing_story_points_field():
    issue = _issue(None, True, "A-1")
    issue["fields"].pop(STORY_POINTS_FIELD)

    html = build_aggregate_report(SPRINT, [issue], STORY_POINTS_FIELD)

    assert "<td>1</td><td>1</td>" in html
