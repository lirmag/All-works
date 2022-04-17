with open('17 (9).txt','r') as f:
    k = list(map(int,f.readlines()))
s = 0
count = 0
sm = []
for index in range(0,len(k) - 1):
    s += 1
    for ind in range(s,len(k)):
        if (k[ind] * k[index]) % 34 != 0:
            count += 1
            sm.append(k[ind] + k[index])
print(count,max(sm))