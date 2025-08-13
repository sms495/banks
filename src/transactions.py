from typing import Any, Dict, Hashable, List, Union
from pathlib import Path

import pandas as pd


def get_transactions_file_csv(file_csv: Union[str, Path]) -> List[Dict[Hashable, Any]]:
    """
    Функция для считывания финансовых операций из CSV.
    """

    try:
        with open(file_csv, encoding="utf-8") as file:
            excel_transaction = pd.read_csv(file, delimiter=";")
            transactions = excel_transaction.to_dict("records")
            return transactions
    except FileNotFoundError:
        print(f"Ошибка: файл {file_csv} не найден! ")
        return []
    except Exception as er:
        print(f"Ошибка при чтении CSV: {er}")
        return []


def get_transactions_file_xlsx(file_xlsx: Union[str, Path]) -> List[Dict[Hashable, Any]]:
    """
    Функция для считывания финансовых операций из Excel.
    """

    try:
        with open(file_xlsx, encoding="utf-8"):
            excel_transaction = pd.read_excel(file_xlsx)
            transactions = excel_transaction.to_dict("records")
            return transactions
    except FileNotFoundError:
        print(f"Ошибка: файл {file_xlsx} не найден! ")
        return []
    except Exception as er:
        print(f"Ошибка при чтении XLSX: {er}")
        return []
