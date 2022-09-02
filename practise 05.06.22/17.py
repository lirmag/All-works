with open('17 (12).txt','r') as f:
    k = list(map(int,f.readlines()))
c = 0
s = 0
for elem in k:
    if elem % 2 == 0:
        s += elem
        c += 1
ar = s // c
count = 0
sm = []
for ind in range(0,len(k) - 1):
    if ((k[ind] % 3 == 0) or (k[ind + 1] % 3 == 0)) and ((k[ind] < ar) or (k[ind + 1] < ar)):
        count += 1
        sm.append(k[ind] + k[ind + 1])
print(count,max(sm))