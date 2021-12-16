for n in range(1,101):
    num = bin(n)[2:]
    sum_1 = 0
    sum_2 = 0
    for a in num:
        a = int(a)
        sum_1 += a
    ans = num + str(sum_1 % 2)
    for el in num:
        el = int(el)
        sum_2 += el
    ans = ans + str(sum_2 % 2)
    ans = int(ans,base=2)
    if ans > 97:
        print(n)
        break
