
# Zadanie 2:
k = (True,False)
print('x y z w F')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                F = ((x >= w) or y and not z) and ((y >= (not z)) or x and not w)
                if F is False:
                    print(int(x), int(y), int(z), int(w), int(F))
                # ((x → w) ∨ y ∧ ¬z) ∧ ((y → ¬z) ∨ x ∧ ¬w).
                # w x y z
# Zadanie 6:
k = []
def f(number):
    n = 1
    s = number
    while s > 200:
        s = s - 15
        n = n + 3
    return n
for i in range (1,10000):
    if f(i) == 46:
        k.append(i)
print(max(k))
# 425
# Zadanie 16:
suma = 0
def f(n):
    if n > 25:
        return 2 * n * n * n + n * n
    if n <= 25:
        return f(n+2) + 2 * f(n + 3)
k = f(2)
while k > 0:
    chislo = k % 10
    suma = suma + chislo
    k =  k // 10
print(suma)
# 33
# Zadanie 22:
k = []
def f(number):
    a = 0
    b = 0
    d = 0
    x = number
    while x > 0:
        if d % 2 == 0:
            a += x % 10
        else:
            b += x % 10
        x = x // 10
        d += 1
    return a, b
for i in range(1,10000):
        if f(i) == (14,12):
            k.append(i)
print(min(k))
# 3599