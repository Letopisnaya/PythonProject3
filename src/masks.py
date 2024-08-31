def get_mask_card_number(card_number: str) -> str:
    """Функция скрытия номера карты"""
    return f"{card_number[:5]} {card_number[4:6]} {"*" * 2} {"*" * 4} {card_number[12:]}"


def get_mask_account(mask_number: str) -> str:
    """Функция маскировки счета"""
    return f"{"*" * 3} {mask_number[16:]}"
