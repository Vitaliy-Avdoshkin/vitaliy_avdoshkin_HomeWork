from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:

    account_number = account_info[account_info.rfind(" ") + 1 :]

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
