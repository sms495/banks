from typing import Any, Dict, Hashable, List
from unittest.mock import patch
from src.transactions import get_transactions_file_csv, get_transactions_file_xlsx


def test_get_transactions_file_xlsx() -> None:
    """
    Функция для тестирования *.xlsx файла (если все хорошо: файл есть, данные присутствуют).
    """
    with patch("pandas.read_excel") as mock_read:
        mock_read.return_value.to_dict.return_value = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        result: List[Dict[Hashable, Any]] = get_transactions_file_xlsx("../data/transactions_excel.xlsx")
        assert result == [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]


def test_get_transactions_file_csv() -> None:
    """
    Функция для тестирования *.csv файла (если все хорошо: файл есть, данные присутствуют).
    """
    with patch("pandas.read_csv") as mock_read:
        mock_read.return_value.to_dict.return_value = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        result: List[Dict[Hashable, Any]] = get_transactions_file_csv("../data/transactions.csv")
        assert result == [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]


def test_get_transactions_file_xlsx_missing() -> None:
    """
    Функция, в которой проверяется, что нужный файл *.xlsx отсутствует
    """
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result: list = get_transactions_file_xlsx("../data/excel.xlsx")
        assert result == []


def test_get_transactions_file_csv_missing() -> None:
    """
    Функция, в которой проверяется, что нужный файл *.csv отсутствует
    """
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result: list = get_transactions_file_xlsx("../data/excel.csv")
        assert result == []
