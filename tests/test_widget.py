import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "entered, obtained",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card(entered: str, obtained: str) -> None:
    assert mask_account_card(entered) == obtained


@pytest.mark.parametrize(
    "old_date, new_date", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-08-14T02:26:18.671407", "14.08.2024")]
)
def test_get_date(old_date: str, new_date: str) -> None:
    assert get_date(old_date) == new_date
