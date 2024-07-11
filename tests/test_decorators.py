import pytest

from src.decorators import log


def test_log_positive(capsys):
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 5)
    out, _ = capsys.readouterr()
    assert "" == out
    result = my_function(1, 5)
    assert result == 6


def test_log_caps(capsys):
    @log(filename="")
    def my_function(x, y):
        return x + y

    my_function(1, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_excep():
    @log(filename="mylog.txt")
    def function(x, y):
        raise TypeError("My func is error")

    with pytest.raises(TypeError, match="My func is error"):
        function(1, 3)

    with open("mylog.txt", "r") as file:
        for line in file:
            log_string = line
    assert log_string == "my_function error: My func is error. Input:(1, 3), {}\n"


def test_log_file():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 5)
    with open("mylog.txt", "r") as file:
        for line in file:
            log_string = line
        assert log_string == "my_function ok\n"
        assert result == 6
