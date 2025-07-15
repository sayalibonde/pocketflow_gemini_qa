from pocketflow import Flow
from nodes.gemini_node import GeminiNode

def create_flow() -> Flow:
    return Flow(start=GeminiNode())
