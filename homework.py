# var 1:
def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n > 1 and n % 2 == 0:
        return f(n - 1) - f(n - 2) + 3 * n
    if n > 1 and n % 2 != 0:
        return f(n - 2) - f(n - 3) + 2 * n


print(f(40))


# var 2:
def f(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n > 1:
        return f(n - 1) - f(n - 2) + 3 * n


print(f(40))


# var 4:
def f(n):
    if n == 0:
        return 0
    if 1 <= n < 3:
        return 1
    if n >= 3:
        return f(n - 1) + f(n - 2)


print(f(47))

# var 5:
k = []


def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2) + 3
    if n > 0 and n % 2 != 0:
        return 2 * f(n - 1) + 1


for n in range(1, 1001):
    print(f(n))
    k.append(f(n))
print(len(set(k)))

# var 6:
k = []


def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f(n / 2)
    if n > 0 and n % 2 != 0:
        return f(n - 1) + 3


for n in range(1, 1001):
    if f(n) == 18:
        k.append(n)
print(len(k))

# var 7:
k = []


def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n / 3) - 1
    if n >= 2 and n % 3 != 0:
        return f(n - 1) + 17


for n in range(1, 1000001):
    if f(n) == 110:
        k.append(n)
print(min(k))

# var 8:
k = []


def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n / 3) - 1
    if n >= 2 and n % 3 != 0:
        return f(n - 1) + 7


for n in range(1, 1000001):
    if f(n) == 111:
        k.append(n)
print(min(k))

# var 9:
k = []


def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n / 3) + 1
    if n >= 2 and n % 3 != 0:
        return f(n - 2) + 5


for n in range(1, 1000001):
    if f(n) == 73:
        k.append(n)
print(min(k))

# var 10:
k = []


def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    if n >= 2 and n % 2 != 0:
        return f(n - 3) + 3


for n in range(1, 1000001):
    if f(n) == 31:
        k.append(n)
print(min(k))

# var 11:
k = []


def f(n):
    if n == 1:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    if n >= 2 and n % 2 != 0:
        return f(n - 1) + n


for n in range(1, 1000001):
    if f(n) == 19:
        k.append(n)
print(min(k))

# var 12:
k = []


def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n / 3) - 1
    if n >= 2 and n % 3 != 0:
        return f(n - 1) + 17


for n in range(1, 100001):
    if f(n) == 43:
        k.append(n)
print(len(k))

# var 13:
k = []


def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n / 3) - 1
    if n >= 2 and n % 3 != 0:
        return f(n - 1) + 7


for n in range(1, 100001):
    if f(n) == 35:
        k.append(n)
print(len(k))

# var 14:
k = []


def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 3 == 0:
        return f(n / 3) + 1
    if n >= 2 and n % 3 != 0:
        return f(n - 2) + 5


for n in range(1, 100001):
    if f(n) == 55:
        k.append(n)
print(len(k))

# var 15:
k = []


def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    if n >= 2 and n % 2 != 0:
        return f(n - 3) + 3


for n in range(1, 100001):
    if f(n) == 12:
        k.append(n)
print(len(k))

# var 16:
k = []


def f(n):
    if n == 1:
        return 1
    if n >= 2 and n % 2 == 0:
        return f(n / 2) + 1
    if n >= 2 and n % 2 != 0:
        return f(n - 1) + n


for n in range(1, 100001):
    if f(n) == 16:
        k.append(n)
print(len(k))

# var 19:
k = []


def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 4 == 0:
        return n + f(n / 2 - 1)
    if n > 5 and n % 4 != 0:
        return n + f(n + 2)


for n in range(1, 10001):
    try:
        f(n)
        k.append(n)
    except RecursionError:
        print(max(k))

# var 20:
k = []
b = []


def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 5 == 0:
        return n + f(n / 5 + 1)
    if n > 5 and n % 5 != 0:
        return n + f(n + 6)


for n in range(1, 10001):
    try:
        f(n)
        k.append(n)
    except RecursionError:
        pass
for i in k:
    if f(i) > 1000:
        b.append(i)
print(min(b))
