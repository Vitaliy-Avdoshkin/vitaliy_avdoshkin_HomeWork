import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")

# Обозначаем переменную, содержащую информацию о транзакции

transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {"name": "руб.", "code": "RUB"},
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


def transactions_amount(transaction: dict) -> float:
    """Функция принимает на вход id транзакции и возвращает сумму в РУБ. Курс валюты функция импортирует через API"""

    currency = transaction["operationAmount"]["currency"].get("code")
    amount = transaction["operationAmount"].get("amount")

    if currency == "RUB":
        return float(amount)
    else:

        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"

        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers)

        result = response.json()

        return round(result["rates"].get("RUB") * float(amount), 2)

    return amount


# print(transactions_amount(transaction))
