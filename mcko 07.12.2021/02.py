for x in range(2,1001):
    num = bin(x)[2:]
    sum_1 = 0
    sum_2 = 0
    ans = ''
    for n in num:
        sum_1 += int(n)
    ans = num + str(sum_1 % 2)
    for s in ans:
        sum_2 += int(s)
    ans += str(sum_2 % 2)
    ans = int(ans,base=2)
    if ans < 98:
        print(x)
# 24