from functools import wraps
from typing import Any, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор для логирования вызовов функции.
    Логирует вызов функции и её результат в файл или консоль.
    Принимает необязательный аргумент filename для указания файла логирования.
    """

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = "my_function ok"

            except Exception as e:
                log_message = f"my_function error: {e}. Input:{args}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)

            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Функция сложения чисел"""
    return x + y


if __name__ == "__main__":
    print(my_function(1, "3"))
