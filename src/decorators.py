import os
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
                return result
            except Exception as e:
                log_message = f"my_function error: {e}. Input:{args}, {kwargs}"
                raise e

            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")

                else:
                    print(log_message)

        return wrapper

    return decorator


# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла "mylog.txt" относительно текущей директории
rel_mylog_path = os.path.join(current_dir, "../logs/mylog.txt")
abs_mylog_path = os.path.abspath(rel_mylog_path)
mylog = abs_mylog_path


@log(filename=mylog)
def my_function(x, y):
    """Функция сложения чисел"""
    return x + y


if __name__ == "__main__":
    print(my_function(1, 3))
