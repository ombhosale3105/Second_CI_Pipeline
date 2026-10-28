from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("36_most_frequent.py")
SPEC = spec_from_file_location("most_frequent_program", MODULE_PATH)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_most_frequent_value():
    assert MODULE.most_frequent([1, 3, 1, 2, 1, 3]) == 1


def test_tie_returns_first_most_frequent():
    assert MODULE.most_frequent(["b", "a", "b", "a"]) == "b"


def test_empty_list():
    assert MODULE.most_frequent([]) is None
