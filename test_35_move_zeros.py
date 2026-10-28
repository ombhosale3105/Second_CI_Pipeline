from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("35_move_zeros.py")
SPEC = spec_from_file_location("move_zeros_program", MODULE_PATH)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_move_zeros_to_end():
    assert MODULE.move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_all_zeros():
    assert MODULE.move_zeros([0, 0]) == [0, 0]


def test_no_zeros():
    assert MODULE.move_zeros([1, 2, 3]) == [1, 2, 3]
