from string import digits
from typing import Optional, Callable, TypeVar, Generic
from collections.abc import Container

T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')


class Condition(Generic[T]):
    def __init__(self, cond: Callable[[str], bool], handle: Callable[[str], T], name: str = "", new_prompt: str = "",
                 is_error: bool = False) -> None:
        """
        A filter and handler for input strings.
        :param cond: A filter for which strings to handle.
        :param handle: Handles a filtered string.
        :param name: Name of the condition, if provided.
        :param new_prompt: The new prompt to switch to after handling, if provided.
        :param is_error: If ``True``, treat this condition as an error condition.
        """
        self.cond = cond
        """
        A filter for which strings to handle.
        """

        self.handle = handle
        """
        Handles a filtered string.
        """

        self.name = name
        """
        Name of the condition, if provided.
        """

        self.new_prompt = new_prompt
        """
        The new prompt to switch to after handling, if provided.
        """

        self.is_error = is_error
        """
        If ``True``, treat this condition as an error condition.
        """

    def __neg__(self):
        """
        Negate a condition.
        :return:
        """
        return Condition(lambda x: not self.cond(x), self.handle, self.name, self.new_prompt, self.is_error)

    def __and__(self, other: 'Condition[U]'):
        """
        Conjunction of two conditions. First condition is used for other args.
        :param other:
        :return:
        """
        return Condition(lambda x: self.cond(x) and other.cond(x), self.handle, self.name, self.new_prompt,
                         self.is_error)

    def __or__(self, other: 'Condition[U]'):
        """
        Disjunction of two conditions. First condition is used for other args.
        :param other:
        :return:
        """
        return Condition(lambda x: self.cond(x) or other.cond(x), self.handle, self.name, self.new_prompt,
                         self.is_error)


def is_pos_int(string: str) -> bool:
    """
    Returns ``True`` if a string can be converted to a positive ``int``.
    :param string:
    :return:
    """
    if not string:
        return False
    for char in string:
        if char not in digits:
            return False
    return True


def is_neg_int(string: str) -> bool:
    """
    Returns ``True`` if a string can be converted to a negative ``int``.
    :param string:
    :return:
    """
    if len(string) < 2:
        return False
    if string[0] != '-':
        return False
    return is_pos_int(string[1:])


def is_valid_int(string: str) -> bool:
    """
    Returns ``True`` if a string can be converted to an ``int``.
    :param string:
    :return:
    """
    return is_pos_int(string) or is_neg_int(string)


def is_valid_float(string: str) -> bool:
    """
    Returns ``True`` if a string can be converted to a ``float``.
    :param string:
    :return:
    """
    if is_valid_int(string):
        return True
    if len(string.split('.')) == 2:
        x, y = string.split('.')
        return is_valid_int(x) and (is_pos_int(y) or not y)
    return False


def int_condition(handle: Callable[[int], T] = lambda x: x, name: str = "", new_prompt: str = "",
                  is_error: bool = False) -> Condition[T]:
    """
    Condition for handling ``int`` values.
    :param handle: Handle the provided integer, or do nothing if not provided.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If true, treat this condition as an error condition.
    :return:
    """
    return Condition(is_valid_int, lambda x: handle(int(x)), name, new_prompt, is_error)


def float_condition(handle: Callable[[float], T] = lambda x: x, name: str = "", new_prompt: str = "",
                    is_error: bool = False) -> Condition[T]:
    """
    Condition for handling ``float`` values.
    :param handle: Handle the provided float, or do nothing if not provided.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If true, treat this condition as an error condition.
    :return:
    """
    return Condition(is_valid_float, lambda x: handle(float(x)), name, new_prompt, is_error)


def gt_condition(y: T, handle: Callable[[V], U] = lambda x: x,
                 cond: Callable[[str], bool] = is_valid_int, conv: Callable[[str], V] = int,
                 name: str = "", new_prompt: str = "", is_error: bool = False) -> Condition[U]:
    """
    Condition for handling an input is greater than ``y``.
    :param y: The second argument for comparison.
    :param handle: Handle the provided object, or do nothing if not provided.
    :param cond: Condition for converting the input to the required type.
    :param conv: Convert the input to the required type.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If ``True``, treat this condition as an error condition.
    :return:
    """
    return Condition(lambda x: cond(x) and conv(x) > y, lambda x: handle(conv(x)), name, new_prompt, is_error)


def ge_condition(y: T, handle: Callable[[V], U] = lambda x: x,
                 cond: Callable[[str], bool] = is_valid_int, conv: Callable[[str], V] = int,
                 name: str = "", new_prompt: str = "", is_error: bool = False) -> Condition[U]:
    """
    Condition for handling an input is greater than or equal to ``y``.
    :param y: The second argument for comparison.
    :param handle: Handle the provided object, or do nothing if not provided.
    :param cond: Condition for converting the input to the required type.
    :param conv: Convert the input to the required type.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If ``True``, treat this condition as an error condition.
    :return:
    """
    return Condition(lambda x: cond(x) and conv(x) >= y, lambda x: handle(conv(x)), name, new_prompt, is_error)


