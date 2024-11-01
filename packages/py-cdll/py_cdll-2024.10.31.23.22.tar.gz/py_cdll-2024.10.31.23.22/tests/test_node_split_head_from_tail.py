from src.py_cdll.node import Node, split_head_from_tail


def test_split_head_from_tail_one_node_success():
    # Setup
    node0: Node = Node(value=None)
    node0.next = node0
    node0.previous = node0

    # Execution
    head0, tail0 = split_head_from_tail(node=node0)

    # Validation
    assert head0 is node0
    assert head0.next is node0
    assert head0.previous is node0
    assert tail0 is None


def test_split_head_from_tail_two_nodes_success():
    # Setup
    node0: Node = Node(value=None)
    node1: Node = Node(value=None)
    node0.next = node1
    node1.previous = node0
    node1.next = node0
    node0.previous = node1

    # Execution
    head0, tail0 = split_head_from_tail(node=node0)

    # Validation
    assert head0 is node0
    assert head0.next is node0
    assert head0.previous is node0
    assert tail0 is node1
    assert tail0.next is node1
    assert tail0.previous is node1


def test_split_head_from_tail_three_nodes_success():
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

    # Execution
    head0, tail0 = split_head_from_tail(node=node0)

    # Validation
    assert head0 is node0
    assert head0.next is head0
    assert head0.previous is head0
    assert tail0 is node1
    assert tail0.next is node2
    assert tail0.previous is node2


def test_split_head_from_tail_four_nodes_success():
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

    # Execution
    head0, tail0 = split_head_from_tail(node=node0)

    # Validation
    assert head0 is node0
    assert head0.next is head0
    assert head0.previous is head0
    assert tail0 is node1
    assert tail0.next is node2
    assert tail0.previous is node3
