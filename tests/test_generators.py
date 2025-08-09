import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


def test_filter_by_currency_usd(sample_transactions: list) -> None:
    """
    Проверка транзации по USD
    """
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 3
    assert {tran["id"] for tran in result} == {939719570, 142264268, 895315941}


def test_filter_by_currency_eur(sample_transactions: list) -> None:
    """
    Проверка транзации по RUB
    """
    result = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(result) == 2
    assert {tran["id"] for tran in result} == {873106923, 594226727}


def test_filter_empty():
    """
    Проверка на пустую тразакцию
    """
    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0


def tets_filter_not_transaction():
    """
    Проверка на тразакцию по несущетсвующей валюте
    """
    result = list(filter_by_currency(sample_transactions, "TUR"))
    assert len(result) == 0


def test_transaction_descriptions(sample_transactions: list) -> None:
    """
    Проверка на описание транзации. Должны выводиться все 5 описаний транзакции
    """
    result = list(transaction_descriptions(sample_transactions))
    assert len(result) == 5

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected_descriptions


@pytest.mark.parametrize("start,stop,expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (1, 4, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]),
    (5, 5, ["0000 0000 0000 0005"]),
    (99999999, 100000000, ["0000 0000 9999 9999", "0000 0001 0000 0000"]),
    (1000, 1003, ["0000 0000 0000 1000", "0000 0000 0000 1001", "0000 0000 0000 1002", "0000 0000 0000 1003"]),
])
def test_card_number_generator(start, stop, expected):
    cards = list(card_number_generator(start, stop))
    assert cards == expected
    assert list(card_number_generator(99999999, 100000000)) == ["0000 0000 9999 9999", "0000 0001 0000 0000"]
    assert list(card_number_generator(1, 0)) == []
