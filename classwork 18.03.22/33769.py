with open('24 (2).txt','r') as f:
    k = []
    for line in f.readlines():
        for elem in line:
            if elem != '\n':
                k.append(elem)
d = dict()
for index in range(0,len(k) - 2):
    if k[index] == k[index + 1]:
        if k[index + 2] not in d:
            d[k[index + 2]] = 1
        else:
            d[k[index + 2]] += 1
print(max(d,key=d.get))
