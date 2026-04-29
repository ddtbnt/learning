from typing import Dict, Any, List

from ...nodes_core.base_node import BaseNode


class DifficultyNode(BaseNode):
    """
    Gán độ khó cho từng câu hỏi.

    Vai trò:
    - phân loại easy / medium / hard
    - cân bằng đề thi
    - chuẩn bị cho exam builder
    """

    def __init__(self, name: str = "difficulty_node"):
        super().__init__(name=name)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        question_mapping = context.get("question_mapping")

        if not question_mapping:
            raise ValueError("question_mapping is empty")

        classified_questions = self._assign_difficulty(question_mapping)

        context["classified_questions"] = classified_questions

        return context

    def _assign_difficulty(self, questions: Any) -> List[Dict[str, Any]]:
        if isinstance(questions, str):
            questions = [
                {
                    "question": line.strip()
                }
                for line in questions.splitlines()
                if line.strip()
            ]

        classified = []

        for index, item in enumerate(questions):
            difficulty = self._calculate_level(index)

            classified.append(
                {
                    **item,
                    "difficulty": difficulty
                }
            )

        return classified

    def _calculate_level(self, index: int) -> str:
        position = index % 10

        if position <= 3:
            return "easy"

        if position <= 7:
            return "medium"

        return "hard"