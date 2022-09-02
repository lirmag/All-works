with open('107_17.txt','r') as f:
    k = list(map(int,f.readlines()))
m = []
for elem in k:
    if elem % 21 == 0:
        m.append(elem)
mn = min(m)
count = 0
sm = []
for index in range(0,len(k) - 1):
    if (k[index] % mn == 0) or (k[index + 1] % mn == 0):
        count += 1
        sm.append(k[index] + k[index + 1])
print(count,max(sm))