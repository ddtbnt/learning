from typing import Callable, Dict, Optional, Type
from .base_node import BaseNode


class NodeRegistry:
    """
    Registry trung tâm quản lý tất cả nodes trong hệ thống LangGraph.

    Vai trò:
    - Đăng ký node
    - Truy xuất node theo tên
    - Hỗ trợ runtime graph builder
    """

    def __init__(self):
        self._nodes: Dict[str, Type[BaseNode]] = {}

    def register(self, name: str):
        """
        Decorator để đăng ký node class.
        """

        def wrapper(node_class: Type[BaseNode]):
            self._nodes[name] = node_class
            return node_class

        return wrapper

    def get(self, name: str) -> Optional[Type[BaseNode]]:
        """
        Lấy node class theo tên.
        """
        return self._nodes.get(name)

    def create(self, name: str, **kwargs) -> BaseNode:
        """
        Khởi tạo instance của node.
        """
        node_class = self.get(name)

        if not node_class:
            raise ValueError(f"Node '{name}' not found in registry")

        return node_class(**kwargs)

    def list_nodes(self):
        """
        Danh sách tất cả nodes đã register.
        """
        return list(self._nodes.keys())


# Global registry instance
node_registry = NodeRegistry()