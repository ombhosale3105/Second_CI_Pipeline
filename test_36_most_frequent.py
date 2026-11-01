import importlib

module = importlib.import_module("36_most_frequent")


def test_most_frequent_item():
    assert module.most_frequent([1, 3, 1, 2, 1, 3]) == 1


def test_tie_uses_first_appearance():
    assert module.most_frequent(["b", "a", "b", "a"]) == "b"


def test_single_item():
    assert module.most_frequent([7]) == 7


def test_empty_list():
    assert module.most_frequent([]) is None
