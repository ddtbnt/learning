from typing import Dict, Any, List

from ...nodes_core.base_node import BaseNode


class ValidatorNode(BaseNode):
    """
    Kiểm tra output trước khi ghi ra Knowledge Base.

    Vai trò:
    - kiểm tra nội dung rỗng
    - kiểm tra heading markdown
    - kiểm tra target path
    """

    REQUIRED_KEYS = [
        "standardized_output",
        "enriched_output",
        "mapping_result"
    ]

    def __init__(self, name: str = "validator_node"):
        super().__init__(name=name)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        errors = []

        errors.extend(self._validate_required_fields(context))
        errors.extend(self._validate_markdown(context))
        errors.extend(self._validate_output_path(context))

        context["validation_status"] = {
            "valid": len(errors) == 0,
            "errors": errors
        }

        if errors:
            raise ValueError(f"Validation failed: {errors}")

        return context

    def _validate_required_fields(self, context: Dict[str, Any]) -> List[str]:
        errors = []

        for key in self.REQUIRED_KEYS:
            if not context.get(key):
                errors.append(f"Missing required field: {key}")

        return errors

    def _validate_markdown(self, context: Dict[str, Any]) -> List[str]:
        errors = []

        content = context.get("enriched_output", "")

        if not content.strip():
            errors.append("enriched_output is empty")

        if "#" not in content:
            errors.append("No markdown headings found")

        return errors

    def _validate_output_path(self, context: Dict[str, Any]) -> List[str]:
        errors = []

        mapping_result = context.get("mapping_result", {})
        target_path = mapping_result.get("target_path")

        if not target_path:
            errors.append("Missing target_path")

        return errors