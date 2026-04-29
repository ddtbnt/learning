from typing import Any, Dict, List
import copy


class StateManager:
    """
    Quản lý STATE trung tâm cho toàn bộ AI workflow.

    Vai trò:
    - lưu state hiện tại
    - update state an toàn
    - rollback khi lỗi
    - merge dữ liệu giữa các node
    """

    def __init__(self):
        self._state: Dict[str, Any] = {}
        self._history: List[Dict[str, Any]] = []

    def get_state(self) -> Dict[str, Any]:
        """
        Trả về toàn bộ state hiện tại.
        """
        return copy.deepcopy(self._state)

    def set_state(self, state: Dict[str, Any]) -> None:
        """
        Gán state mới hoàn toàn.
        """
        self._save_history()
        self._state = copy.deepcopy(state)

    def update_state(self, data: Dict[str, Any]) -> None:
        """
        Merge dữ liệu mới vào state hiện tại.
        """
        self._save_history()
        self._state.update(data)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Lấy 1 field trong state.
        """
        return self._state.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Gán 1 field vào state.
        """
        self._save_history()
        self._state[key] = value

    def merge_state(self, new_state: Dict[str, Any]) -> None:
        """
        Merge nhiều field cùng lúc.
        """
        self._save_history()

        for key, value in new_state.items():
            self._state[key] = value

    def rollback(self, steps: int = 1) -> None:
        """
        Khôi phục state trước đó.
        """
        if len(self._history) >= steps:
            self._state = self._history[-steps]
            self._history = self._history[:-steps]

    def clear(self) -> None:
        """
        Xóa toàn bộ state.
        """
        self._save_history()
        self._state = {}

    def history_count(self) -> int:
        """
        Số lượng snapshot đã lưu.
        """
        return len(self._history)

    def _save_history(self) -> None:
        """
        Lưu snapshot trước khi thay đổi.
        """
        self._history.append(copy.deepcopy(self._state))