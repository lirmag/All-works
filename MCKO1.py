# task1
k = (True,False)
print('x y z w f')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                f = not (x and y) and (y or z) or not w
                if f is False:
                    print(int(x), int(y), int(z), int(w), int(f))
                # ¬ (x  y)  (y  z)  ¬w
 # y w x z

# task3
k = []
def f(number):
    s = number
    n = 1
    while s < 45:
        s = s + 6
        n = n * 4
    return n
for number in range(1,100001):
    if f(number) == 256:
        k.append(number)
print(max(k))

# task13
k = []
def f(n):
    x = n
    L = 0
    M = 0
    while x > 0:
        M = M + 2
        if x % 8 != 0:
            L = L + 1
        x = x // 8
    return L,M

for n in range(1,10000):
    print(f(n))
    if f(n) == (2,6):
        k.append(n)
print(k)
print(min(k))