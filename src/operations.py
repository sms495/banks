import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция, которая фильтрует список словарей с данными о банковских операциях, оставляя только те,
    в описании которых есть нужная строка
    """
    try:
        result = []
        for operation in data:
            if 'description' in operation and re.search(search, operation['description'], re.IGNORECASE):
                result.append(operation)
        return result
    except re.error:
        return []


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция, которая считает количество операций в каждой категории
    """
    counter = Counter()
    for operation in data:
        description = operation.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                counter[category] += 1
    return dict(counter)
