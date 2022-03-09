from functools import lru_cache


def moves(h):
    return h + 1, h + 4, h * 5

@lru_cache(None)
def game(h):
    if h >= 68:
        return 'END'
    elif any(game(x) == 'END' for x in moves(h)):
        return 'P1'
    elif all(game(x) == 'P1' for x in moves(h)):
        return 'B1'
    elif any(game(x) == 'B1' for x in moves(h)):
        return 'P2'
    elif all(game(x) == 'P2' or game(x) == 'P1' for x in moves(h)):
        return 'B2'


for i in range(1,68):
    print(i,game(i))
