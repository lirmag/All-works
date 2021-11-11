f = open('24 (4).txt','r')
lines = f.readlines()
d = dict()
k = []
for line in lines:
    for elem in line:
        k.append(elem)
for i in range(0,len(k) - 1):
    if i == (len(k) - 3):
        break
    if k[i] == k[i + 2]:
        if k[i + 1] not in d:
            d[k[i + 1]] = 1
        else:
            d[k[i + 1]] += 1
max_key = max(d,key=d.get)
print(max_key)