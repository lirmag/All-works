f = open('24 (2).txt','r')
lines = f.readlines()
c = 1
d = dict()
k = []
for line in lines:
    for element in line:
        k.append(element)
for i in range(0,len(k) - 1):
    if ((i + 2) < (len(k) - 1)) and k[i] == k[i + 2]:
        if k[i + 1] not in d:
            d[k[i + 1]] = 1
        else:
            d[k[i + 1]] += 1
max_key = max(d, key=d.get)
print(max_key)