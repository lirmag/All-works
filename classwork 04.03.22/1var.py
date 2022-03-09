c = open('24-179.txt', 'r')
lines = c.readlines()
k = []
count = 0
d = dict()
for line in lines:
    for elem in line:
        k.append(elem)

for index in range(0, len(k) - 1):
    if (k[index] == 'C') and (k[index + 1] == 'B') and (
            (k[index + 2] != 'A') and (k[index + 2] != 'B') and (k[index + 2] != 'F')) and (k[index + 3] == 'B') and (
            k[index + 4] == 'C'):
        count += 1
        if k[index + 2] not in d:
            d[k[index + 2]] = 1
        else:
            d[k[index + 2]] += 1
print(count)
print(d)
