from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Функция принимает список словарей и значение ключа state(по умолчанию 'EXECUTED' и
    возращает новый список словарей, содержащий только те словари, у который ключ state
    соответствует указанному ключу"""
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция, принимает список словарей, отсортированный по дате (data)
    (по умолчанию - по убыванию)"""
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
