from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("38_missing_number_xor.py")
SPEC = spec_from_file_location("missing_number_xor_program", MODULE_PATH)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_missing_middle_number():
    assert MODULE.missing_number([3, 0, 1]) == 2


def test_missing_zero():
    assert MODULE.missing_number([1, 2, 3]) == 0


def test_missing_last_number():
    assert MODULE.missing_number([0, 1, 2, 3]) == 4
