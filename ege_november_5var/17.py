f = open('17 (6).txt','r')
s = 0
k = []
count = 0
sum_1 = []
lines = f.readlines()
for element in lines:
    element = int(element)
    k.append(element)
for i in range(0,len(k) - 1):
    s += 1
    for j in range(s,len(k)):
        if (k[i] + k[j]) % 10 == 0:
            count += 1
            sum_1.append(k[i] + k[j])
print(count, max(sum_1))