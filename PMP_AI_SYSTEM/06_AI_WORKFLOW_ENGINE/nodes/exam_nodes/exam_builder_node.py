from typing import Dict, Any, List


from ...nodes_core.base_node import BaseNode


class ExamBuilderNode(BaseNode):
    """
    Tạo đề thi PMP hoàn chỉnh từ danh sách câu hỏi.

    Vai trò:
    - gom câu hỏi thành exam
    - sinh metadata bài thi
    - chuẩn hóa output cho Web App
    """

    def __init__(self, name: str = "exam_builder_node"):
        super().__init__(name=name)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        classified_questions = context.get("classified_questions")

        if not classified_questions:
            raise ValueError("classified_questions is empty")

        exam = self._build_exam(classified_questions)

        context["exam_output"] = exam

        return context

    def _build_exam(self, questions: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "exam_title": "PMP Mock Exam",
            "total_questions": len(questions),
            "estimated_minutes": len(questions) * 1.5,
            "questions": [
                {
                    "number": index + 1,
                    "question": item.get("question", ""),
                    "difficulty": item.get("difficulty", "medium")
                }
                for index, item in enumerate(questions)
            ]
        }