k = set()


def f(l,n):
    global k
    if (l > 4000000) or (n > 4000000) or (l + n > 4000000):
        return 0
    else:
        k.add(n)
        k.add(l + n)
        return f(n,l + n)


f(0,1)
sum_1 = 0
for elem in sorted(k):
    if elem % 2 == 0:
        sum_1 += elem
print(sum_1)


