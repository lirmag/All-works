with open('17 (1).txt','r') as f:
    k = list(map(int,f.readlines()))


count = 0
sm = []
s = 0
for index in range(0,len(k) - 1):
    s += 1
    for ind in range(s,len(k)):
        if ((k[index] % 160) != (k[ind] % 160)) and ((k[index] % 7 == 0) or (k[index] % 7 == 0)):
            count += 1
            sm.append(k[index] + k[ind])


print(count,max(sm))