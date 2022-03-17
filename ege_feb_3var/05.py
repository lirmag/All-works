k = set()
for N in range(100,3001):
    number = str(bin(N)[2:])
    for elem in number:
        if elem == '1':
            number = number.replace('1','',1)
            while number[0] == '0':
                number = number[1::]
                if len(number) == 0:
                    number = 0
                    break
        break
    if number != 0:
        number = int(number,base=2)
    ans = N - number
    k.add(ans)
print(k)
print(len(k))