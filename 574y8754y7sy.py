k = 0
list = []
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n/2) + 3
    if n > 0 and n % 2 != 0:
        return  2 * f(n-1) + 1
for n in range(1,1001):
    list.append(f(n))

print(len(set(list)))