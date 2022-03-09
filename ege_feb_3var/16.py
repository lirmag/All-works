def f(N):
    if N < 8:
        f(N + 3)
        print(N)
        f(2 * N)

print(f(1))