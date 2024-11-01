from src.py_cdll.node import Node, equal


def test_equal_one_value_same_success():
    # Setup
    value0: str = "value0"
    first0: Node = Node(value=value0)
    second0: Node = Node(value=value0)
    first0.next = first0
    first0.previous = first0
    second0.next = second0
    second0.previous = second0
    boolean0: bool = True

    # Execution
    boolean1: bool = equal(first=first0, second=second0)

    # Validation
    assert boolean0 is boolean1


def test_equal_one_value_different_values_success():
    # Setup
    value0: str = "value0"
    value1: str = "value1"
    first0: Node = Node(value=value0)
    second0: Node = Node(value=value1)
    first0.next = first0
    first0.previous = first0
    second0.next = second0
    second0.previous = second0
    boolean0: bool = False

    # Execution
    boolean1: bool = equal(first=first0, second=second0)

    # Validation
    assert boolean0 is boolean1


def test_equal_two_values_different_lengths_success():
    # Setup
    value0: str = "value0"
    value1: str = "value1"
    first0: Node = Node(value=value0)
    second0: Node = Node(value=value0)
    second1: Node = Node(value=value1)
    first0.next = first0
    first0.previous = first0
    second0.next = second1
    second1.previous = second0
    second1.next = second0
    second0.previous = second1
    boolean0: bool = False

    # Execution
    boolean1: bool = equal(first=first0, second=second0)

    # Validation
    assert boolean0 is boolean1


def test_equal_two_values_same_success():
    # Setup
    value0: str = "value0"
    value1: str = "value1"
    first0: Node = Node(value=value0)
    first1: Node = Node(value=value1)
    second0: Node = Node(value=value0)
    second1: Node = Node(value=value1)
    first0.next = first1
    first1.previous = first0
    first1.next = first0
    first0.previous = first1
    second0.next = second1
    second1.previous = second0
    second1.next = second0
    second0.previous = second1
    boolean0: bool = True

    # Execution
    boolean1: bool = equal(first=first0, second=second0)

    # Validation
    assert boolean0 is boolean1


def test_equal_two_values_different_values_success():
    # Setup
    value0: str = "value0"
    value1: str = "value1"
    value2: str = "value2"
    first0: Node = Node(value=value0)
    first1: Node = Node(value=value1)
    second0: Node = Node(value=value0)
    second1: Node = Node(value=value2)
    first0.next = first1
    first1.previous = first0
    first1.next = first0
    first0.previous = first1
    second0.next = second1
    second1.previous = second0
    second1.next = second0
    second0.previous = second1
    boolean0: bool = False

    # Execution
    boolean1: bool = equal(first=first0, second=second0)

    # Validation
    assert boolean0 is boolean1
