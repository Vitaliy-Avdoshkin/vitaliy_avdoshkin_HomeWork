import pytest

@pytest.mark.parametrize("x", [(7000792289606361), (8000522289606361),(700792289606361), ()])
def test_get_mask_card_number(x):
    card_number_str = str(x)
    assert f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


@pytest.mark.parametrize("x", [(73654108430135874305), (773654108430135874305), (3373654108430135874305), ()])
def test_get_mask_account(x):
    account_number_str = str(x)
    assert f"**{account_number_str[-4:]}"


