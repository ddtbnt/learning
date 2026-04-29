# 06_AI_WORKFLOW_ENGINE/nodes_core/base_node.py

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseNode(ABC):
    """
    Abstract Node chuẩn cho toàn bộ LangGraph system

    Mọi node (loader, analyzer, enrich...) đều phải inherit từ class này
    """

    def __init__(self, name: str):
        self.name = name

    # =========================
    # CORE EXECUTION METHOD
    # =========================
    def __call__(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        LangGraph sẽ gọi node qua __call__
        """

        try:
            print(f"[NODE START] {self.name}")

            updated_state = self.run(state)

            print(f"[NODE END] {self.name}")

            return updated_state

        except Exception as e:
            return self.handle_error(state, e)

    # =========================
    # MAIN LOGIC (MUST IMPLEMENT)
    # =========================
    @abstractmethod
    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Logic chính của node
        """
        pass

    # =========================
    # ERROR HANDLING
    # =========================
    def handle_error(self, state: Dict[str, Any], error: Exception) -> Dict[str, Any]:
        """
        Default error handler cho tất cả node
        """

        if "errors" not in state:
            state["errors"] = []

        state["errors"].append({
            "node": self.name,
            "error": str(error)
        })

        print(f"[NODE ERROR] {self.name}: {error}")

        return state

    # =========================
    # OPTIONAL HOOKS
    # =========================
    def before_run(self, state: Dict[str, Any]):
        """
        Hook trước khi chạy node
        """
        pass

    def after_run(self, state: Dict[str, Any]):
        """
        Hook sau khi chạy node
        """
        pass