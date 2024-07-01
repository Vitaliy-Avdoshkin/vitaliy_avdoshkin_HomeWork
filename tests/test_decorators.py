import pytest

from src.decorators import log, my_function


def test_log_positive():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 5)
    assert result == 3


def test_log_caps(capsys):
    my_function(1, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_excep():
    with pytest.raises(Exception):
        my_function
