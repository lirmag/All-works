f = open('17 (6).txt','r')
k = []
sum_1 = []
count = 0


for el in f:
    el = int(el)
    k.append(el)

for index in range(0,len(k)):
    if index == len(k) - 2:
        break
    if ((k[index]*k[index] + k[index + 1]*k[index + 1] > k[index + 2]*k[index + 2]) and (k[index]*k[index] + k[index + 2]*k[index + 2] > k[index + 1]*k[index + 1]) and (k[index + 1]*k[index + 1] + k[index + 2]*k[index + 2] > k[index]*k[index])):
        count += 1
        sum_1.append(k[index] + k[index + 1] + k[index + 2])
print(count,max(sum_1))

