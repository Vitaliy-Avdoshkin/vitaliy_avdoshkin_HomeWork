import os

import pytest

from src.decorators import log

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла "mylog.txt" относительно текущей директории
rel_mylog_path = os.path.join(current_dir, "../logs/mylog.txt")
abs_mylog_path = os.path.abspath(rel_mylog_path)
mylog = abs_mylog_path


def test_log_positive(capsys):
    @log(filename=mylog)
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
    @log(filename=mylog)
    def function(x, y):
        raise TypeError("My func is error")

    with pytest.raises(TypeError, match="My func is error"):
        function(1, 3)

    with open(mylog, "r") as file:
        for line in file:
            log_string = line
    assert log_string == "my_function error: My func is error. Input:(1, 3), {}\n"


def test_log_file():
    @log(filename=mylog)
    def my_function(x, y):
        return x + y

    result = my_function(1, 5)
    with open(mylog, "r") as file:
        for line in file:
            log_string = line
        assert log_string == "my_function ok\n"
        assert result == 6
