f = open('24 (3).txt')
lines = f.readlines()
d = dict()
k = []
for line in lines:
    for element in line:
        k.append(element)
for i in range(0,len(k) - 1):
    if k[i] == 'E':
        if k[i+1] not in d:
            d[k[i+1]] = 1
        else:
            d[k[i + 1]] += 1
max_key = max(d,key=d.get)
print(max_key)
