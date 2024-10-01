from pathlib import Path
import pandas as pd
import csv

BASE_DIR = Path(__file__).resolve().parent.parent
join_path_csv = BASE_DIR / "data" / "transactions.csv"
join_path_exc = BASE_DIR / "data" / "transactions_excel.xlsx"

# with open('transactions.csv') as file:
#   reader = csv.DictReader(file, delimiter=';')
#  for row in reader:
#     print(row)


def transaction_read_csv(join_path_csv):
    """Функция принимает на вход путь до файла csv и возвращает список словарей с транзакциями"""
    try:
        with open(join_path_csv, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            header = next(reader)
            result = []
            for row in reader:
                row_dict = dict()
                for idx, item in enumerate(header):
                    row_dict[item] = row[idx]
                result.append(row_dict)
        return result
    except FileNotFoundError:
        transactions = []
        return transactions


def transaction_read_exsel(join_path_exc):
    """Функция принимает на вход путь до файла escel и возвращает список словарей с транзакциями"""
    try:
        transaction_excel = pd.read_excel(join_path_exc).to_dict("records")
        return transaction_excel
    except FileNotFoundError:
        transactions = []
        return transactions


print(transaction_read_csv(join_path_csv))
print(transaction_read_exsel(join_path_exc))
