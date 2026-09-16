import requests


class JiraClient:
    def __init__(self, site, email, api_token):
        self.base_url = f"{site.rstrip('/')}/rest/agile/1.0"
        self.auth = (email, api_token)

    def get_board_id(self, project_key):
        """Return the first board ID associated with a project key."""
        response = requests.get(
            f"{self.base_url}/board",
            params={"projectKeyOrId": project_key},
            auth=self.auth,
        )
        response.raise_for_status()
        boards = response.json()["values"]
        if not boards:
            raise ValueError(f"No board found for project '{project_key}'")
        return boards[0]["id"]

    def get_active_sprint(self, board_id):
        """Return the currently active sprint on a board, or None if there isn't one."""
        response = requests.get(
            f"{self.base_url}/board/{board_id}/sprint",
            params={"state": "active"},
            auth=self.auth,
        )
        response.raise_for_status()
        sprints = response.json()["values"]
        return sprints[0] if sprints else None

    def get_sprint_issues(self, sprint_id):
        """Return all issues in a sprint, paging through results as needed."""
        issues = []
        start_at = 0
        while True:
            response = requests.get(
                f"{self.base_url}/sprint/{sprint_id}/issue",
                params={"startAt": start_at, "maxResults": 50},
                auth=self.auth,
            )
            response.raise_for_status()
            data = response.json()
            issues.extend(data["issues"])
            start_at += len(data["issues"])
            if start_at >= data["total"] or not data["issues"]:
                break
        return issues
