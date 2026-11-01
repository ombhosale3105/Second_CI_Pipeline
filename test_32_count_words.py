import importlib

module = importlib.import_module("32_count_words")


def test_count_words_normal_sentence():
    assert module.count_words("Python is easy to learn") == 5


def test_count_words_extra_spaces():
    assert module.count_words("  Count   these   words  ") == 3


def test_count_words_punctuation():
    assert module.count_words("Hello, world! It's Python.") == 4


def test_count_words_empty_string():
    assert module.count_words("") == 0
