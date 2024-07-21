import csv
import json
import logging
import os
from typing import Any

import pandas as pd

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)

# Создаем путь до файла JSON относительно текущей директории
rel_json_path = os.path.join(current_dir, "../data/operations.json")
abs_json_path = os.path.abspath(rel_json_path)

# Создаем путь до файла csv относительно текущей директории
rel_csv_path = os.path.join(current_dir, "../data/transactions.csv")
abs_csv_path = os.path.abspath(rel_csv_path)

# Создаем путь до файла xlsx относительно текущей директории
rel_xlsx_path = os.path.join(current_dir, "../data/transactions_excel.xlsx")
abs_xlsx_path = os.path.abspath(rel_xlsx_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_info_json(json_file: str) -> list[Any]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей"""

    with open(json_file, "r", encoding="utf-8") as file:
        try:
            logger.info("Путь до файла json верный")
            transactions_info = json.load(file)
            return transactions_info
        except:
            logger.warning("Импортируемый список пуст или отсутствует.")
            return []


# print(
#     json.dumps(
#         get_transactions_info_json(abs_json_path),
#         indent=4,
#     )
# )


def get_transactions_info_csv(input_csv_file: str) -> list[Any]:
    """Функция принимает на вход путь до файла csv и возвращает список словарей"""
    with open(input_csv_file, newline="", encoding="utf-8") as csv_file:
        result_csv = []
        dict_csv = {}
        try:
            logger.info("Путь до файла csv верный")
            reader_csv = csv.DictReader(csv_file, delimiter=";")
            for row in reader_csv:
                dict_csv["id"] = row["id"]
                dict_csv["state"] = row["state"]
                dict_csv["date"] = row["date"]
                dict_csv.update(
                    {
                        "operationAmount": {
                            "amount": row["amount"],
                            "currency": {
                                "name": row["currency_name"],
                                "code": row["currency_code"],
                            },
                        }
                    }
                )
                dict_csv["description"] = row["description"]
                dict_csv["from"] = row["from"]
                dict_csv["to"] = row["to"]
                result_csv.append(dict_csv)
            return result_csv
        except:
            logger.warning("Импортируемый список пуст или отсутствует.")
            return []


# print(
#     json.dumps(
#         get_transactions_info_csv(abs_csv_path),
#         indent=4,
#     )
# )


def get_transactions_info_xlsx(input_xlsx_file: str) -> list[Any]:
    """Функция принимает на вход путь до файла xlsx и возвращает список словарей"""

    df = pd.read_excel(abs_xlsx_path)
    result_xlsx = []
    dict_xlsx = {}

    try:
        logger.info("Путь до файла csv верный")

        # Преобразуем DataFrame в список словарей
        df_dict = df.to_dict("records")

        for i in df_dict:
            dict_xlsx["id"] = i["id"]
            dict_xlsx["state"] = i["state"]
            dict_xlsx["date"] = i["date"]
            dict_xlsx.update(
                {
                    "operationAmount": {
                        "amount": i["amount"],
                        "currency": {
                            "name": i["currency_name"],
                            "code": i["currency_code"],
                        },
                    }
                }
            )
            dict_xlsx["description"] = i["description"]
            dict_xlsx["from"] = i["from"]
            dict_xlsx["to"] = i["to"]
            result_xlsx.append(dict_xlsx)
        return result_xlsx
    except:
        logger.warning("Импортируемый список пуст или отсутствует.")
        return []


# print(
#     json.dumps(
#         get_transactions_info_xlsx(abs_xlsx_path),
#         indent=4,
#     )
# )
