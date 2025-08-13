import json
import logging
import os
from typing import Dict, Any

from src.external_api import get_converter

# Создание папки logs, если она не существует
if not os.path.exists('logs'):
    os.makedirs('logs')

# Настройка логирования
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8', mode='w')
file_handler.setLevel(logging.DEBUG)

# Форматирование логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логеру
logger.addHandler(file_handler)


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
                logger.info(f"Данные из файла загружены: {path_file}")
            except json.JSONDecodeError:
                logger.error(f"Ошибка декодирования в файле: {path_file}")
                print(f"Ошибка декодирования в файле {path_file}")
                return False
    except FileNotFoundError:
        logger.error(f"Файл не найден: {path_file}")
        print(f"Файл {path_file} не найден")
        return False

    return True


def get_amount_transaction(transaction: Dict[str, Any]):
    """
    функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float
    """
    logger.info("Работает функция транзакции")
    amount = transaction.get("operationAmount").get("amount")
    currency = transaction.get("operationAmount").get("currency").get("code")

    logger.info(f"Транзакции по {currency} валюте")
    if currency == "RUB":
        return amount
    elif currency in ["USD", "EUR"]:
        converter_result = get_converter(currency, amount)
        return converter_result
    else:
        return "Выбранная вылюта неизвестна"


# if __name__ == '__main__':
#     os.path.join('data', 'operations.json')
