from typing import Dict, Any

from ...nodes_core.base_node import BaseNode
from ...engine.llm_client import LLMClient
from ...engine.retry_policy import RetryPolicy
from ...engine.tool_registry import tool_registry


class StandardizerNode(BaseNode):
    """
    Chuẩn hóa nội dung học PMP bằng AI.

    Vai trò:
    - làm sạch nội dung
    - chuẩn hóa markdown
    - đồng bộ cấu trúc EN / VI
    """

    def __init__(self, name: str = "standardizer_node"):
        super().__init__(name=name)

        self.llm = LLMClient()
        self.retry = RetryPolicy()

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        raw_content = context.get("raw_content", "")

        if not raw_content:
            raise ValueError("raw_content is empty")

        prompt = self._build_prompt(raw_content)

        standardized_text = self.retry.execute(
            self.llm.chat,
            prompt
        )

        context["standardized_output"] = standardized_text

        return context

    def _build_prompt(self, raw_content: str) -> str:
        """
        Load prompt template + inject raw content.
        """
        template_path = (
            "06_AI_WORKFLOW_ENGINE/prompts/standardize_prompt.md"
        )

        template = tool_registry.execute("read_file", template_path)

        return template.replace("{{RAW_CONTENT}}", raw_content)