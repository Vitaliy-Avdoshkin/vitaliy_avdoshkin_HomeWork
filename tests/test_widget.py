import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_data


@pytest.mark.parametrize(
    "x",
    [
        "Visa Platinum 8990922113665229",
        "Счет 73654108430135874305",
        "Maestro 1596837868705199",
        "",
    ],
)
def test_mask_account_card(x):
    account_number = x[x.rfind(" ") + 1 :]

    if "Счет" in x:
        assert x[: x.rfind(" ")] + " " + get_mask_account(account_number)
    else:
        assert x[: x.rfind(" ")] + " " + get_mask_card_number(account_number)


def test_get_data(input_date):
    assert get_data(input_date)
