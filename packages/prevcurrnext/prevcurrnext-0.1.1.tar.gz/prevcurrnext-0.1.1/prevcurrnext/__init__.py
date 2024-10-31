from typing import Any, Iterable


def currprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: bool = True,
    end_curr_on_none: bool = False,
) -> Iterable[tuple[T | None, T | None]]:
    """
    Iterate over the iterable, yielding pairs of (current item, previous item).

    Parameters:
        iterable: An iterable to traverse.
        start_prev_on_none (optional): If True (default), yield the first pair with prev as None.
        end_curr_on_none (optional): If True, after the last item, yield a pair (None, prev).

    Example:
        >>> for curr, prev in currprev([1, 2, 3]):
        ...     print(f"{curr}, {prev}")
        1, None
        2, 1
        3, 2

        >>> for curr, prev in currprev([1, 2, 3], start_prev_on_none=False):
        ...     print(f"{curr}, {prev}")
        2, 1
        3, 2

        >>> for curr, prev in currprev([1, 2, 3], end_curr_on_none=True):
        ...     print(f"{curr}, {prev}")
        1, None
        2, 1
        3, 2
        None, 3
    """
    prev: T | None = None
    for curr in iter(iterable):
        if prev is not None or start_prev_on_none:
            yield curr, prev
        prev = curr
    if end_curr_on_none and prev is not None:
        yield None, prev


def prevcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: bool = True,
    end_curr_on_none: bool = False,
) -> Iterable[tuple[T | None, T | None]]:
    """
    Iterate over the iterable, yielding pairs of (previous item, current item).

    Parameters:
        iterable: An iterable to traverse.
        start_prev_on_none (optional): If True (default), yield the first pair with prev as None.
        end_curr_on_none (optional): If True, after the last item, yield a pair (prev, None).

    Example:
        >>> for prev, curr in prevcurr([1, 2, 3]):
        ...     print(f"{prev}, {curr}")
        None, 1
        1, 2
        2, 3

        >>> for prev, curr in prevcurr([1, 2, 3], start_prev_on_none=False):
        ...     print(f"{prev}, {curr}")
        1, 2
        2, 3

        >>> for prev, curr in prevcurr([1, 2, 3], end_curr_on_none=True):
        ...     print(f"{prev}, {curr}")
        None, 1
        1, 2
        2, 3
        3, None
    """
    for curr, prev in currprev(
        iterable,
        start_prev_on_none=start_prev_on_none,
        end_curr_on_none=end_curr_on_none,
    ):
        yield prev, curr


def currnext[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: bool = False,
    end_next_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None]]:
    """
    Iterate over the iterable, yielding pairs of (current item, next item).

    Parameters:
        iterable: An iterable to traverse.
        start_curr_on_none (optional): If True, start with curr as None. Default is False.
        end_next_on_none (optional): If True (default), after the last item, yield a pair (curr, None).

    Example:
        >>> for curr, next in currnext([1, 2, 3]):
        ...     print(f"{curr}, {next}")
        1, 2
        2, 3
        3, None

        >>> for curr, next in currnext([1, 2, 3], end_next_on_none=False):
        ...     print(f"{curr}, {next}")
        1, 2
        2, 3

        >>> for curr, next in currnext([1, 2, 3], start_curr_on_none=True):
        ...     print(f"{curr}, {next}")
        None, 1
        1, 2
        2, 3
        3, None
    """
    iterator = iter(iterable)
    try:
        if not start_curr_on_none:
            curr = next(iterator)
        else:
            curr = None
    except StopIteration:
        return
    for _next in iterator:
        yield curr, _next
        curr = _next
    if end_next_on_none and curr is not None:
        yield curr, None


def nextcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: bool = False,
    end_next_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None]]:
    """
    Iterate over the iterable, yielding pairs of (next item, current item).

    Parameters:
        iterable: An iterable to traverse.
        start_curr_on_none (optional): If True, start with curr as None. Default is False.
        end_next_on_none (optional): If True (default), after the last item, yield a pair (None, curr).

    Example:
        >>> for next, curr in nextcurr([1, 2, 3]):
        ...     print(f"{next}, {curr}")
        2, 1
        3, 2
        None, 3

        >>> for next, curr in nextcurr([1, 2, 3], end_next_on_none=False):
        ...     print(f"{next}, {curr}")
        2, 1
        3, 2

        >>> for next, curr in nextcurr([1, 2, 3], start_curr_on_none=True):
        ...     print(f"{next}, {curr}")
        1, None
        2, 1
        3, 2
        None, 3
    """
    for curr, _next in currnext(
        iterable,
        start_curr_on_none=start_curr_on_none,
        end_next_on_none=end_next_on_none,
    ):
        yield _next, curr


