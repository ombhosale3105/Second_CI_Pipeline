from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("33_first_non_repeating.py")
SPEC = spec_from_file_location("first_non_repeating_program", MODULE_PATH)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_first_non_repeating_character():
    assert MODULE.first_non_repeating("swiss") == "w"


def test_all_repeated():
    assert MODULE.first_non_repeating("aabbcc") is None


def test_first_character_is_unique():
    assert MODULE.first_non_repeating("abcab") == "c"
