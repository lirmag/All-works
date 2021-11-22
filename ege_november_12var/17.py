f = open('17 (12).txt','r')
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
        if ((k[i] % 31 == 0) or (k[j] % 31 == 0)) and ((k[i] - k[j]) % 2 == 0):
            count += 1
            sum_1.append(k[i] + k[j])
print(count,max(sum_1))
