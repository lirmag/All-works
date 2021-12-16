f = open('12.txt', 'r')
lines = f.readlines()
k = []
for el in lines:
    el = int(el)
    k.append(el)
count = 0
sum_1 = []
for ind in range(0, len(k) - 1):
    if (k[ind] % 9 == 0) or (k[ind + 1] % 9 == 0):
        count += 1
        sum_1.append(k[ind] + k[ind + 1])
print(count, max(sum_1))
