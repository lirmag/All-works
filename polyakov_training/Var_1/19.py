from functools import lru_cache


def moves(h):
    if (h % 2 == 0) and (h % 3 == 0):
        return h // 2, h - (h * (2/3))
    if (h % 2 != 0) and (h % 3 == 0):
        return h - 2, h - (h * (2/3))
    if (h % 2 == 0) and (h % 3 != 0):
        return h // 2, h - 3
    if (h % 2 != 0) and (h % 3 != 0):
        return h - 2, h - 3


@lru_cache(None)
def f(h):
    if h == 1:
        return 'END'
    elif any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    elif all(f(x) == 'P1' for x in moves(h)):
        return 'B1'
    elif any(f(x) == 'B1' for x in moves(h)):
        return 'P2'
    elif all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'B2'


for i in range(100, 1, -1):
    print(i, f(i))
