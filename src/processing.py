from typing import List, Dict


data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Функция принимает список словарей и значение ключа state(по умолчанию 'EXECUTED' и
    возращает новый список словарей, содержащий только те словари, у который ключ state
    соответствует указанному ключу"""
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция, принимает список словарей, отсортированный по дате (data)
    (по умолчанию - по убыванию)"""
    return sorted(data, key=lambda x: x['date'], reverse=reverse)


filter_executed = filter_by_state(data)
print(filter_executed)

filter_canceled = filter_by_state(data, 'CANCELED')
print(filter_canceled)

sort_date_desc = sort_by_date(data)
print(sort_date_desc)

sort_date_asc = sort_by_date(data, reverse=False)
print(sort_date_asc)
