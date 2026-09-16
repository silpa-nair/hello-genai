from unittest.mock import patch, MagicMock

from jira_client import JiraClient


def _mock_response(json_data):
    response = MagicMock()
    response.json.return_value = json_data
    response.raise_for_status.return_value = None
    return response


@patch("jira_client.requests.get")
def test_get_board_id_returns_first_board(mock_get):
    mock_get.return_value = _mock_response({"values": [{"id": 42}, {"id": 43}]})

    client = JiraClient("https://example.atlassian.net", "user@example.com", "token")
    board_id = client.get_board_id("SCRUM")

    assert board_id == 42


@patch("jira_client.requests.get")
def test_get_board_id_raises_when_no_board(mock_get):
    mock_get.return_value = _mock_response({"values": []})

    client = JiraClient("https://example.atlassian.net", "user@example.com", "token")

    try:
        client.get_board_id("SCRUM")
        assert False, "expected ValueError"
    except ValueError:
        pass


@patch("jira_client.requests.get")
def test_get_active_sprint_returns_none_when_no_active_sprint(mock_get):
    mock_get.return_value = _mock_response({"values": []})

    client = JiraClient("https://example.atlassian.net", "user@example.com", "token")
    sprint = client.get_active_sprint(42)

    assert sprint is None


@patch("jira_client.requests.get")
def test_get_sprint_issues_pages_through_results(mock_get):
    mock_get.side_effect = [
        _mock_response({"issues": [{"key": "A-1"}], "total": 2}),
        _mock_response({"issues": [{"key": "A-2"}], "total": 2}),
    ]

    client = JiraClient("https://example.atlassian.net", "user@example.com", "token")
    issues = client.get_sprint_issues(99)

    assert [issue["key"] for issue in issues] == ["A-1", "A-2"]
