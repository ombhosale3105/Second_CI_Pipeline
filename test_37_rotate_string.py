from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("37_rotate_string.py")
SPEC = spec_from_file_location("rotate_string_program", MODULE_PATH)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_rotate_right():
    assert MODULE.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_by_string_length():
    assert MODULE.rotate_string("hello", 5) == "hello"


def test_empty_string():
    assert MODULE.rotate_string("", 3) == ""
