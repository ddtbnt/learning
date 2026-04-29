from typing import Dict, Any
import os

from ...nodes_core.base_node import BaseNode
from ...engine.tool_registry import tool_registry


class WriterNode(BaseNode):
    """
    Ghi output cuối cùng vào Knowledge Base.

    Vai trò:
    - tạo folder nếu chưa có
    - ghi markdown file
    - cập nhật output path vào state
    """

    def __init__(self, name: str = "writer_node"):
        super().__init__(name=name)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        validation = context.get("validation_status", {})

        if not validation.get("valid"):
            raise ValueError("validation_status invalid")

        mapping_result = context.get("mapping_result", {})
        target_path = mapping_result.get("target_path")

        if not target_path:
            raise ValueError("target_path missing")

        content = context.get("enriched_output", "")

        self._ensure_directory(target_path)

        tool_registry.execute(
            "write_file",
            target_path,
            content
        )

        context["output_path"] = target_path

        return context

    def _ensure_directory(self, file_path: str):
        directory = os.path.dirname(file_path)

        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)