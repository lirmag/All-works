def f(number):
    i = 2
    k = []
    while i ** 2 < number:
        if number % i == 0:
            k.append(number // i)
            k.append(i)
        i += 1
        if i ** 2 == number:
            k.append(i)
    if len(k) >= 2:
        k = sorted(k)[::-1]
        return k[0] + k[1]
    else:
        return 0


c = 0
for number in range(10000001,1000000000000000000001):
    if c == 5:
        break
    if (f(number) > 0) and (f(number) < 10000):
        print(f(number))
        c += 1
