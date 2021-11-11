f = open('17 (11).txt','r')
k = []
lines = f.readlines()
for elem in lines:
    elem = int(elem)
    k.append(elem)
print(k)
count = 0
sum_1 = []
for i in range(0,len(k) - 1):
    if (k[i] % 3 == 0) or (k[i + 1] % 3 == 0):
        count += 1
        sum_1.append(k[i] + k[i + 1])
print(count,max(sum_1))