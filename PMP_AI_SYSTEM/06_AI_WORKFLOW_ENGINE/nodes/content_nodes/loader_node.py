from typing import Dict, Any
from pathlib import Path

from ...engine.tool_registry import tool_registry
from ...nodes_core.base_node import BaseNode


class LoaderNode(BaseNode):
    """
    Node đầu tiên trong pipeline RAW → KNOWLEDGE.

    Vai trò:
    - Đọc dữ liệu đầu vào (Markdown / JSON / TXT)
    - Chuẩn hóa input vào STATE
    """

    def __init__(self, name: str = "loader_node"):
        super().__init__(name=name)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Input:
            context["file_path"]

        Output:
            context["raw_content"]
            context["source_type"]
        """

        file_path = context.get("file_path")

        if not file_path:
            raise ValueError("file_path is required")

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        content = tool_registry.execute("read_file", file_path)

        file_ext = path.suffix.lower()

        if file_ext == ".json":
            source_type = "json"
        elif file_ext == ".md":
            source_type = "markdown"
        else:
            source_type = "text"

        context["raw_content"] = content
        context["source_type"] = source_type

        return context