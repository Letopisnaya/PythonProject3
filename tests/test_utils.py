import os

import pytest

from src.utils import file_opening


@pytest.fixture
def path_to_file():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


@pytest.fixture
def path_to_file_empty():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_empty.json")


def test_file_opening_empty(path_to_file_empty):
    assert file_opening(path_to_file_empty) == []


def test_file_opening(path_to_file):
    assert file_opening(path_to_file)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB", "name": "руб."}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
