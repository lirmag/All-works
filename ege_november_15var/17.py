f = open('17 (15).txt','r')
lines= f.readlines()
k = []
for el in lines:
    el = int(el)
    k.append(el)
s = 0
count = 0
sum_1 = []
for i in range(0,len(k) - 1):
    s += 1
    for j in range(s,len(k)):
        if (((k[i] - k[j]) % 2 == 0) and ((k[i] % 19 == 0) or (k[j] % 19 == 0))):
            count += 1
            sum_1.append(k[j] + k[i])
print(count,max(sum_1))