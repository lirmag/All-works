with open('24 (1).txt','r') as f:
    k = []
    for line in f.readlines():
        for elem in line:
            if elem != '\n':
                k.append(elem)
d = dict()
for index in range(0,len(k) - 1):
    if k[index] == 'E':
        if k[index +  1] not in d:
            d[k[index + 1]] = 1
        else:
            d[k[index + 1]] += 1
print(max(d,key=d.get))