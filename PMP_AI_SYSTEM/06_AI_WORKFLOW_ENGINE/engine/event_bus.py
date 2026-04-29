from typing import Any, Callable, Dict, List, DefaultDict
from collections import defaultdict


class EventBus:
    """
    Event-driven system cho LangGraph engine.

    Vai trò:
    - Giao tiếp giữa các node không phụ thuộc trực tiếp
    - Hỗ trợ publish / subscribe
    - Dùng cho tracing, logging, orchestration
    """

    def __init__(self):
        self._subscribers: DefaultDict[str, List[Callable]] = defaultdict(list)

    def subscribe(self, event: str, handler: Callable) -> None:
        """
        Đăng ký handler cho event.
        """
        self._subscribers[event].append(handler)

    def unsubscribe(self, event: str, handler: Callable) -> None:
        """
        Hủy đăng ký handler.
        """
        if handler in self._subscribers[event]:
            self._subscribers[event].remove(handler)

    def publish(self, event: str, data: Dict[str, Any]) -> None:
        """
        Phát event tới tất cả subscribers.
        """
        for handler in self._subscribers[event]:
            try:
                handler(data)
            except Exception as e:
                # Không crash system vì event lỗi
                print(f"[EventBus Error] {event}: {str(e)}")

    def clear(self, event: str) -> None:
        """
        Xóa toàn bộ subscribers của event.
        """
        self._subscribers[event].clear()

    def clear_all(self) -> None:
        """
        Reset toàn bộ event system.
        """
        self._subscribers.clear()