from typing import Optional


def get_mask_card_number(card_number: str) -> Optional[str]:
    """Функция, принимает на вход номер карты и возвращает ее маску."""

    card_result: str
    card_number = card_number.lstrip().rstrip()
    if card_number.isdigit() and len(card_number) == 16:
        new_card_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
        card_result = " ".join(new_card_number[i * 4:(i + 1) * 4] for i in range(4))
        return card_result
    else:
        return 'Номер карты введен неправильно'


def get_mask_account(count_number: str) -> Optional[str]:
    """Функция, принимает на вход номер счёта и возвращает его маску."""

    count_result: str
    count_number = count_number.lstrip().rstrip()
    if count_number.isdigit() and len(count_number) == 20:
        count_result = (len(count_number[-6:-4]) * "*") + count_number[-4:]
        return count_result
    else:
        return 'Номер счета введен неправильно'


# card_number = input("Введите номер карты:")
# card_code = get_mask_card_number(card_number)
# print(card_code)
#
# count_number = input("Введите номер счета:")
# count_code = get_mask_account(count_number)
# print(count_code)
