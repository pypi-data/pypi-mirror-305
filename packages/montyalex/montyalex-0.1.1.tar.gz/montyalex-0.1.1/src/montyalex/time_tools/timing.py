from time import perf_counter
from functools import wraps
from typing import Callable, Any


def func_time(func_name: str, func_message: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_time: float = perf_counter()
            result: Any = func(*args, **kwargs)
            end_time: float = perf_counter()

            print(f'"{func_name}()": {end_time - start_time:.3f} seconds {func_message}')
            return result

        return wrapper

    return decorator
