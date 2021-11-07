f = open('24.txt','r')
lines = f.readlines()
k = []
answer = []
c = 1
d = dict()
for line in lines:
    for element in line:
        k.append(element)
for i in range(0,len(k) - 1):
    if k[i] == 'A' and k[i + 1] != 'A':
        if k[i + 1] not in d:
            d[k[i + 1]] = 1
        else:
            d[k[i + 1]] += 1
max_key = max(d,key=d.get)
print(max_key)





