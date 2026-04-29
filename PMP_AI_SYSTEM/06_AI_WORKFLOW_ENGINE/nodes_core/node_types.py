from enum import Enum


class NodeType(str, Enum):
    """
    Phân loại node trong hệ thống LangGraph.

    Dùng để routing execution, debug và tối ưu pipeline.
    """

    LLM = "llm"              # node gọi AI model (Qwen3.5)
    IO = "io"                # node đọc/ghi file, json, markdown
    LOGIC = "logic"          # node xử lý logic thuần (python)
    VALIDATION = "validation" # node kiểm tra dữ liệu
    TRANSFORM = "transform"   # node chuyển đổi dữ liệu
    ROUTER = "router"         # node điều hướng graph
    UTILITY = "utility"      # tool/helper node


class NodeStatus(str, Enum):
    """
    Trạng thái thực thi của node.
    """

    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    RETRYING = "retrying"