from src.operations import process_bank_search, process_bank_operations

test_data = [
    {'id': 1, 'amount': 1000, 'description': 'food'},
    {'id': 2, 'amount': 100, 'description': 'transport'},
    {'id': 3, 'amount': 50, 'description': 'transport'},
    {'id': 4, 'amount': 300, 'description': 'food'},
    {'id': 5, 'amount': 2000, 'description': 'food'}
]


def test_process_search_try() -> None:
    """
    Тест для поиска по категории, например, по food, сколько раз встречалось
    """
    result = process_bank_search(test_data, "food")
    assert len(result) == 3
    assert all("food" in operat["description"].lower() for operat in result)


def test_process_search_none() -> None:
    """
    Функция для поиска по категории, в данном случаи, что данной категории
    нет в перечне
    """
    result = process_bank_search(test_data, "none")
    assert len(result) == 0


def test_process_bank_search_invalid() -> None:
    """
    Функция для поиска по категории, в данном случаи, что данной категории
    нет в перечне, т.к. ошибка в написании
    """
    result = process_bank_search(test_data, "foods")
    assert result == []


def test_process_bank_operations() -> None:
    """
    Функция, которая считает количество операций в каждой категории
    """
    categories = ['food', 'transport']
    result = process_bank_operations(test_data, categories)
    assert result == {'food': 3, 'transport': 2}
