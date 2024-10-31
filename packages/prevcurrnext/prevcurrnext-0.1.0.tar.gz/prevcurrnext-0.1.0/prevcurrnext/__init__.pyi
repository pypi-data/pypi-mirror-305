from typing import Any, Iterable, Literal, overload

@overload
def currprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True] = True,
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def currprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True] = True,
    end_curr_on_none: Literal[False] = False,
) -> Iterable[tuple[T, T | None]]: ...
@overload
def currprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def currprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    end_curr_on_none: Literal[False] = False,
) -> Iterable[tuple[T, T]]: ...
@overload
def currprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: bool = True,
    end_curr_on_none: bool = False,
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def prevcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True] = True,
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def prevcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    end_curr_on_none: Literal[True],
) -> Iterable[tuple[T, T | None]]: ...
@overload
def prevcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True] = True,
    end_curr_on_none: Literal[False] = False,
) -> Iterable[tuple[T | None, T]]: ...
@overload
def prevcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    end_curr_on_none: Literal[False] = False,
) -> Iterable[tuple[T, T]]: ...
@overload
def currnext[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def currnext[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False] = False,
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T, T]]: ...
@overload
def currnext[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False] = False,
    end_next_on_none: bool = True,
) -> Iterable[tuple[T, T | None]]: ...
@overload
def currnext[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
    end_next_on_none: bool = True,
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def nextcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False] = False,
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T, T]]: ...
@overload
def nextcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[False] = False,
    end_next_on_none: Literal[True] = True,
) -> Iterable[tuple[T, T | None]]: ...
@overload
def nextcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T | None, T]]: ...
@overload
def nextcurr[T = Any](
    iterable: Iterable[T],
    *,
    start_curr_on_none: Literal[True],
    end_next_on_none: Literal[True] = True,
) -> Iterable[tuple[T | None, T | None]]: ...
@overload
def prevcurrnext[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    start_curr_on_none: Literal[False] = False,
    end_curr_on_none: bool = False,
    end_next_on_none: Literal[True] = True,
) -> Iterable[tuple[T, T | None, T | None]]: ...
@overload
def prevcurrnext[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    start_curr_on_none: Literal[False] = False,
    end_curr_on_none: Literal[False] = False,
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T, T, T]]: ...
@overload
def prevcurrnext[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True] = True,
    start_curr_on_none: bool = False,
    end_curr_on_none: bool = False,
    end_next_on_none: Literal[True] = True,
) -> Iterable[tuple[T | None, T | None, T | None]]: ...
@overload
def prevcurrnext[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True] = True,
    start_curr_on_none: bool = False,
    end_curr_on_none: Literal[False] = False,
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T | None, T | None, T]]: ...
@overload
def nextcurrprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    start_curr_on_none: Literal[False] = False,
    end_curr_on_none: bool = False,
    end_next_on_none: Literal[True] = True,
) -> Iterable[tuple[T | None, T | None, T]]: ...
@overload
def nextcurrprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[False],
    start_curr_on_none: Literal[False] = False,
    end_curr_on_none: Literal[False] = False,
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T, T, T]]: ...
@overload
def nextcurrprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True] = True,
    start_curr_on_none: bool = False,
    end_curr_on_none: bool = False,
    end_next_on_none: Literal[True] = True,
) -> Iterable[tuple[T | None, T | None, T | None]]: ...
@overload
def nextcurrprev[T = Any](
    iterable: Iterable[T],
    *,
    start_prev_on_none: Literal[True] = True,
    start_curr_on_none: bool = False,
    end_curr_on_none: Literal[False] = False,
    end_next_on_none: Literal[False],
) -> Iterable[tuple[T, T | None, T | None]]: ...
