def filter_by_currency(transaction_list: list, name: str) -> list:
    for transactions in transaction_list:
        new_list_transactions = list(
            filter(
                lambda transactions: name == (transactions.get("operationAmount").get("currency").get("name")),
                transaction_list,
            )
        )
        return new_list_transactions


def transaction_descriptions(transaction_list):
    description_of_transactions = ""
    for transact in transaction_list:
        description_of = transact["description"]
        description_of_transactions = description_of_transactions + description_of + "/n"
    description_of_transactions_list = description_of_transactions.split("/n")
    for transaction in description_of_transactions_list:
        yield transaction


