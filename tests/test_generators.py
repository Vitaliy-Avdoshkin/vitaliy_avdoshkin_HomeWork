import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency():
    generator = filter_by_currency()
    assert next(generator) == 939719570
    assert next(generator) == 142264268



def test_transaction_descriptions():
    generator = transaction_descriptions()
    assert next(generator) == 'Перевод организации'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод со счета на счет'
    assert next(generator) == 'Перевод с карты на карту'
    assert next(generator) == 'Перевод организации'


#def test_card_number_generator():


if __name__ == '__main__':
    i = card_number_generator(1, 5)
    assert next(i) == '0000 0000 0001'
    assert next(i) == '0000 0000 0002'
    assert next(i) == '0000 0000 0003'
    assert next(i) == '0000 0000 0004'
    assert next(i) == '0000 0000 0005'


