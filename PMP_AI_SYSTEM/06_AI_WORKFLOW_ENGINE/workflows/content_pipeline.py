from langgraph.graph import StateGraph, END

from ..nodes.content_nodes.loader_node import LoaderNode
from ..nodes.content_nodes.analyzer_node import AnalyzerNode
from ..nodes.content_nodes.standardizer_node import StandardizerNode
from ..nodes.content_nodes.enricher_node import EnricherNode
from ..nodes.content_nodes.mapping_node import MappingNode
from ..nodes.content_nodes.validator_node import ValidatorNode
from ..nodes.content_nodes.writer_node import WriterNode


def build_content_pipeline():
    """
    RAW DATA → KNOWLEDGE BASE pipeline
    """

    graph = StateGraph(dict)

    loader = LoaderNode()
    analyzer = AnalyzerNode()
    standardizer = StandardizerNode()
    enricher = EnricherNode()
    mapper = MappingNode()
    validator = ValidatorNode()
    writer = WriterNode()

    graph.add_node("loader", loader.execute)
    graph.add_node("analyzer", analyzer.execute)
    graph.add_node("standardizer", standardizer.execute)
    graph.add_node("enricher", enricher.execute)
    graph.add_node("mapper", mapper.execute)
    graph.add_node("validator", validator.execute)
    graph.add_node("writer", writer.execute)

    graph.set_entry_point("loader")

    graph.add_edge("loader", "analyzer")
    graph.add_edge("analyzer", "standardizer")
    graph.add_edge("standardizer", "enricher")
    graph.add_edge("enricher", "mapper")
    graph.add_edge("mapper", "validator")
    graph.add_edge("validator", "writer")
    graph.add_edge("writer", END)

    return graph.compile()