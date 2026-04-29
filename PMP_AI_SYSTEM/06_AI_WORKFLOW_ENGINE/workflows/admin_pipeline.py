from langgraph.graph import StateGraph, END

from ..nodes.content_nodes.loader_node import LoaderNode
from ..nodes.content_nodes.analyzer_node import AnalyzerNode
from ..nodes.content_nodes.enricher_node import EnricherNode
from ..nodes.content_nodes.validator_node import ValidatorNode
from ..nodes.content_nodes.writer_node import WriterNode


def build_admin_pipeline():
    """
    ADMIN pipeline dùng để:
    - enrich lại dữ liệu
    - validate lại nội dung
    - rebuild knowledge base
    """

    graph = StateGraph(dict)

    loader = LoaderNode()
    analyzer = AnalyzerNode()
    enricher = EnricherNode()
    validator = ValidatorNode()
    writer = WriterNode()

    graph.add_node("loader", loader.execute)
    graph.add_node("analyzer", analyzer.execute)
    graph.add_node("enricher", enricher.execute)
    graph.add_node("validator", validator.execute)
    graph.add_node("writer", writer.execute)

    graph.set_entry_point("loader")

    graph.add_edge("loader", "analyzer")
    graph.add_edge("analyzer", "enricher")
    graph.add_edge("enricher", "validator")
    graph.add_edge("validator", "writer")
    graph.add_edge("writer", END)

    return graph.compile()