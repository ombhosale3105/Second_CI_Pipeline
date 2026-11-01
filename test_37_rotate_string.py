import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_left():
    assert module.rotate_string("abcdef", 2) == "cdefab"


def test_rotate_by_string_length():
    assert module.rotate_string("hello", 5) == "hello"


def test_rotate_more_than_length():
    assert module.rotate_string("abcdef", 8) == "cdefab"


def test_negative_rotation():
    assert module.rotate_string("abcdef", -2) == "efabcd"


def test_empty_string():
    assert module.rotate_string("", 3) == ""
