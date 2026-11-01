import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating_character():
    assert module.first_non_repeating("swiss") == "w"


def test_first_character_is_unique():
    assert module.first_non_repeating("abcdef") == "a"


def test_no_non_repeating_character():
    assert module.first_non_repeating("aabbcc") is None


def test_empty_string():
    assert module.first_non_repeating("") is None
