f = open('17 (13).txt','r')
lines = f.readlines()
k = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
s = 0
count = 0
sum_1 = []
for i in range(0,len(k) - 1):
    s += 1
    for j in range(s,len(k)):
        if ((k[i] % 160) != (k[j] % 160) and ((k[i] % 7 == 0) or (k[j] % 7 == 0))) is True:
            count += 1
            sum_1.append(k[i] + k[j])
print(count,max(sum_1))