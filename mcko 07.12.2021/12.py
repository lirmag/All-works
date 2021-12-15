f = open('12.txt','r')
k = []
lines = f.readlines()
for el in lines:
    el = int(el)
    k.append(el)
sum_1 = []
count = 0
for ind in range(0,len(k) - 1):
    if (k[ind] % 5 == 0) or (k[ind + 1] % 5 == 0):
        count += 1
        sum_1.append(k[ind] + k[ind + 1])
print(count,min(sum_1))