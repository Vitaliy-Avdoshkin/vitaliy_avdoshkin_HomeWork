def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""

    card_number_str = str(card_number)

    if len(card_number_str) == 16:
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    else:
        return "Неверный формат банковской карты"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(accound_number: str) -> str:
    """Функция маскировки номера счета"""

    account_number_str = str(accound_number)

    if len(account_number_str) == 20:
        return f"**{account_number_str[-4:]}"
    else:
        return "Неверный формат номера счета"


print(get_mask_account("73654108430135874305"))
