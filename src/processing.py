from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Функция принимает список операций и возвращает список со статусом 'EXECUTED'"""

    return [i for i in operations if i.get("state") == state]


def sort_by_date(operations: list[dict[str, Any]], reverse: bool = True) -> Any:
    """Функция принимает список операций и возвращает отсортированный по дате список"""

    sort_operations_date = sorted(operations, key=lambda new_operations: new_operations["date"], reverse=reverse)
    return sort_operations_date
