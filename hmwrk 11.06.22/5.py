res = set()
for number in range(100,3001):
    n = bin(number)[2::]
    if n[0] == '1':
        n = n[1::]
        while n[0] == '0' and (len(n) > 1):
            n = n[1::]
    if n[0] == '0':
        n = 0
    else:
        n = int(n,base=2)
    res.add(number - n)
print(res,len(res),sep='\n')
