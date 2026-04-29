from typing import Any, Callable, Dict, Optional
import json
import os


class ToolRegistry:
    """
    Registry quản lý toàn bộ system tools.

    Vai trò:
    - đăng ký tool
    - gọi tool theo tên
    - tách system utility khỏi business node
    """

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, name: str):
        def wrapper(func: Callable):
            self._tools[name] = func
            return func
        return wrapper

    def get(self, name: str) -> Optional[Callable]:
        return self._tools.get(name)

    def execute(self, name: str, *args, **kwargs) -> Any:
        tool = self.get(name)

        if not tool:
            raise ValueError(f"Tool '{name}' not found")

        return tool(*args, **kwargs)


tool_registry = ToolRegistry()


@tool_registry.register("read_file")
def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


@tool_registry.register("write_file")
def write_file(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


@tool_registry.register("append_file")
def append_file(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "a", encoding="utf-8") as file:
        file.write(content)


@tool_registry.register("read_json")
def read_json(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


@tool_registry.register("write_json")
def write_json(path: str, data: Dict[str, Any]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


@tool_registry.register("exists_file")
def exists_file(path: str) -> bool:
    return os.path.exists(path)


@tool_registry.register("list_files")
def list_files(path: str):
    if not os.path.exists(path):
        return []

    return [
        os.path.join(path, file_name)
        for file_name in os.listdir(path)
    ]