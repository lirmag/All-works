# ДЕЛ(A, 34) /\ (ДЕЛ(283, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(120, x)))

def f(A, x):
    if A % x == 0:
        return 1
    else:
        return 0
A = 1
while True:
    for x in range(1,1000000):
        if   f(A, 34) and (f(283, x) <= (not f(A, x) <= (not f(120, x)))):
            br
        else:
            break
    A += 1