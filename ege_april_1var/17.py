with open('17 (8).txt','r') as f:
    k = list(map(int,f.readlines()))
count = 0
sm = []
for ind in range(0,len(k) - 1):
    if ((k[ind] % 3 == 0) or (k[ind + 1] % 3 == 0)) and ((k[ind] + k[ind + 1]) % 5 == 0):
        count += 1
        sm.append(k[ind] + k[ind + 1])
print(count)
print(max(sm))