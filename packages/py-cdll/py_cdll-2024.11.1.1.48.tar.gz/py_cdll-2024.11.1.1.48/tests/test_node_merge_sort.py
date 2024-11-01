import pytest

from src.py_cdll import CDLL
from src.py_cdll.node import merge_sort


def test_merge_sort_integers_success():
    # Setup
    l0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    c0 = CDLL(l0)
    l1 = [0, 9, 2, 7, 4, 5, 6, 3, 8, 1]
    c1 = CDLL(l1)

    # Execution
    l2 = merge_sort(head=c1._head)
    c2 = CDLL()
    c2._head = l2
    c2._length = 10

    # Validation
    assert c0 == c2


def test_merge_sort_strings_success():
    # Setup
    l0 = ["a", "d", "f", "j", "m", "p", "q", "t", "v", "y"]
    c0 = CDLL(l0)
    l1 = ['t', 'v', 'y', 'j', 'm', 'a', 'p', 'q', 'd', 'f']
    c1 = CDLL(l1)

    # Execution
    l2 = merge_sort(head=c1._head)
    c2 = CDLL()
    c2._head = l2
    c2._length = 10

    # Validation
    assert c0 == c2


def test_merge_sort_functions_failure():
    # Setup
    l0 = [min, max, all]
    c0 = CDLL(l0)

    # Validation
    with pytest.raises(TypeError):
        merge_sort(head=c0._head)
