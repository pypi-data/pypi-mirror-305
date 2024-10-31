import pytest

from src.py_cdll import NotANodeError
from src.py_cdll.node import Node, length


def test_length_not_node_failure():
    # Setup
    node0: float = 3.14

    # Validation
    with pytest.raises(NotANodeError):
        # noinspection PyTypeChecker
        length(node=node0)


def test_length_one_node_success():
    # Setup
    node0: Node = Node(value=None)
    node0.next = node0
    node0.previous = node0
    length0: int = 1

    # Execution
    length1: int = length(node=node0)

    # Validation
    assert length0 == length1


def test_length_two_nodes_success():
    # Setup
    node0: Node = Node(value=None)
    node1: Node = Node(value=None)
    node0.next = node1
    node1.previous = node0
    node1.next = node0
    node0.previous = node1
    length0: int = 2

    # Execution
    length1: int = length(node=node0)

    # Validation
    assert length0 == length1


def test_length_three_nodes_success():
    # Setup
    node0: Node = Node(value=None)
    node1: Node = Node(value=None)
    node2: Node = Node(value=None)
    node0.next = node1
    node1.previous = node0
    node1.next = node2
    node2.previous = node1
    node2.next = node0
    node0.previous = node2
    length0: int = 3

    # Execution
    length1: int = length(node=node0)

    # Validation
    assert length0 == length1


def test_length_four_nodes_success():
    # Setup
    node0: Node = Node(value=None)
    node1: Node = Node(value=None)
    node2: Node = Node(value=None)
    node3: Node = Node(value=None)
    node0.next = node1
    node1.previous = node0
    node1.next = node2
    node2.previous = node1
    node2.next = node3
    node3.previous = node2
    node3.next = node0
    node0.previous = node3
    length0: int = 4

    # Execution
    length1: int = length(node=node0)

    # Validation
    assert length0 == length1
