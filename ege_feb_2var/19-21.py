from functools import lru_cache
import math



def moves(h):
    a, b = h
    return (a - 1,b), (a,b - 1), (math.ceil(a / 2),b),(a,math.ceil(b / 2))

@lru_cache(None)
def f(h):
    if h[0] <= 1 or h[1] <= 1:
        return
    if sum(h) <= 40:
        return 'END'
    elif any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    elif all(f(x) == 'P1' for x in moves(h)):
        return 'B1'
    elif any(f(x) == 'B1' for x in moves(h)):
        return 'P2'
    elif all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'B2'


for i in range(21,100):
    h = 20, i
    print(i, f(h))
