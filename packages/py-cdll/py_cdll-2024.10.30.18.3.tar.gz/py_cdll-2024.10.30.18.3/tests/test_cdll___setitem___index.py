import pytest

from src.py_cdll import CDLL


def test___setitem___index_in_range_success():
    # Setup
    data0: str = "data0"
    data1: str = "data1"
    cdll0: CDLL = CDLL(values=[data0])

    # Execution
    cdll0[0] = data1

    # Validation
    assert cdll0[0] == data1


def test___setitem___index_out_of_range_failure():
    # Setup
    data0: str = "data0"
    data1: str = "data1"
    cdll0: CDLL = CDLL(values=[data0])

    # Validation
    with pytest.raises(IndexError):
        cdll0[1] = data1


def test___setitem___index_empty_list_out_of_range_failure():
    # Setup
    data0: str = "data0"
    cdll0: CDLL = CDLL()

    # Validation
    with pytest.raises(IndexError):
        cdll0[0] = data0


def test___setitem___index_negative_success():
    # Setup
    data0: str = "data0"
    data1: str = "data1"
    data2: str = "data2"
    datas0: list[str] = [data0, data1]
    cdll0: CDLL = CDLL(values=datas0)

    # Execution
    cdll0[-1] = data2

    # Validation
    assert cdll0[-1] == data2
