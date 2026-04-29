from typing import Dict, Any
import re

from ...nodes_core.base_node import BaseNode


class AnalyzerNode(BaseNode):
    """
    Phân tích nội dung RAW sau khi load.

    Vai trò:
    - nhận diện cấu trúc tài liệu
    - đếm section
    - phát hiện heading
    - chuẩn bị metadata cho AI xử lý tiếp
    """

    def __init__(self, name: str = "analyzer_node"):
        super().__init__(name=name)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        raw_content = context.get("raw_content", "")

        if not raw_content:
            raise ValueError("raw_content is empty")

        headings = self._extract_headings(raw_content)

        analysis = {
            "character_count": len(raw_content),
            "line_count": len(raw_content.splitlines()),
            "heading_count": len(headings),
            "headings": headings,
            "language_hint": self._detect_language(raw_content)
        }

        context["analysis_result"] = analysis

        return context

    def _extract_headings(self, content: str):
        """
        Tìm markdown headings.
        """
        pattern = r"^(#{1,6})\s+(.*)$"
        matches = re.findall(pattern, content, re.MULTILINE)

        return [
            {
                "level": len(item[0]),
                "title": item[1].strip()
            }
            for item in matches
        ]

    def _detect_language(self, content: str) -> str:
        """
        Detect sơ bộ English / Vietnamese.
        """
        vietnamese_chars = "ăâđêôơưáàảãạấầẩẫậéèẻẽẹíìỉĩịóòỏõọúùủũụýỳỷỹỵ"

        for ch in content.lower():
            if ch in vietnamese_chars:
                return "vi"

        return "en"