f = open('17 (5).txt','r')
lines = f.readlines()
k = []
for el in lines:
    el = int(el)
    k.append(el)
s = 0
count = 0
sum_1 = []
for ind in range(0,len(k) - 1):
    s += 1
    for elem in range(s,len(k)):
        if ((k[ind] * k[elem]) % 26 == 0):
            count += 1
            sum_1.append(k[ind] + k[elem])
print(count,max(sum_1))