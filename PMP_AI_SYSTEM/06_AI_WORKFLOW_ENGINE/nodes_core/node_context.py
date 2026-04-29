from typing import Any, Dict, Optional
from dataclasses import dataclass, field


@dataclass
class NodeContext:
    """
    Context object dùng để truyền xuyên suốt giữa các nodes trong LangGraph pipeline.

    Đây là lớp giúp tách STATE runtime khỏi logic node,
    tránh việc node thao tác trực tiếp vào global state.
    """

    state: Dict[str, Any] = field(default_factory=dict)

    metadata: Dict[str, Any] = field(default_factory=dict)

    trace_id: Optional[str] = None

    current_node: Optional[str] = None

    def get(self, key: str, default: Any = None) -> Any:
        """
        Lấy giá trị từ state.
        """
        return self.state.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Ghi giá trị vào state.
        """
        self.state[key] = value

    def update(self, data: Dict[str, Any]) -> None:
        """
        Update nhiều giá trị cùng lúc.
        """
        self.state.update(data)

    def add_metadata(self, key: str, value: Any) -> None:
        """
        Lưu metadata phục vụ debug / tracing / logging.
        """
        self.metadata[key] = value

    def copy(self) -> "NodeContext":
        """
        Clone context (dùng khi branch graph).
        """
        return NodeContext(
            state=self.state.copy(),
            metadata=self.metadata.copy(),
            trace_id=self.trace_id,
            current_node=self.current_node
        )