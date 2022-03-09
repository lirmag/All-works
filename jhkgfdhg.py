from functools import lru_cache


def moves(h):
    return h + 1, (h * 3) - 2


@lru_cache(None)
def f(h):
    if h > 39:
        return 'END'
    elif any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    elif all(f(x) == 'P1' for x in moves(h)):
        return 'B1'
    elif any(f(x) == 'B1' for x in moves(h)):
        return 'P2'
    elif all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'B2'


for i in range(2, 100):
    print(i, f(i))
