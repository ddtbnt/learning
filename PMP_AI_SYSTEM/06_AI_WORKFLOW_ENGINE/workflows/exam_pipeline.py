from langgraph.graph import StateGraph, END

from ..nodes.exam_nodes.question_mapper_node import QuestionMapperNode
from ..nodes.exam_nodes.difficulty_node import DifficultyNode
from ..nodes.exam_nodes.exam_builder_node import ExamBuilderNode


def build_exam_pipeline():
    """
    KNOWLEDGE BASE → PMP EXAM pipeline
    """

    graph = StateGraph(dict)

    question_mapper = QuestionMapperNode()
    difficulty = DifficultyNode()
    exam_builder = ExamBuilderNode()

    graph.add_node("question_mapper", question_mapper.execute)
    graph.add_node("difficulty", difficulty.execute)
    graph.add_node("exam_builder", exam_builder.execute)

    graph.set_entry_point("question_mapper")

    graph.add_edge("question_mapper", "difficulty")
    graph.add_edge("difficulty", "exam_builder")
    graph.add_edge("exam_builder", END)

    return graph.compile()