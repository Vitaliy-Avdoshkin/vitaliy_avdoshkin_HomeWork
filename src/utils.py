import json
import logging
from typing import Any

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    r"D:\PYTHON\vitaliy_avdoshkin_HomeWork\logs\utils.log", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_info(json_file: str) -> list[Any]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей"""

    with open(json_file, "r", encoding="utf-8") as file:
        try:
            logger.info("Путь до файла json верный")
            transactions_info = json.load(file)
            return transactions_info
        except:
            logger.warning("Импортируемый список пуст или отсутствует.")
            return []


print(
    json.dumps(
        get_transactions_info(
            r"D:\PYTHON\vitaliy_avdoshkin_HomeWork\data\operations.json"
        ),
        indent=4,
    )
)

# print(get_transactions_info(r"D:\PYTHON\vitaliy_avdoshkin_HomeWork\data\operations.json"))
