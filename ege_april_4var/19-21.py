from functools import lru_cache
def moves(h):
    a,b = h
    return (a + 1,b + 2),(a + 2,b + 1),(a * 2,b),(a, b * 2)


@lru_cache(None)
def f(h):
    if sum(h) >= 47:
        return 'END'
    elif any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    elif all(f(x) == 'P1' for x in moves(h)):
        return 'B1'
    elif any(f(x) == 'B1' for x in moves(h)):
        return 'P2'
    elif all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'B2'


for i in range(1,37):
    h = 10,i
    print(i,f(h))