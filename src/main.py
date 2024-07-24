from src.utils import (
    get_transactions_info_json,
    get_transactions_info_csv,
    get_transactions_info_xlsx,
)
from src.processing import (
    filter_by_state,
    sort_by_date,
)
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


def main():
    input_src = int(
        input(
            """Привет! Добро пожаловать в программу работы 
    с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
        )
    )
    if input_src == 1:
        print("Для обработки выбран JSON-файл.")
        result = get_transactions_info_json(abs_json_path)
    if input_src == 2:
        print("Для обработки выбран CSV-файл.")
        result = get_transactions_info_csv(abs_csv_path)
    if input_src == 3:
        print("Для обработки выбран XLSX-файл.")
        result = get_transactions_info_xlsx(abs_xlsx_path)

    input_state = str(
        input(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        ).upper()
    )
    while input_state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {input_state} недоступен.")
        input_state = str(
            input(
                """Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
            ).upper()
        )
    else:
        filter_by_state(result, input_state)
        print(f"Операции отфильтрованы по статусу {input_state}")
    input_date_sort = str(input("Отсортировать операции по дате? Да/Нет"))
    input_ascending = str(input("Отсортировать по возрастанию или убыванию?"))
    input_currency = str(input("Выводить только рублевые транзакции? Да/Нет"))
    input_word_filter = str(
        input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
        )
    )


main()
