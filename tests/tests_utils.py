from src.utils import get_transactions_info


def test_get_transactions_info():
    """Функция тестирует возврат пустого списка, если на входе список пуст"""
    assert get_transactions_info([]) == []
