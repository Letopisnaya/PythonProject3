from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Функция принимает список операций и возвращает список со статусом 'EXECUTED'"""

    return [i for i in operations if i.get("state") == state]