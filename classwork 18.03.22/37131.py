with open('24 (3).txt','r') as f:
    k = []
    for line in f.readlines():
        for elem in line:
            if elem != '\n':
                k.append(elem)
count = 1
ans = []
for index in range(0,len(k) - 1):
    if (k[index] == 'K' and k[index + 1] == 'L') or (k[index] == 'L' and k[index + 1] == 'K'):
        ans.append(count)
        count = 1
    else:
        count += 1

print(max(ans))
