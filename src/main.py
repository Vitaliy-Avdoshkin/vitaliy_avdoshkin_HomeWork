import os

from src.processing import filter_by_state, sort_by_date
from src.utils import (
    filter_by_currency,
    filter_by_description,
    get_transactions_info_csv,
    get_transactions_info_json,
    get_transactions_info_xlsx,
)
from src.widget import get_data, mask_account_card

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
            """Привет! Добро пожаловать в программу работыс банковскими транзакциями.
            Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
        )
    )
    while input_src not in [1, 2, 3]:
        input_src = int(
            input(
                """Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла"""
            )
        )

    else:
        if input_src == 1:
            print("Для обработки выбран JSON-файл.")
            get_info = get_transactions_info_json(abs_json_path)
        if input_src == 2:
            print("Для обработки выбран CSV-файл.")
            get_info = get_transactions_info_csv(abs_csv_path)
        if input_src == 3:
            print("Для обработки выбран XLSX-файл.")
            get_info = get_transactions_info_xlsx(abs_xlsx_path)
    get_info

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
        state_filter = filter_by_state(get_info, input_state)
        print(f"Операции отфильтрованы по статусу {input_state}")
    state_filter

    input_date_sort = str(input("Отсортировать операции по дате? Да/Нет").title())
    while input_date_sort not in ["Да", "Нет"]:
        input_date_sort = str(input("Отсортировать операции по дате? Да/Нет").title())
    else:
        if input_date_sort == "Да":
            input_ascending = str(
                input("Отсортировать по возрастанию или убыванию?").lower()
            )
            while input_ascending not in ["по возрастанию", "по убыванию"]:
                input_ascending = str(
                    input("Отсортировать по возрастанию или убыванию?").lower()
                )
            else:
                if input_ascending == "по возрастанию":
                    date_sort = sort_by_date(state_filter, descending=False)
                    date_sort
                else:
                    date_sort = sort_by_date(state_filter, descending=True)
                    date_sort

        else:
            date_sort = state_filter

    input_currency = str(input("Выводить только рублевые транзакции? Да/Нет").title())
    while input_currency not in ["Да", "Нет"]:
        input_currency = str(
            input("Выводить только рублевые транзакции? Да/Нет").title()
        )
    else:
        if input_currency == "Да":
            currency_filter = filter_by_currency(date_sort, "RUB")

        else:
            currency_filter = date_sort

    input_word_filter = str(
        input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
        ).title()
    )
    while input_word_filter not in ["Да", "Нет"]:
        input_word_filter = str(
            input(
                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
            ).title()
        )
    else:
        if input_word_filter == "Да":
            input_filter_word = str(
                input(
                    "Пожалуйста, укажите слово, по которому будет проводиться фильтрация"
                )
            )
            description_filter = filter_by_description(
                currency_filter, input_filter_word
            )
            description_filter
        else:
            description_filter = currency_filter
    print(" ")
    print("Распечатываю итоговый список транзакций...")
    print(" ")
    if len(description_filter) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(description_filter)}")
        print(" ")

        for i in description_filter:
            print(f"{get_data(i['date'])} {str(i['description'])}")
            if i["description"] == "Открытие вклада":
                print(f"Счет {mask_account_card(i['to'])}")
                print(f'Сумма: {i["operationAmount"].get('amount')}')
                print(" ")
            if i["description"] == "Перевод организации":
                print(
                    f"{mask_account_card(str(i['from']))} -> {mask_account_card(str(i['to']))}"
                )
                print(f'Сумма: {i["operationAmount"].get('amount')}')
                print(" ")
            if i["description"] == "Перевод с карты на карту":
                print(
                    f"{mask_account_card(str(i['from']))} -> {mask_account_card(str(i['to']))}"
                )
                print(f'Сумма: {i["operationAmount"].get('amount')}')
                print(" ")
            if i["description"] == "Перевод со счета на счет":
                print(
                    f"{mask_account_card(str(i['from']))} -> {mask_account_card(str(i['to']))}"
                )
                print(f'Сумма: {i["operationAmount"].get('amount')}')
                print(" ")


main()
