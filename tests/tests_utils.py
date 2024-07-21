from src.utils import get_transactions_info_json


def test_get_transactions_info_json():
    """Функция тестирует возврат пустого списка, если на входе список пуст"""
    assert get_transactions_info_json([]) == []
