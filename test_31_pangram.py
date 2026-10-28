from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("31_pangram.py")
SPEC = spec_from_file_location("pangram_program", MODULE_PATH)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_classic_pangram():
    assert MODULE.is_pangram("The quick brown fox jumps over the lazy dog")


def test_missing_letter():
    assert not MODULE.is_pangram("Hello world")


def test_case_and_punctuation():
    assert MODULE.is_pangram("Pack my box with five dozen liquor jugs!")
