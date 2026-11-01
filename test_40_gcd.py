import importlib

module = importlib.import_module("40_gcd")


def test_gcd_of_two_numbers():
    assert module.gcd(48, 18) == 6


def test_gcd_with_zero():
    assert module.gcd(10, 0) == 10


def test_gcd_with_negative_number():
    assert module.gcd(-24, 18) == 6


def test_gcd_of_coprime_numbers():
    assert module.gcd(17, 5) == 1
