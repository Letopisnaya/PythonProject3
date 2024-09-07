def filter_by_currency(transaction_list: list, name: str) -> list:
    """Функция выдает список трансакций с определенной валютой"""
    for transactions in transaction_list:
        new_list_transactions = list(
            filter(
                lambda transactions: name == (transactions.get("operationAmount").get("currency").get("name")),
                transaction_list,
            )
        )
        return new_list_transactions


def transaction_descriptions(transaction_list):
    """Функция выдает описание операций"""
    description_of_transactions = ""
    for transact in transaction_list:
        description_of = transact["description"]
        description_of_transactions = description_of_transactions + description_of + "/n"
    description_of_transactions_list = description_of_transactions.split("/n")
    for transaction in description_of_transactions_list:
        yield transaction


def card_number_generator(start: int, end: int) -> str:
    """Функция генерирует номера карт"""
    for number in range(start, end + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield (formatted_card_number)
