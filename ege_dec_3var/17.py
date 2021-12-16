f = open('17 (2).txt','r')
k = []
lines = f.readlines()
for el in lines:
    el = int(el)
    k.append(el)
s = 0
count = 0
sum_1 = []
for el in range(0,len(k) - 1):
    s += 1
    for elem in range(s,len(k)):
        if ((k[el] * k[elem]) % 10 == 0):
            count += 1
            sum_1.append(k[el] + k[elem])
print(count,max(sum_1))