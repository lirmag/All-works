with open('17.txt','r') as f:
    k = list(map(int,f.readlines()))
s = 0
count = 0
sm = []
for index in range(0,len(k) - 1):
    s += 1
    for ind in range(s,len(k)):
        if (k[index] + k[ind]) % 120 == 0:
            count += 1
            sm.append(k[index] + k[ind])
print(count,max(sm))