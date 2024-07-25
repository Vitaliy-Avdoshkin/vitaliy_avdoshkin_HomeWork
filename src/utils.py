import csv
import json
import logging
import os
import re
from collections import Counter
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
            # transactions_info = list(json.load(file))
            transactions_info = json.load(file)
            return transactions_info
        except Exception:
            logger.warning("Импортируемый список пуст или отсутствует.")
            return []


# print(get_transactions_info_json(abs_json_path))


def get_transactions_info_csv(input_csv_file: str) -> list[Any]:
    """Функция принимает на вход путь до файла csv и возвращает список словарей"""
    with open(input_csv_file, newline="", encoding="utf-8") as csv_file:
        result_csv = []

        try:
            logger.info("Путь до файла csv верный")
            reader_csv = csv.DictReader(csv_file, delimiter=";")
            for row in reader_csv:
                dicts_csv = {}
                dicts_csv["id"] = row["id"]
                dicts_csv["state"] = row["state"]
                dicts_csv["date"] = row["date"]
                dicts_csv.update(
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
                dicts_csv["description"] = row["description"]
                dicts_csv["from"] = row["from"]
                dicts_csv["to"] = row["to"]
                result_csv.append(dicts_csv)
            return result_csv
        except Exception:
            logger.warning("Импортируемый список пуст или отсутствует.")
            return []


# print(get_transactions_info_csv(abs_csv_path))


def get_transactions_info_xlsx(input_xlsx_file: str) -> list[Any]:
    """Функция принимает на вход путь до файла xlsx и возвращает список словарей"""

    df = pd.read_excel(abs_xlsx_path)
    result_xlsx = []

    try:
        logger.info("Путь до файла csv верный")

        # Преобразуем DataFrame в список словарей
        df_dict = df.to_dict("records")

        for i in df_dict:
            dicts_xlsx = {}
            dicts_xlsx["id"] = i["id"]
            dicts_xlsx["state"] = i["state"]
            dicts_xlsx["date"] = i["date"]
            dicts_xlsx.update(
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
            dicts_xlsx["description"] = i["description"]
            dicts_xlsx["from"] = i["from"]
            dicts_xlsx["to"] = i["to"]
            result_xlsx.append(dicts_xlsx)
        return result_xlsx
    except Exception:
        logger.warning("Импортируемый список пуст или отсутствует.")
        return []


# print(get_transactions_info_xlsx(abs_xlsx_path))


def filter_by_description(input_list: list[Any], search_string: str) -> list[Any]:
    """Функция принимает на вход список словарей
    и возвращает список словарей, отфильтрованный по заданном слову в описании транзакций"""
    pattern = re.compile(search_string, re.IGNORECASE)
    filtered_lists = []
    for i in input_list:
        # i.get("description") == str(i.get("description"))
        match = pattern.search(str(i.get("description")))
        if match:
            filtered_lists.append(i)

    return filtered_lists


# print(filter_by_description(get_transactions_info_json(abs_json_path), 'перевод'))
# print(filter_by_description(get_transactions_info_csv(abs_csv_path), 'Перевод'))
# print(filter_by_description(get_transactions_info_xlsx(abs_xlsx_path), 'перевод'))


def categories_counter(input_list: list[Any], categories_list: list[Any]) -> dict:
    """Функция принимает на вход исходный список словарей
        и список категорий и возвращает словарь с количеством операций в каждой категории"""
    result = []
    for i in input_list:
        if i.get("description") in categories_list:
            result.append(str(i["description"]))
    count = Counter(result)
    return count


# print(
#     categories_counter(
#         get_transactions_info_csv(abs_csv_path),
#         [
#             "Перевод организации",
#             "Перевод с карты на карту",
#             "Открытие вклада",
#             "Перевод со счета на счет",
#         ],
#     )
# )


def filter_by_currency(input_list: list[Any], currency_string: str) -> list[Any]:
    """Функция принимает на вход список словарей
        и возвращает список словарей, отфильтрованный по заданной валюте"""
    pattern = re.compile(currency_string, re.IGNORECASE)
    filtered_currency_lists = []
    for i in input_list:
        if 'operationAmount' in i:
            # i.get("description") == str(i.get("description"))
            match = pattern.search(str(i.get("operationAmount")["currency"]["code"]))
            if match:
                filtered_currency_lists.append(i)

    return filtered_currency_lists


#print(filter_by_currency(get_transactions_info_json(abs_json_path), 'RUB'))
# print(filter_by_currency(get_transactions_info_csv(abs_csv_path), 'RUB'))
# print(filter_by_currency(get_transactions_info_xlsx(abs_xlsx_path), 'RUB'))
