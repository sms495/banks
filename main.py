import json
from typing import Any, Dict, List

from src.operations import process_bank_search
from src.transactions import get_transactions_file_csv, get_transactions_file_xlsx
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def get_transactions_file_json(full_path: str) -> List[Dict[str, Any]]:
    """ Загружаем данные из JSON-файла и преобразует
    в унифицированный формат пригодный для Exel/CSV. """

    # Загрузка данных из JSON-файла
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Преобразование
    file_conversion = []
    for operation in data:
        if not operation:   # Пропуск пустых операций
            continue

        file_conversion.append({
            'id': operation.get('id'),
            'state': operation.get('state'),
            'date': operation.get('date'),
            'amount': operation.get('operationAmount', {}).get('amount', ''),
            'currency_name': operation.get('operationAmount', {}).get('currency', {}).get('name', ''),
            'currency_code': operation.get('operationAmount', {}).get('currency', {}).get('code', ''),
            'from': operation.get('from', ''),
            'to': operation.get('to', ''),
            'description': operation.get('description')
        })
    return file_conversion


def get_user_choice(prompt: str, valid_choices: List[str]) -> str:
    """Получает и валидирует выбор пользователя."""
    while True:
        user_input = input(f"{prompt}\nПользователь: ").strip().lower()
        for choice in valid_choices:
            if user_input == choice.lower():
                return choice
        print(f"Некорректный ввод. Пожалуйста, выберите один из вариантов: {', '.join(valid_choices)}")


def filter_rub_transactions(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Фильтрует транзакции, оставляя только рублевые."""
    return [t for t in transactions if t.get("currency_code") == "RUB"]


def print_transaction(transaction: Dict[str, Any]) -> None:
    """Форматирует и печатает информацию о транзакции в заданном формате."""
    date = get_date(transaction["date"])
    description = transaction["description"]

    # Обработка from и to
    from_account = mask_account_card(transaction["from"]) \
        if "from" in transaction and isinstance(transaction["from"], str) else "Не указано"
    to_account = mask_account_card(transaction["to"]) \
        if "to" in transaction and isinstance(transaction["to"], str) else "Не указано"

    # Получаем сумму и валюту
    amount = transaction["amount"]
    currency = transaction["currency_name"]

    # Формируем строку перевода
    transfer_line = ""
    if from_account != "Не указано" and to_account != "Не указано":
        transfer_line = f"{from_account} -> {to_account}"
    elif to_account != "Не указано":
        transfer_line = f"{to_account}"

    # Печатаем информацию о транзакции
    print(f"{date} {description}")
    if transfer_line:
        print(transfer_line)
    print(f"Сумма: {amount} {currency}\n")


def main() -> None:
    """Основная функция обработки банковских транзакций.

     Программа фильтрует данные, производит выборку операций, необходимых пользователю,
    и выводит в консоль операции, соответствующие выборке пользователя. """
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:\n'
          '1. Получить информацию о транзакциях из JSON-файла \n'
          '2. Получить информацию о транзакциях из CSV-файла \n'
          '3. Получить информацию о транзакциях из XLSX-файла \n')

    # Получаем выбор пользователя
    file_choice = input("Пользователь: ").strip()

    # Определяем путь к файлу
    transactions = []
    if file_choice == "1":
        print("\nПрограмма: Для обработки выбран JSON-файл.\n")
        transactions = get_transactions_file_json("data/operations.json")
    elif file_choice == "2":
        print("\nПрограмма: Для обработки выбран CSV-файл.\n")
        transactions = get_transactions_file_csv("data/transactions.csv")
    elif file_choice == "3":
        print("\nПрограмма: Для обработки выбран XLSX-файл.\n")
        transactions = get_transactions_file_xlsx("data/transactions_excel.xlsx")
    else:
        print("Неверный выбор. Завершение программы.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции. Файл пуст или имеет неверный формат.")
        return

    # Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию. \n"
              f"Доступные для фильтровки статусы: {', '.join(valid_statuses)} \n")
        status = input("Пользователь: ").strip().upper()

        if status in valid_statuses:
            print(f'\nПрограмма: Операции отфильтрованы по статусу "{status}" \n')
            filtered_transactions = filter_by_state(transactions, status)
            break
        else:
            print(f'\nПрограмма: Статус операции "{status}" недоступен. \n')

    if not filtered_transactions:
        print("Не найдено ни одной транзакции с указанным статусом.")
        return

    # Сортировка по дате
    sort_choice = get_user_choice("Программа: Отсортировать операции по дате? (Да/Нет) \n", ["Да", "Нет"])
    if sort_choice == "Да":
        order_choice = get_user_choice(
            "\nПрограмма: Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): \n",
            ["по возрастанию", "по убыванию"])
        reverse_sort = order_choice == "по убыванию"
        filtered_transactions = sort_by_date(filtered_transactions, reverse_sort)

    # Фильтрация по валюте
    currency_choice = get_user_choice("\nВыводить только рублевые транзакции? (Да/Нет) \n", ["Да", "Нет"])
    if currency_choice == "Да":
        filtered_transactions = filter_rub_transactions(filtered_transactions)

    # Фильтрация по ключевому слову
    search_choice = get_user_choice("\nОтфильтровать список транзакций по определенному слову в описании? (Да/Нет) \n",
                                    ["Да", "Нет"])
    if search_choice == "Да":
        search_word = input("\nВведите слово для поиска в описании: ").strip()
        filtered_transactions = process_bank_search(filtered_transactions, search_word)

    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for transaction in filtered_transactions:
            print_transaction(transaction)


if __name__ == '__main__':
    main()
