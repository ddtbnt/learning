from typing import Dict, Any, List

from ...nodes_core.base_node import BaseNode
from ...engine.llm_client import LLMClient
from ...engine.retry_policy import RetryPolicy
from ...engine.tool_registry import tool_registry


class MappingNode(BaseNode):
    """
    Mapping nội dung sang cấu trúc Knowledge Base.

    Vai trò:
    - map chapter → concept
    - map topic → category
    - xác định output folder
    """

    def __init__(self, name: str = "mapping_node"):
        super().__init__(name=name)

        self.llm = LLMClient()
        self.retry = RetryPolicy()

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        enriched_output = context.get("enriched_output", "")

        if not enriched_output:
            raise ValueError("enriched_output is empty")

        prompt = self._build_prompt(enriched_output)

        mapping_result = self.retry.execute(
            self.llm.chat,
            prompt
        )

        context["mapping_result"] = {
            "raw_mapping": mapping_result,
            "target_path": self._resolve_output_path(context)
        }

        return context

    def _build_prompt(self, enriched_output: str) -> str:
        template_path = (
            "06_AI_WORKFLOW_ENGINE/prompts/mapping_prompt.md"
        )

        template = tool_registry.execute("read_file", template_path)

        return template.replace(
            "{{ENRICHED_CONTENT}}",
            enriched_output
        )

    def _resolve_output_path(self, context: Dict[str, Any]) -> str:
        """
        Xác định nơi ghi file trong Knowledge Base.
        """
        file_path = context.get("file_path", "")

        return (
            "PMP_KNOWLEDGE_BASE/"
            "2_CONCEPTS_LIBRARY/"
            f"{self._safe_filename(file_path)}.md"
        )

    def _safe_filename(self, file_path: str) -> str:
        import os

        name = os.path.basename(file_path)
        name = os.path.splitext(name)[0]

        return name.replace(" ", "_").lower()