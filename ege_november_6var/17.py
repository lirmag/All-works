f = open('17 (7).txt','r')
k = []
lines = f.readlines()
for element in lines:
    element = int(element)
    k.append(element)
s = 0
sum_1 = []
count = 0
for i in range(0,len(k) - 1):
    s += 1
    for j in range(s,len(k)):
        if (k[i] + k[j]) % 126 == 0:
            count += 1
            sum_1.append(k[i] + k[j])
print(count,max(sum_1))
