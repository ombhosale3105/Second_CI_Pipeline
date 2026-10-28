from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("39_transpose_matrix.py")
SPEC = spec_from_file_location("transpose_matrix_program", MODULE_PATH)
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_square_matrix():
    assert MODULE.transpose_matrix([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_rectangular_matrix():
    assert MODULE.transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_empty_matrix():
    assert MODULE.transpose_matrix([]) == []
