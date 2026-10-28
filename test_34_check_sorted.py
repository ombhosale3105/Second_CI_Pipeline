from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("34_check_sorted.py")
SPEC = spec_from_file_location("check_sorted_program", MODULE_PATH)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_sorted_list():
    assert MODULE.is_sorted([1, 2, 2, 5])


def test_unsorted_list():
    assert not MODULE.is_sorted([1, 4, 3, 5])


def test_empty_and_single_item_lists():
    assert MODULE.is_sorted([])
    assert MODULE.is_sorted([7])
