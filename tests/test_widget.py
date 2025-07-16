import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "user_number, count_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Mir 2200792289606361", "Mir 2200 79** **** 6361"),
       ],
)
def test_mask_account_card(user_number: str, count_result: str) -> None:
    """Функция, которая обрабатывает информацию как о картах, так и о счетах"""
    assert mask_account_card(user_number) == count_result


@pytest.mark.parametrize(
    "user_date, new_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-07-20T08:38:00.342334", "20.07.2020"),
        ("2025-07-14T02:08:58.425572", "14.07.2025"),
        ("2025-07-15T02:08:58.425572", "15.07.2025"),
    ],
)
def test_get_date(user_date: str, new_date: str) -> None:
    """Функция, которая работает с датой вводимой с клавиатуры и возвращает строку в формате "ДД.ММ.ГГГГ"""
    assert get_date(user_date) == new_date