def prevcurrnext[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: bool = True,
    start_curr_on_none: bool = False,
    end_curr_on_none: bool = False,
    end_next_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None, T | None]]:
    """
    Iterate over the iterable, yielding triples of (previous item, current item, next item).

    Parameters:
        iterable: An iterable to traverse.
        start_prev_on_none (optional): If True (default), the first prev is None.
        start_curr_on_none (optional): If True, the first curr is None. Requires start_prev_on_none=True.
        end_curr_on_none (optional): If True, after the last item, yield pairs ending with curr as None.
                                     Requires end_next_on_none=True.
        end_next_on_none (optional): If True (default), after the last item, next is None.

    Raises:
        ValueError: If start_curr_on_none is True but start_prev_on_none is False.
        ValueError: If end_next_on_none is False but end_curr_on_none is True.

    Example:
        >>> for prev, curr, next in prevcurrnext([1, 2, 3]):
        ...     print(f"{prev}, {curr}, {next}")
        None, 1, 2
        1, 2, 3
        2, 3, None

        >>> for prev, curr, next in prevcurrnext([1, 2, 3], start_prev_on_none=False):
        ...     print(f"{prev}, {curr}, {next}")
        1, 2, 3
        2, 3, None

        >>> for prev, curr, next in prevcurrnext([1, 2, 3], end_curr_on_none=True):
        ...     print(f"{prev}, {curr}, {next}")
        None, 1, 2
        1, 2, 3
        2, 3, None
        3, None, None

        >>> for prev, curr, next in prevcurrnext([1, 2, 3], start_curr_on_none=True):
        ...     print(f"{prev}, {curr}, {next}")
        None, None, 1
        None, 1, 2
        1, 2, 3
        2, 3, None
    """
    prev = None
    curr = None
    iterator = iter(iterable)
    if not start_prev_on_none:
        if start_curr_on_none:
            raise ValueError("start_curr_on_none=True requires start_prev_on_none=True")
        try:
            prev = next(iterator)
        except StopIteration:
            return
        try:
            curr = next(iterator)
        except StopIteration:
            yield prev, None, None
            return
    elif not start_curr_on_none:
        try:
            curr = next(iterator)
        except StopIteration:
            return
    for _next in iterator:
        yield prev, curr, _next
        prev = curr
        curr = _next
    if end_curr_on_none:
        if not end_next_on_none:
            raise ValueError("end_next_on_none=True requires end_curr_on_none=True")
        yield prev, curr, None
        yield curr, None, None
    elif end_next_on_none:
        yield prev, curr, None


def nextcurrprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: bool = True,
    start_curr_on_none: bool = False,
    end_curr_on_none: bool = False,
    end_next_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None, T | None]]:
    """
    Iterate over the iterable, yielding triples of (next item, current item, previous item).

    Parameters:
        iterable: An iterable to traverse.
        start_prev_on_none (optional): If True (default), the first prev is None.
        start_curr_on_none (optional): If True, the first curr is None. Requires start_prev_on_none=True.
        end_curr_on_none (optional): If True, after the last item, yield pairs ending with curr as None.
                                     Requires end_next_on_none=True.
        end_next_on_none (optional): If True (default), after the last item, next is None.

    Raises:
        ValueError: If start_curr_on_none is True but start_prev_on_none is False.
        ValueError: If end_next_on_none is False but end_curr_on_none is True.

    Example:
        >>> for next, curr, prev in nextcurrprev([1, 2, 3]):
        ...     print(f"{next}, {curr}, {prev}")
        2, 1, None
        3, 2, 1
        None, 3, 2

        >>> for next, curr, prev in nextcurrprev([1, 2, 3], start_prev_on_none=False):
        ...     print(f"{next}, {curr}, {prev}")
        3, 2, 1
        None, 3, 2

        >>> for next, curr, prev in nextcurrprev([1, 2, 3], end_curr_on_none=True):
        ...     print(f"{next}, {curr}, {prev}")
        2, 1, None
        3, 2, 1
        None, 3, 2
        None, None, 3

        >>> for next, curr, prev in nextcurrprev([1, 2, 3], start_curr_on_none=True):
        ...     print(f"{next}, {curr}, {prev}")
        1, None, None
        2, 1, None
        3, 2, 1
        None, 3, 2
    """
    for prev, curr, _next in prevcurrnext(
        iterable,
        start_prev_on_none=start_prev_on_none,
        start_curr_on_none=start_curr_on_none,
        end_curr_on_none=end_curr_on_none,
        end_next_on_none=end_next_on_none,
    ):
        yield _next, curr, prev
