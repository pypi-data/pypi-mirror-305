__author__ = "xilax79"
__copyright__ = "Copyright 2024, xilax79"
__license__ = "Apache 2.0"
__version__ = "0.1.0"
__maintainer__ = "xilax79 <xilax79@gmail.com>"
__status__ = "Development"

from functools import wraps
from typing import Callable, Type, Optional

def guard(
    type: Type[Exception] = Exception, 
    h: Optional[Callable[..., None]] = None, 
    f: Optional[Callable[..., None]] = None
) -> Callable:
    """
    A decorator to wrap a function with try-except-finally logic.

    Args:
        - type: the exception type to catch (default: Exception)
        - h: handler function that processes the exception (optional)
            Args:
                - e (exception)
                - *args (function arguments)
                - **kwargs (function keyword arguments)
        - f: cleanup function executed in the 'finally' block (optional)
            Args:
                - *args (function arguments)
                - **kwargs (function keyword arguments)
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Execute the decorated function and return results
                return func(*args, **kwargs)
            except type as e:
                if h:
                    # Pass the exception and original arguments to handler
                    h(e, *args, **kwargs)
                else:
                    raise
            finally:
                if f:
                    # Execute cleanup function with the original arguments
                    f(*args, **kwargs)

        return wrapper

    return decorator
