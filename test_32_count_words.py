from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("32_count_words.py")
SPEC = spec_from_file_location("count_words_program", MODULE_PATH)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_normal_sentence():
    assert MODULE.count_words("Python is easy to learn") == 5


def test_extra_spaces():
    assert MODULE.count_words("  count   these words  ") == 3


def test_empty_sentence():
    assert MODULE.count_words("") == 0
