from typing import Any
from functools import wraps


def log(filename: str) -> Any:
    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = "my_function ok"
                print(log_message)
            except Exception as e:
                log_message = f"my_function_ error: {e}. Input:{args}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message)

            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция сложения чисел"""
    return x + y


print(my_function(1, 2))
