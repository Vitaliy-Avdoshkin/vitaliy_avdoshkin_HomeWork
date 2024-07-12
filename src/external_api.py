import os
from typing import Any
import requests
from dotenv import load_dotenv

from src.utils import get_transactions_info

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


transactions_info = get_transactions_info(
    r"D:\PYTHON\vitaliy_avdoshkin_HomeWork\data\operations.json"
)


def transactions_amount(id_transaction: int) -> float:
    """Функция принимает на вход id транзакции и возвращает сумму в РУБ. Курс валюты функция импортирует через API"""

    for transaction in transactions_info:
        currency = transaction["operationAmount"]["currency"].get("code")

        if transaction.get("id") == id_transaction:

            if currency == "RUB":
                return float(transaction["operationAmount"].get("amount"))
            else:

                url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"

                headers = {"apikey": API_KEY}

                response = requests.get(url, headers=headers)

                result = response.json()

                return round(
                    result["rates"].get("RUB")
                    * float(transaction["operationAmount"].get("amount")),
                    2,
                )


print(transactions_amount(441945886))
print(transactions_amount(142264268))
print(transactions_amount(214024827))
print(transactions_amount(536723678))
