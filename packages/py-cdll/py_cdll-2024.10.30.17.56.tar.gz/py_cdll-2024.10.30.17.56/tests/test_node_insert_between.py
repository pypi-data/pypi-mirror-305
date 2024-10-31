from src.py_cdll import CDLL
from src.py_cdll.node import Node, insert_between


def test_insert_between_first_zero_second_one_success():
    # Setup
    l0: list[int] = [0]
    l1: list[int] = [1]
    l2: list[int] = [0, 1]
    before0: Node = CDLL(values=l0)._head
    after0: Node = before0.next
    insert0: Node = CDLL(values=l1)._head
    c0: CDLL = CDLL(values=l2)

    # Execution
    insert_between(before=before0, after=after0, insert=insert0)
    c1 = CDLL()
    c1._head = before0
    c1._length = 2

    # Validation
    assert c0 == c1


def test_insert_between_first_zero_two_second_one_success():
    # Setup
    l0: list[int] = [0, 2]
    l1: list[int] = [1]
    l2: list[int] = [0, 1, 2]
    before0: Node = CDLL(values=l0)._head
    after0: Node = before0.next
    insert0: Node = CDLL(values=l1)._head
    c0: CDLL = CDLL(values=l2)

    # Execution
    insert_between(before=before0, after=after0, insert=insert0)
    c1 = CDLL()
    c1._head = before0
    c1._length = 3

    # Validation
    assert c0 == c1


def test_insert_between_first_five_twelve_second_two_success():
    # Setup
    l0: list[int] = [5, 12]
    l1: list[int] = [2]
    l2: list[int] = [2, 5, 12]
    before0: Node = CDLL(values=l0)._head.previous
    after0: Node = before0.next
    insert0: Node = CDLL(values=l1)._head
    c0: CDLL = CDLL(values=l2)

    # Execution
    insert_between(before=before0, after=after0, insert=insert0)
    c1 = CDLL()
    c1._head = before0.next
    c1._length = 3

    # Validation
    assert c0 == c1


def test_insert_between_first_five_twelve_second_two_four_success():
    # Setup
    l0: list[int] = [5, 12]
    l1: list[int] = [2, 4]
    l2: list[int] = [2, 4, 5, 12]
    before0: Node = CDLL(values=l0)._head.previous
    after0: Node = before0.next
    insert0: Node = CDLL(values=l1)._head
    c0: CDLL = CDLL(values=l2)

    # Execution
    insert_between(before=before0, after=after0, insert=insert0)
    c1 = CDLL()
    c1._head = before0.next
    c1._length = 4

    # Validation
    assert c0 == c1


def test_insert_between_first_five_twelve_sixteen_twenty_second_none_success():
    # Setup
    l0: list[int] = [5, 12, 16, 20]
    l1: None = None
    l2: list[int] = [5, 20]
    before0: Node = CDLL(values=l0)._head
    after0: Node = before0.previous
    insert0: None = l1
    c0: CDLL = CDLL(values=l2)

    # Execution
    insert_between(before=before0, after=after0, insert=insert0)
    c1 = CDLL()
    c1._head = before0
    c1._length = 2

    # Validation
    assert c0 == c1


