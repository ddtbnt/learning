import requests
from typing import Dict, Any, Optional


class LLMClient:
    """
    Wrapper giao tiếp với Ollama / Qwen3.5 local model.

    Vai trò:
    - chuẩn hóa request
    - chuẩn hóa response
    - tách AI khỏi business logic
    """

    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        model: str = "qwen3.5",
        timeout: int = 180
    ):
        self.base_url = base_url
        self.model = model
        self.timeout = timeout

    def chat(
        self,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.2
    ) -> str:
        payload: Dict[str, Any] = {
            "model": self.model,
            "messages": [],
            "stream": False,
            "options": {
                "temperature": temperature
            }
        }

        if system:
            payload["messages"].append({
                "role": "system",
                "content": system
            })

        payload["messages"].append({
            "role": "user",
            "content": prompt
        })

        response = requests.post(
            f"{self.base_url}/api/chat",
            json=payload,
            timeout=self.timeout
        )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"]

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2
    ) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature
            }
        }

        response = requests.post(
            f"{self.base_url}/api/generate",
            json=payload,
            timeout=self.timeout
        )

        response.raise_for_status()

        return response.json().get("response", "")

    def health_check(self) -> bool:
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=5
            )
            return response.status_code == 200
        except Exception:
            return False

    def list_models(self):
        response = requests.get(
            f"{self.base_url}/api/tags",
            timeout=10
        )

        response.raise_for_status()

        return response.json()