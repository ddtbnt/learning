from typing import Dict, Any

from ...nodes_core.base_node import BaseNode
from ...engine.llm_client import LLMClient
from ...engine.retry_policy import RetryPolicy
from ...engine.tool_registry import tool_registry


class EnricherNode(BaseNode):
    """
    Bổ sung kiến thức PMI vào nội dung đã chuẩn hóa.

    Vai trò:
    - thêm mindset PMP
    - bổ sung missing concepts
    - làm rõ nội dung học
    """

    def __init__(self, name: str = "enricher_node"):
        super().__init__(name=name)

        self.llm = LLMClient()
        self.retry = RetryPolicy()

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        standardized_output = context.get("standardized_output", "")

        if not standardized_output:
            raise ValueError("standardized_output is empty")

        prompt = self._build_prompt(standardized_output)

        enriched_output = self.retry.execute(
            self.llm.chat,
            prompt
        )

        context["enriched_output"] = enriched_output

        return context

    def _build_prompt(self, standardized_output: str) -> str:
        """
        Nạp prompt enrich + inject content.
        """
        template_path = (
            "06_AI_WORKFLOW_ENGINE/prompts/enrich_prompt.md"
        )

        template = tool_registry.execute("read_file", template_path)

        return template.replace(
            "{{STANDARDIZED_CONTENT}}",
            standardized_output
        )