import asyncio
from typing import Any, Callable, Dict, List, Optional


class AsyncExecutor:
    """
    Async execution engine for running nodes in parallel or controlled concurrency.
    Used by LangGraph runtime to optimize pipeline performance.
    """

    def __init__(self, max_concurrency: int = 5):
        self.max_concurrency = max_concurrency
        self._semaphore = asyncio.Semaphore(max_concurrency)

    async def run_node(self, node: Callable, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a single node asynchronously with semaphore control.
        """
        async with self._semaphore:
            if asyncio.iscoroutinefunction(node):
                return await node(state)
            return node(state)

    async def run_nodes_sequential(
        self,
        nodes: List[Callable],
        state: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Run nodes sequentially (stateful pipeline).
        Each node updates state and passes to next node.
        """
        current_state = state

        for node in nodes:
            current_state = await self.run_node(node, current_state)

        return current_state

    async def run_nodes_parallel(
        self,
        nodes: List[Callable],
        state: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Run nodes in parallel (stateless or independent tasks).
        """

        tasks = [
            self.run_node(node, state)
            for node in nodes
        ]

        return await asyncio.gather(*tasks)

    async def run_with_retry(
        self,
        node: Callable,
        state: Dict[str, Any],
        retries: int = 3,
        delay: float = 1.0
    ) -> Dict[str, Any]:
        """
        Execute node with retry logic.
        """
        last_error = None

        for attempt in range(retries):
            try:
                return await self.run_node(node, state)
            except Exception as e:
                last_error = e
                await asyncio.sleep(delay * (attempt + 1))

        raise RuntimeError(f"Node failed after retries: {str(last_error)}")