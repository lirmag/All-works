# if n % 2 == 0 and n > 1:
#     Number = (n-1) - (n-2) +3n
#     if n % 2 != 0 and n > 1:
#         Number = (n - 2) - (n -3) + 2n

def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    elif n % 2 == 0 and n > 1:
        return f(n - 1) - f(n - 2) + 3 * n
    elif n % 2 != 0 and n > 1:
        return f(n - 2) - f(n - 3) + 2 * n


print(f(40))
