import requests


class ConfluenceClient:
    def __init__(self, site, email, api_token):
        self.base_url = f"{site.rstrip('/')}/wiki/rest/api"
        self.auth = (email, api_token)

    def update_page(self, page_id, title, html_body):
        """Overwrite a Confluence page's content, bumping its version number."""
        current = requests.get(
            f"{self.base_url}/content/{page_id}",
            params={"expand": "version"},
            auth=self.auth,
        )
        current.raise_for_status()
        next_version = current.json()["version"]["number"] + 1

        payload = {
            "id": page_id,
            "type": "page",
            "title": title,
            "version": {"number": next_version},
            "body": {"storage": {"value": html_body, "representation": "storage"}},
        }
        response = requests.put(
            f"{self.base_url}/content/{page_id}",
            json=payload,
            auth=self.auth,
        )
        response.raise_for_status()
        return response.json()
