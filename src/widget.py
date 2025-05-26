from typing import Optional


def mask_account_card(user_number: str) -> Optional[str]:
   """Функция, которая обрабатывает информацию как о картах, так и о счетах"""
   count_result: str

   if 'счет' in user_number.lower():
       count_result = user_number[:5] + (len(user_number[-6:-4]) * "*") + user_number[-4:]
       #return count_result
   else:
       card_number =  user_number[-16:]
       new_card_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
       name_card = user_number[:-16]
       card_number_result = " ".join(new_card_number[i * 4: (i + 1) * 4] for i in range(4))
       count_result = name_card + card_number_result

   return count_result


def get_date(user_date: str) -> Optional[str]:
    """Функция, которая работает с датой вводимой с клавиатуры и возвращает строку в формате "ДД.ММ.ГГГГ"""
    #2024-03-11T02:26:18.671407
    new_date = user_date[8:10] + "." + user_date[5:7] + "." +user_date[:4]

    return new_date


user_number = input("Введите номер счета или данные карты:")
account_card = mask_account_card(user_number)
print(account_card)

user_date = input("Введите дату:")
current_datetime = get_date(user_date)
print(current_datetime)