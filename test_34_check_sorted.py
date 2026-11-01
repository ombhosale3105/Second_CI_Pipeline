import importlib

module = importlib.import_module("34_check_sorted")


def test_sorted_list():
    assert module.is_sorted([1, 2, 3, 4]) is True


def test_unsorted_list():
    assert module.is_sorted([1, 3, 2, 4]) is False


def test_equal_values_are_sorted():
    assert module.is_sorted([2, 2, 2]) is True


def test_empty_and_single_item_lists():
    assert module.is_sorted([]) is True
    assert module.is_sorted([10]) is True
