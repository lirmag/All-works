c = open('24.txt', 'r')
lines = c.readlines()
max = 10000
k = ['1']
for line in lines:
    count = 0
    for elem in line:
        if elem == 'G':
            count += 1
    if count < max:
        max = count
        k[0] = line

d = dict()
for ind in range(0,len(k[0]) - 1):
    if k[0][ind] not in d:
        d[k[0][ind]] = 1
    else:
        d[k[0][ind]] += 1

print(d)
