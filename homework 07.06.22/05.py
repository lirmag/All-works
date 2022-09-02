res = set()
for number in range(10,1001):
    n = bin(number)[2::]
    if n[0] == '1':
        n = n[1::]
        while n[0] == '0' and (len(n) > 1):
            n = n[1::]
    ans = int(n,base=2) - number
    res.add(ans)


# print(int('10000',base=2))
print(len(res))