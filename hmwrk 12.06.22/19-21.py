from functools import lru_cache


def moves(h):
    return (h + 1), (h * 3 - 2)


@lru_cache(None)
def game(h):
    if h >= 40:
        return 'end'
    elif any(game(x) == 'end' for x in moves(h)):
        return 'p1'
    elif all(game(x) == 'p1' for x in moves(h)):
        return 'b1'
    elif any(game(x) == 'b1' for x in moves(h)):
        return 'p2'
    elif all(game(x) == 'p1' or game(x) == 'p2' for x in moves(h)):
        return 'b2'


for i in range(2,40):
    print(i,game(i))
