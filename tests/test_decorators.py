import pytest

from src.decorators import log


# Функция для успешного тестирования
@log(filename="mylog.txt")
def successful_function(x, y):
    return x + y


# Функция с ошибкой
@log(filename="mylog.txt")
def function_with_exception(x, y):
    return x / y


def test_successful_function(capsys):
    result = successful_function(1, 2)

    # Проверяем результат функции
    assert result == 3

    # Получаем вывод из консоли
    captured = capsys.readouterr()

    # Проверяем логи
    assert "Starting successful_function with args: (1, 2) kwargs: {}" in captured.out
    assert "successful_function ok: Result: 3" in captured.out


def test_function_with_exception(capsys):
    with pytest.raises(ZeroDivisionError):
        function_with_exception(1, 0)

    # Получаем вывод из консоли
    captured = capsys.readouterr()

    # Проверяем логи
    assert "Starting function_with_exception with args: (10, 0) kwargs: {}" in captured.out
    assert "function_with_exception error: ZeroDivisionError. Inputs: (10, 0), {}" in captured.out
