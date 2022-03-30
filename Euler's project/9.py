p = 1000
flag = True
for a in range(1, p + 1):
    for b in range(a + 1, p + 1):
        c = p - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a, b, c)
            print(a * b * c)
            flag = False
            break
    if flag is False:
        break