def lt_condition(y: T, handle: Callable[[V], U] = lambda x: x,
                 cond: Callable[[str], bool] = is_valid_int, conv: Callable[[str], V] = int,
                 name: str = "", new_prompt: str = "", is_error: bool = False) -> Condition[U]:
    """
    Condition for handling an input is less than ``y``.
    :param y: The second argument for comparison.
    :param handle: Handle the provided object, or do nothing if not provided.
    :param cond: Condition for converting the input to the required type.
    :param conv: Convert the input to the required type.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If ``True``, treat this condition as an error condition.
    :return:
    """
    return Condition(lambda x: cond(x) and conv(x) < y, lambda x: handle(conv(x)), name, new_prompt, is_error)


def le_condition(y: T, handle: Callable[[V], U] = lambda x: x,
                 cond: Callable[[str], bool] = is_valid_int, conv: Callable[[str], V] = int,
                 name: str = "", new_prompt: str = "", is_error: bool = False) -> Condition[U]:
    """
    Condition for handling an input is less than or equal to ``y``.
    :param y: The second argument for comparison.
    :param handle: Handle the provided object, or do nothing if not provided.
    :param cond: Condition for converting the input to the required type.
    :param conv: Convert the input to the required type.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If ``True``, treat this condition as an error condition.
    :return:
    """
    return Condition(lambda x: cond(x) and conv(x) <= y, lambda x: handle(conv(x)), name, new_prompt, is_error)

def eq_condition(y: T, handle: Callable[[V], U] = lambda x: x,
                 cond: Callable[[str], bool] = lambda x: True, conv: Callable[[str], V] = lambda x: x,
                 name: str = "", new_prompt: str = "", is_error: bool = False) -> Condition[U]:
    """
    Condition for handling an input equal to ``y``.
    :param y: The second argument for comparison.
    :param handle: Handle the provided object, or do nothing if not provided.
    :param cond: Condition for converting the input to the required type.
    :param conv: Convert the input to the required type.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If ``True``, treat this condition as an error condition.
    :return:
    """
    return Condition(lambda x: cond(x) and conv(x) == y, lambda x: handle(conv(x)), name, new_prompt, is_error)


def contains_condition(values: Container[T], handle: Callable[[T], V] = lambda x: x,
                       cond: Callable[[str], bool] = lambda x: True, conv: Callable[[str], T] = lambda x: x, name: str = "",
                       new_prompt: str = "", is_error: bool = False) -> Condition[V]:
    """
    Condition for handling an input inside a container.
    :param values: The valid container of values.
    :param handle: Handle the provided object, or do nothing if not provided.
    :param cond: Condition for converting the input to the required type.
    :param conv: Convert the input to the required type.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If ``True``, treat this condition as an error condition.
    :return:
    """
    return Condition(lambda x: cond(x) and conv(x) in values, lambda x: handle(conv(x)), name, new_prompt, is_error)

def range_condition(values: range, handle: Callable[[int], T] = lambda x: x, name: str = "",
                    new_prompt: str = "", is_error: bool = False) -> Condition[V]:
    """
    Condition for handling an input inside a range.
    :param values: The valid range of values.
    :param handle: Handle the provided object, or do nothing if not provided.
    :param cond: Condition for converting the input to the required type.
    :param conv: Convert the input to the required type.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If ``True``, treat this condition as an error condition.
    :return:
    """
    return contains_condition(values, handle, is_valid_int, int, name, new_prompt, is_error)


def nonempty_condition(value: Optional[T] = None, name: str = "", new_prompt: str = "",
                       is_error: bool = False) -> Condition[Optional[T]]:
    """
    Condition for handling nonempty strings.
    :param value: The value to return for handling, or do nothing if not provided.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If ``True``, treat this condition as an error condition.
    :return:
    """
    return Condition(lambda x: x, lambda x: x if value is None else None, name, new_prompt, is_error)


def null_condition(value: Optional[T] = None, name: str = "", new_prompt: str = "",
                   is_error: bool = False) -> Condition[Optional[T]]:
    """
    Condition for handling any string.
    :param value: The value to return for handling, or do nothing if not provided.
    :param name: Name of the condition, if provided.
    :param new_prompt: The new prompt to switch to after handling, if provided.
    :param is_error: If ``True``, treat this condition as an error condition.
    :return:
    """
    return Condition(lambda x: True, lambda x: x if value is None else None, name, new_prompt, is_error)
