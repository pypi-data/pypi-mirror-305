import pytest

from src.py_cdll.exceptions import UnableToRemoveSingleNodeError
from src.py_cdll.node import Node, stitch, remove


def test_remove_single_node_sequence_failure():
    # Setup
    node0: Node = Node(value=None)
    stitch(head=node0, last=node0)

    # Validation
    with pytest.raises(UnableToRemoveSingleNodeError):
        remove(target=node0)


def test_remove_first_in_two_node_sequence_success():
    # Setup
    node0: Node = Node(value=None)
    node1: Node = Node(value=None)
    stitch(head=node0, last=node1)
    stitch(head=node1, last=node0)

    # Verification
    assert node1.next is node0
    assert node1.previous is node0

    # Execution
    remove(target=node0)

    # Validation
    assert node1.next is node1
    assert node1.previous is node1


def test_remove_last_in_three_node_sequence_success():
    # Setup
    node0: Node = Node(value=None)
    node1: Node = Node(value=None)
    node2: Node = Node(value=None)
    stitch(head=node0, last=node2)
    stitch(head=node1, last=node0)
    stitch(head=node2, last=node1)

    # Verification
    assert node0.next is node1
    assert node0.previous is node2
    assert node1.next is node2
    assert node1.previous is node0

    # Execution
    remove(target=node2)

    # Validation
    assert node0.next is node1
    assert node0.previous is node1
    assert node1.next is node0
    assert node1.previous is node0


def test_remove_middle_in_five_node_sequence_success():
    # Setup
    node0: Node = Node(value=None)
    node1: Node = Node(value=None)
    node2: Node = Node(value=None)
    node3: Node = Node(value=None)
    node4: Node = Node(value=None)
    stitch(head=node0, last=node4)
    stitch(head=node1, last=node0)
    stitch(head=node2, last=node1)
    stitch(head=node3, last=node2)
    stitch(head=node4, last=node3)

    # Verification
    assert node0.next is node1
    assert node0.previous is node4
    assert node1.next is node2
    assert node1.previous is node0
    assert node2.next is node3
    assert node2.previous is node1
    assert node3.next is node4
    assert node3.previous is node2
    assert node4.next is node0
    assert node4.previous is node3

    # Execution
    remove(target=node2)

    # Validation
    assert node0.next is node1
    assert node0.previous is node4
    assert node1.next is node3
    assert node1.previous is node0
    assert node3.next is node4
    assert node3.previous is node1
    assert node4.next is node0
    assert node4.previous is node3
