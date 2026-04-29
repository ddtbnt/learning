from typing import Dict, Any

from .state_manager import StateManager
from .tool_registry import tool_registry
from ..workflows.content_pipeline import build_content_pipeline
from ..workflows.exam_pipeline import build_exam_pipeline
from ..workflows.admin_pipeline import build_admin_pipeline


class GraphRuntime:
    """
    Runtime trung tâm của LangGraph system.

    Vai trò:
    - load workflow
    - tạo initial state
    - execute pipeline
    - trả kết quả
    """

    def __init__(self):
        self.state_manager = StateManager()

        self.workflows = {
            "content": build_content_pipeline(),
            "exam": build_exam_pipeline(),
            "admin": build_admin_pipeline()
        }

    def run(self, workflow_name: str, initial_state: Dict[str, Any]):
        if workflow_name not in self.workflows:
            raise ValueError(f"Unknown workflow: {workflow_name}")

        workflow = self.workflows[workflow_name]

        state = self.state_manager.create(initial_state)

        result = workflow.invoke(state)

        return result


def main():
    runtime = GraphRuntime()

    initial_state = {
        "file_path": "sample_input.md"
    }

    result = runtime.run(
        workflow_name="content",
        initial_state=initial_state
    )

    print("Pipeline completed")
    print(result)


if __name__ == "__main__":
    main()