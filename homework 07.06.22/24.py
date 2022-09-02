with open('24 (6).txt','r') as f:
    k = list(map(str,f.readlines()))
n = []
n_c = 0
for line in k:
    n.append(line.count('N'))
d = dict()
for line in k:
    if line.count('N') == min(n):
        for index in range(0,len(line) - 2):
            if d[line[index]] not in d:
                d[line[index]] = 1
            else:
                d[line[index]] += 1
mk = max(d,key=d.get)
print(mk)
