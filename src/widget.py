from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция общей маскировки карты и счета"""

    account_number = account_info[account_info.rfind(" ") + 1:]

    if "Счет" in account_info:
        return (
            account_info[: account_info.rfind(" ")]
            + " "
            + get_mask_account(account_number)
        )
    else:
        return (
            account_info[: account_info.rfind(" ")]
            + " "
            + get_mask_card_number(account_number)
        )


print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Счет 73654108430135874305"))


# def get_data(datatime: str) -> str:
#     """Функция преобразования даты"""
#
#     return f"{datatime[8:10]}.{datatime[5:7]}.{datatime[:4]} "
#
#
# print(get_data("2018-07-11T02:26:18.671407"))


"TASK 2 second method"

def get_data(date: str) -> str:
    """Функция преобразования даты"""

    date_update = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date_update.strftime("%d-%m-%Y")


print(get_data("2018-07-11T02:26:18.671407"))

