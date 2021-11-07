f = open('17 (2).txt','r')
k = []
s = 0
count = 0
sum_1 = []
for element in f:
    element = int(element)
    k.append(element)
for i in range(0,len(k) - 1):
    s += 1
    for j in range(s,len(k)):
        if (((k[i] + k[j]) % 2 != 0) and ((k[i] * k[j]) % 5 == 0)):
            count += 1
            sum_1.append(k[i] + k[j])
print(count)
print(max(sum_1))