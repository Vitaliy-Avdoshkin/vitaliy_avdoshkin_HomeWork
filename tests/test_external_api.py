from unittest.mock import patch

from src.external_api import transactions_amount, transaction


@patch("requests.get")
def test_transactions_amount(mock_get):

    mock_get.return_value.json.return_value = {"rates": {"RUB": 87.39642}}
    assert transactions_amount(transaction) == 718518.31
