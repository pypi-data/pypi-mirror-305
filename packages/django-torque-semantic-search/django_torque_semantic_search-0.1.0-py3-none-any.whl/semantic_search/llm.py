import requests
from django.conf import settings


class LLM:
    def __init__(self):
        self.api_base = getattr(settings, "SEMANTIC_SEARCH_EMBEDDING_API_BASE_URL")
        self.api_key = getattr(settings, "SEMANTIC_SEARCH_EMBEDDING_API_KEY")

    def get_embeddings(self, texts, *, prompt_name=None) -> list[list[float]]:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"input": texts}
        if prompt_name:
            data["type"] = prompt_name

        response = requests.post(
            f"{self.api_base}/embeddings", json=data, headers=headers
        )

        payload = response.json()
        results = payload.get("data", [])
        embeddings = [result.get("embedding") for result in results]

        return embeddings


llm = LLM()
