N = int(input())
def f(N,sum_1 = 1):
    if N > 0:
        f(N - 1,sum_1)
        sum_1 *= N




print(f(N))