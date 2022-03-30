with open('17 (7).txt','r') as f:
    k = list(map(int, f.readlines()))
count = 0
sm = []
i = 0
for index in range(0,len(k) - 1):
    i += 1
    for ind in range(i,len(k)):
        if ((k[ind] % 7 == 0) or (k[index] % 7 == 0)) and ((k[index] % 160) != (k[ind] % 160)):
            count += 1
            sm.append(k[index] + k[ind])
print(count,max(sm))