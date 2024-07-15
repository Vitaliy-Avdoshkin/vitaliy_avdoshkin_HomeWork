import json
from typing import Any


def get_transactions_info(json_file: str) -> list[Any]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей"""

    with open(json_file, "r", encoding="utf-8") as file:
        try:
            transactions_info = json.load(file)
            return transactions_info
        except:
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
