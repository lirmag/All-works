with open('17 (3).txt','r') as f:
    k = list(map(int,f.readlines()))

count = 0
sm = []
s = 0
for index in range(0,len(k) - 1):
    s += 1
    for ind in range(s,len(k)):
        if ((k[ind] - k[index]) % 2 == 0) and ((k[index] % 31 == 0) or (k[ind] % 31 == 0)):
            count += 1
            sm.append(k[index] + k[ind])
print(count,max(sm))
