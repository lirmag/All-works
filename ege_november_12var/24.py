f = open('24 (5).txt','r')
lines = f.readlines()
k = []
for line in lines:
    for elem in line:
        k.append(elem)
d = dict()
for i in range(0,len(k) - 1):
    if k[i] == 'E':
        if k[i + 1] not in d:
            d[k[i + 1]] = 1
        else:
            d[k[i + 1]] += 1
max_key = max(d,key=d.get)
print(max_key)
