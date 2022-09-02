from functools import lru_cache


def moves(h):
    return (h + 1), (h + 2), (h * 2)


@lru_cache(None)
def f(h):
    if h >= 42:
        return 'end'
    elif any(f(x) == 'end' for x in moves(h)):
        return 'p1'
    elif all(f(x) == 'p1' for x in moves(h)):
        return 'b1'
    elif any(f(x) == 'b1' for x in moves(h)):
        return 'p2'
    elif all(f(x) == 'p1' or f(x) == 'p2' for x in moves(h)):
        return 'b2'


for i in range(1, 42):
    print(i, f(i))
