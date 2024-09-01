import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("entered, obtained", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"), ("Счет 64686473678894779589", "Счет **9589"), ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"), ("Счет 35383033474447895560", "Счет **5560"), ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658")])
def test_mask_account_card(entered, obtained):
    assert mask_account_card(entered) == obtained

