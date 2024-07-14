import os

import requests
from dotenv import load_dotenv


load_dotenv(".env")

API_KEY = os.getenv("API_KEY")

#Обозначаем переменную, содержащую информацию о транзакции

transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "\u041f\u0435\u0440\u0435\u0432\u043e\u0434 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438",
        "from": "MasterCard 7158300734726758",
        "to": "\u0421\u0447\u0435\u0442 35383033474447895560"
    }


def transactions_amount(transaction: int) -> float:
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


#print(transactions_amount(transaction))
