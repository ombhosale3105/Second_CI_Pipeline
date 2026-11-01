import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_middle_number():
    assert module.missing_number_xor([3, 0, 1]) == 2


def test_missing_zero():
    assert module.missing_number_xor([1, 2, 3]) == 0


def test_missing_last_number():
    assert module.missing_number_xor([0, 1, 2, 3]) == 4


def test_empty_input():
    assert module.missing_number_xor([]) == 0
