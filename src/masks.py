import logging

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    "../logs\\masks.log", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""

    card_number_str = str(card_number)

    if len(card_number_str) == 16:
        logger.info("Формат карты верный")
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    else:
        logger.warning("Неверный формат банковской карты")
        return "Неверный формат банковской карты"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(accound_number: str) -> str:
    """Функция маскировки номера счета"""

    account_number_str = str(accound_number)

    if len(account_number_str) == 20:
        logger.info("Формат счета верный")
        return f"**{account_number_str[-4:]}"
    else:
        logger.warning("Неверный формат счета")
        return "Неверный формат номера счета"


print(get_mask_account("73654108430135874305"))
