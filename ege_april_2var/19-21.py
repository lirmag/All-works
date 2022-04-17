# from functools import lru_cache
# def moves(h):
#     a,b = h
#     if (a % 2 == 0) and (b % 2 == 0):
#         return (a - 1, b), (a, b - 1), (a // 2, b), (a, b // 2)
#     elif (a % 2 != 0) and (b % 2 == 0):
#         return (a - 1, b), (a, b - 1), ((a + 1) // 2, b), (a, b // 2)
#     elif (a % 2 == 0) and (b % 2 != 0):
#         return (a - 1, b), (a, b - 1), (a // 2, b), (a, (b + 1) // 2)
#     elif (a % 2 != 0) and (b % 2 != 0):
#         return (a - 1, b), (a, b - 1), ((a + 1) // 2, b), (a, (b + 1) // 2)
#
# @lru_cache(None)
# def game(h):
#     if h[1] <= 1 or h[0] <= 1:
#         return
#     if sum(h) <= 20:
#         return 'END'
#     if any(game(x) == 'END' for x in moves(h)):
#         return 'P1'
#     if all(game(x) == 'P1' for x in moves(h)):
#         return 'B1'
#     if any(game(x) == 'B1' for x in moves(h)):
#         return 'P2'
#     if all(game(x) == 'P1' or game(x) == 'P1' for x in moves(h)):
#         return 'B2'
#
#
# for i in range(10,101):
#     h = 10,i
#     print(i,game(h))
from functools import lru_cache


def moves(h):
    a, b = h
    if (a % 2 == 0) and (b % 2 == 0):
        return (a - 1, b), (a, b - 1), (a // 2, b), (a, b // 2)
    elif (a % 2 != 0) and (b % 2 == 0):
        return (a - 1, b), (a, b - 1), ((a + 1) // 2, b), (a, b // 2)
    elif (a % 2 == 0) and (b % 2 != 0):
        return (a - 1, b), (a, b - 1), (a // 2, b), (a, (b + 1) // 2)
    elif (a % 2 != 0) and (b % 2 != 0):
        return (a - 1, b), (a, b - 1), ((a + 1) // 2, b), (a, (b + 1) // 2)


@lru_cache(None)
def f(h):
    if h[0] <= 1 or h[1] <= 1:
        return
    if sum(h) <= 20:
        return 'END'
    elif any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    elif all(f(x) == 'P1' for x in moves(h)):
        return 'B1'
    elif any(f(x) == 'B1' for x in moves(h)):
        return 'P2'
    elif all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'B2'


for i in range(11, 101):
    h = 10, i
    print(i, f(h))
