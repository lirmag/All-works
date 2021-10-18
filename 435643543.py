list = []
def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n / 3) - 1
    if n >= 2 and n % 3 != 0:
        return f(n - 1) + 17
for n in range(1,999999):
    if f(n) == 110:
        list.append(n)
print(min(list))