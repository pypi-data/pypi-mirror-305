from typing import TypeVar, Iterator, Sequence

from src.py_cdll.exceptions import UnableToRemoveSingleNodeError, NotANodeError

_T = TypeVar("_T")


class Node:
    """Circular Doubly Linked Node"""

    def __init__(self, value) -> None:
        self.value = value
        self.next: Node = self
        self.previous: Node = self

    def __repr__(self) -> str:
        node_values: list = []

        current_node: Node = self
        while True:
            node_values.append(current_node.value)
            current_node = current_node.next
            if not isinstance(current_node, Node) or current_node is self:
                break

        # string = str(node_values)
        string = f"Node{node_values}"
        return string


def nodes_values(values: Sequence[_T]) -> Node | None:
    """Create circular doubly linked list of Nodes containing values."""
    values_iterator: Iterator[_T] = iter(values)

    try:
        head: Node | None = Node(value=next(values_iterator))
        current: Node | None = head
    except StopIteration:
        head, current = None, None

    for value in values_iterator:
        node: Node = Node(value=value)
        insert_between(before=current, after=head, insert=node)
        current = current.next

    return head


def length(node: Node) -> int:
    """Count nodes in circular doubly linked sequence."""
    try:
        node.next.previous.value
    except AttributeError as exception:
        raise NotANodeError(f"'{node}' is not a Node, but a '{type(node)}'.") from exception

    sequence_length: int = 0
    current: Node = node

    while True:
        sequence_length += 1
        current = current.next

        if current is node:
            break

    return sequence_length


def remove(target: Node) -> None:
    insert_between(before=target.previous, after=target.next, insert=None)


def equal(first: Node, second: Node) -> bool:
    """Compare nodes from head in two circular doubly linked sequences."""
    equality: bool = True

    first_head: Node = first
    second_head: Node = second

    first_current: Node = first_head
    second_current: Node = second_head

    while True:
        equality &= first_current.value is second_current.value or first_current.value == second_current.value

        if first_current.next is first_head and second_current.next is second_head:
            break
        elif first_current.next is first_head and second_current.next is not second_head:
            equality &= False
            break
        elif first_current.next is not first_head and second_current.next is second_head:
            equality &= False
            break

        first_current = first_current.next
        second_current = second_current.next

    return equality


def reverse_order(head: Node) -> Node:
    if head.next is head:
        reversed_sequence: Node = head
    else:
        reversed_sequence: Node = head.previous
        previous_node: Node = head
        current_node: Node = head.previous

        while True:
            old_previous: Node = current_node.previous

            current_node.next = current_node.previous
            current_node.previous = previous_node

            previous_node = current_node
            current_node = old_previous

            if previous_node is head:
                break

    return reversed_sequence


def split_head_from_tail(node: Node) -> tuple[Node, Node | None]:
    first_head: Node = node

    if node.next is node:
        second_head: None = None
    else:
        second_last: Node = node.previous
        second_head: Node = node.next
        second_head.previous = second_last
        second_last.next = second_head

        first_head.next = first_head
        first_head.previous = first_head

    return first_head, second_head


def middle_adjacent(head: Node) -> tuple[Node, Node]:
    """When node amount is uneven, preferentially adds one more node to before than after."""
    slow: Node = head
    fast: Node = head

    while fast.next is not head and fast.next.next is not head:
        slow = slow.next
        fast = fast.next.next

    before_last: Node = slow
    after_head: Node = slow.next

    return before_last, after_head


def stitch(head: Node, last: Node) -> None:
    """Stitch together head and last to make open list circular."""
    head.previous = last
    last.next = head


def insert_between(before: Node, after: Node, insert: Node | None) -> None:
    """
    Allows that insert can have multiple connected nodes.
    Assumes that each input Node is in a fully circular doubly linked list.
    """
    try:
        if insert is None and length(node=before) == 1:
            raise UnableToRemoveSingleNodeError(f"Unable to remove node '{before}' "
                                                f"because it is the only one in sequence.")
        elif insert is None:
            insert_head: Node = after
            insert_last: Node = before
        else:
            insert_head: Node = insert
            insert_last: Node = insert.previous
            insert_head.previous = before
            insert_last.next = after
    except AttributeError as exception:
        raise NotANodeError(f"'{insert}' is not a Node, but a '{type(insert)}'.") from exception

    before.next = insert_head
    after.previous = insert_last


def before_target(current: Node, head: Node, target: Node) -> Node:
    """
    Assuming pre-sorted sub-lists.
    Assuming first head value is lower than or equal to insert head value.
    """
    while current.next.value <= target.value and current.next is not head:
        current = current.next

    return current


def split_in_middle(head: Node) -> tuple[Node, Node]:
    before_head: Node = head
    after_last: Node = head.previous

    before_last, after_head = middle_adjacent(head=head)

    stitch(head=before_head, last=before_last)
    stitch(head=after_head, last=after_last)

    return before_head, after_head


def merge(first: Node, second: Node) -> Node:
    """
    Merge pre-sorted circular doubly linked nodes.
    Moving nodes from second into sorted positions in first.
    Assuming pre-sorted sub-lists.
    """

    if first.value > second.value:
        first, second = second, first

    before_insert: Node = first

    while second is not None:
        insert, second = split_head_from_tail(node=second)
        before_insert = before_target(current=before_insert, head=first, target=insert)
        insert_between(before=before_insert, after=before_insert.next, insert=insert)

    return first


def merge_sort(head: Node) -> Node:
    """Merge-sort implementation for circular doubly linked nodes."""

    if head.next is head:
        # When there is only one value, there is nothing to sort.
        merged_sorted: Node = head
    else:
        first, second = split_in_middle(head=head)
        first_sorted, second_sorted = merge_sort(head=first), merge_sort(head=second)
        merged_sorted: Node = merge(first=first_sorted, second=second_sorted)

    return merged_sorted
