from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1),  (2 * a, b),  (a, 2 * b)


@lru_cache(None)
def game(h):
    if sum(h) >= 77:
        return 'END'
    elif any(game(x) == 'END' for x in moves(h)):
        return 'P1'
    elif all(game(x) == 'P1' for x in moves(h)):
        return 'B1'
    elif any(game(x) == 'B1' for x in moves(h)):
        return 'P2'
    elif all(game(x) == 'P2' or game(x) == 'P1' for x in moves(h)):
        return 'B2'


for i in range(1, 100):
    h = 7, i
    print(i, game(h))
