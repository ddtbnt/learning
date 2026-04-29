from typing import Dict, Any

from ...nodes_core.base_node import BaseNode
from ...engine.llm_client import LLMClient
from ...engine.retry_policy import RetryPolicy
from ...engine.tool_registry import tool_registry


class QuestionMapperNode(BaseNode):
    """
    Map knowledge content sang câu hỏi PMP.

    Vai trò:
    - xác định concept cần hỏi
    - sinh blueprint câu hỏi
    - chuẩn bị input cho exam builder
    """

    def __init__(self, name: str = "question_mapper_node"):
        super().__init__(name=name)

        self.llm = LLMClient()
        self.retry = RetryPolicy()

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        knowledge_content = context.get("knowledge_content", "")

        if not knowledge_content:
            raise ValueError("knowledge_content is empty")

        prompt = self._build_prompt(knowledge_content)

        mapped_questions = self.retry.execute(
            self.llm.chat,
            prompt
        )

        context["question_mapping"] = mapped_questions

        return context

    def _build_prompt(self, knowledge_content: str) -> str:
        template_path = (
            "06_AI_WORKFLOW_ENGINE/prompts/exam_prompt.md"
        )

        template = tool_registry.execute(
            "read_file",
            template_path
        )

        return template.replace(
            "{{KNOWLEDGE_CONTENT}}",
            knowledge_content
        )