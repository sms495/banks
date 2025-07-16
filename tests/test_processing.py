import pytest

from src.processing import filter_by_state, sort_by_date

data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'NONE', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'NONE', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.mark.parametrize(
    "state",
    [
        ("EXECUTED"),
        ("CANCELED"),
        ("NONE"),
    ],
)
def test_filter_by_state(state: str, test_expected_count: int) -> None:
    """Функция принимает список словарей и значение ключа state(по умолчанию 'EXECUTED' и
        возращает новый список словарей, содержащий только те словари, у который ключ state
        соответствует указанному ключу"""
    result = filter_by_state(data, state)
    assert len(result) == test_expected_count


@pytest.mark.parametrize(
    "data, reverse",
    [
        (
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2020-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2021-10-14T08:21:33.419441'},
                {'id': 594226727, 'state': 'NONE', 'date': '2022-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'NONE', 'date': '2023-10-14T08:21:33.419441'},
            ],
            False,
        ),
        (
            [
                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2020-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2021-10-14T08:21:33.419441'},
                {'id': 594226727, 'state': 'NONE', 'date': '2022-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'NONE', 'date': '2023-10-14T08:21:33.419441'},
            ],
            True,
        ),
    ],
)
def test_sort_by_date(data: list, reverse: bool, sort_date_false: list) -> None:
    """Функция, принимает список словарей, отсортированный по дате (data)
    (по умолчанию - по убыванию)"""
    assert sort_by_date(data, False) == sort_date_false


def sort_date_true(data: list, reverse: bool, sort_date_false: list) -> None:
    """Функция, принимает список словарей, отсортированный по дате (data)
    (по умолчанию - по убыванию)"""
    assert sort_by_date(data, True) == sort_date_false
