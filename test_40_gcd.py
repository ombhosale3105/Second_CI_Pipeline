from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("40_gcd.py")
SPEC = spec_from_file_location("gcd_program", MODULE_PATH)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_common_divisor():
    assert MODULE.gcd(48, 18) == 6


def test_coprime_numbers():
    assert MODULE.gcd(17, 5) == 1


def test_negative_inputs():
    assert MODULE.gcd(-24, 18) == 6
