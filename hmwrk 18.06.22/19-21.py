from functools import lru_cache
def moves(h):
    a,b = h
    return (a + 1,b),(a,b + 1),(a * 2,b),(a,b * 2)


@lru_cache(None)
def f(h):
    if sum(h) >= 107:
        return 'end'
    elif any(f(x) == 'end' for x in moves(h)):
        return 'p1'
    elif all(f(x) == 'p1' for x in moves(h)):
        return 'b1'
    elif any(f(x) == 'b1' for x in moves(h)):
        return 'p2'
    elif all(f(x) == 'p1' or f(x) == 'p2' for x in moves(h)):
        return 'b2'


for i in range(1,94):
    h = 13,i
    print(i,f(h))