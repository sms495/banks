import json
from typing import Dict, Any

from src.external_api import get_converter


def get_json_file(path_file: str) -> bool:
    """
    Функция, которая принимает на вход путь до operations.JSON-файла и возвращает список
    словарей с данными о финансовых транзакциях. Если файл пустой, содержит
    не список или не найден, функция возвращает пустой список
    """
    try:
        with open(path_file) as operations_file:
            try:
                json.load(operations_file)
            except json.JSONDecodeError:
                print(f"Ошибка декодирования в файле {path_file}")
                return False
    except FileNotFoundError:
        print(f"Файл {path_file} не найден")
        return False

    return True


def get_amount_transaction(transaction: Dict[str, Any]):
    """
    функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float
    """
    amount = transaction.get("operationAmount").get("amount")
    currency = transaction.get("operationAmount").get("currency").get("code")

    if currency == "RUB":
        return amount
    elif currency in ["USD", "EUR"]:
        converter_result = get_converter(currency, amount)
        return converter_result
    else:
        return "Выбранная вылюта неизвестна"


# if __name__ == '__main__':
#     os.path.join('data', 'operations.json')
