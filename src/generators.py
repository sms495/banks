from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Функция возвращает итератор, который выдает транзакции, у которых валюта совпадает с переданной.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, который принимает список словарей с транзакциями и возращает описание каждой операций
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for num in range(start, stop + 1):
        # Переменную card_str делаем 16-значной.
        card_str = str(num).zfill(16)
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted
