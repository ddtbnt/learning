import time
from typing import Callable, Any, Optional, Type


class RetryPolicy:
    """
    Retry / fallback policy cho:
    - LLM calls
    - file operations
    - unstable nodes
    """

    def __init__(
        self,
        max_retries: int = 3,
        delay: float = 1.0,
        backoff: float = 2.0,
        exceptions: Optional[tuple[Type[Exception], ...]] = (Exception,)
    ):
        self.max_retries = max_retries
        self.delay = delay
        self.backoff = backoff
        self.exceptions = exceptions

    def execute(
        self,
        func: Callable,
        *args,
        on_retry: Optional[Callable] = None,
        **kwargs
    ) -> Any:
        attempt = 0
        current_delay = self.delay
        last_error = None

        while attempt < self.max_retries:
            try:
                return func(*args, **kwargs)

            except self.exceptions as error:
                last_error = error
                attempt += 1

                if on_retry:
                    on_retry(attempt, error)

                if attempt >= self.max_retries:
                    break

                time.sleep(current_delay)
                current_delay *= self.backoff

        raise RuntimeError(
            f"Retry failed after {self.max_retries} attempts: {last_error}"
        )

    async def execute_async(
        self,
        func: Callable,
        *args,
        on_retry: Optional[Callable] = None,
        **kwargs
    ) -> Any:
        import asyncio

        attempt = 0
        current_delay = self.delay
        last_error = None

        while attempt < self.max_retries:
            try:
                result = func(*args, **kwargs)

                if asyncio.iscoroutine(result):
                    return await result

                return result

            except self.exceptions as error:
                last_error = error
                attempt += 1

                if on_retry:
                    on_retry(attempt, error)

                if attempt >= self.max_retries:
                    break

                await asyncio.sleep(current_delay)
                current_delay *= self.backoff

        raise RuntimeError(
            f"Async retry failed after {self.max_retries} attempts: {last_error}"
        )