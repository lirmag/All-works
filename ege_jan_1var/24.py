c = open('24 (3).txt','r')
f = c.readlines()
k = ['1']
a = []
min = 100
count = 0
for line in f:
    for el in line:
        if el == 'G':
            count += 1
    if count < min and count != 0:
        min = count
        k[0] = line
    count = 0
k = k[0][0:len(k) - 2]
print(k)
print(min)



d = dict()
for el in k:
    for elem in el:
        if elem not in d:
            d[elem] = 1
        else:
            d[elem] += 1

max_key = max(d,key=d.get)
print(max_key)
print(d)

