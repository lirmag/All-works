k = []
for number in range(10,1001):
    num = bin(number)[2:]
    num = num[1:]
    while num[0] == '0':
        num = num[1:]
        if len(num) == 0:
            num = '0'
            break
    a = int(num,base=2)
    ans = number - a
    k.append(ans)
print(len(set(k)))