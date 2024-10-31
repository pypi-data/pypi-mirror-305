class BaseCDLLException(Exception):
    """Base exception for Circular Doubly Linked List project."""


class CDLLAlreadyPopulatedError(BaseCDLLException):
    """Raise when attempting to populate CDLL, but there is already data in it."""


class NodeNotFoundError(BaseCDLLException):
    """Raise when search for Node returns nothing."""


class NegativeIndexError(BaseCDLLException):
    """Raise for indices that should be at least 0."""


class ValueNotFoundError(BaseCDLLException):
    """Raise for searches that return no result."""


class FirstValueNotFoundError(BaseCDLLException):
    """Raise when the first input of a method was not found where expected."""


class SecondValueNotFoundError(BaseCDLLException):
    """Raise when the second input of a method was not found where expected."""


class ValuesNotAdjacentError(BaseCDLLException):
    """Raise when values were not found adjacent to each other."""


class NoAdjacentValueError(BaseCDLLException):
    """Raise for searches for adjacent values in lists with single item."""


class MultipleValuesFoundError(BaseCDLLException):
    """Raise for searches that return no result."""


class UnableToPopulateWithNoValuesError(BaseCDLLException):
    """Raise when attempting to populate CDLL without any values."""


class EmptyCDLLError(BaseCDLLException):
    """Raise when an iterable is found to be empty."""


class UnevenListLengthError(BaseCDLLException):
    """Raise for lists that contain uneven amount of items."""


class InputNotIterableError(BaseCDLLException):
    """Raise when an input is not iterable."""


class NoBeforeAndAfterUniqueError(BaseCDLLException):
    """Raise when it is impossible to return the values before and after a unique element."""


class NoOrderedOccurrenceError(BaseCDLLException):
    """Raise when it is impossible to tell if data is ordered because values are missing."""


class AmbiguousEmptyCDLLStateError(BaseCDLLException):
    """Raise when it is ambiguous whether a CDLL is empty."""


class UnableToRemoveSingleNodeError(BaseCDLLException):
    """Raise when attempting to remove a node that is alone in its own sequence."""


class NotANodeError(BaseCDLLException):
    """Raise when a supposed Node turns out not to be so."""
