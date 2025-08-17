from src.utils import get_amount_transaction

from unittest.mock import patch


def test_get_amount_transaction_rub() -> None:
    """
    Тестирование транзакций в валюте RUB
    """
    assert (get_amount_transaction({"operationAmount": {"amount": "31957.58", "currency": {"code": "RUB"}}})
            == "31957.58"
            )
    assert (get_amount_transaction({"operationAmount": {"amount": "48223.05", "currency": {"code": "RUB"}}})
            == "48223.05"
            )


@patch('requests.get')
def test_get_amount_transactions_usd(return_mock):
    """
    Тестирование транзакций в валюте USD
    """
    # with patch("requests.get") as return_mock:
    return_mock.return_value.json.return_value = {'result': 123456}
    assert (
            get_amount_transaction({"operationAmount": {"amount": "8221.37", "currency": {"code": "USD"}}})
            == 123456
        )


def test_get_amount_transactions_unknown() -> None:
    """
    Тестирование транзакции в неизвестной валюте
    """
    assert (
            get_amount_transaction({"operationAmount": {"amount": "12345.11", "currency": {"code": "TUR"}}})
            == "Выбранная вылюта неизвестна"
    )
