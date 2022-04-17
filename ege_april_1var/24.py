with open('24 (2).txt', 'r') as f:
    k = list(map(str,f.readline()))
count = 1
mx = []
for ind in range(0,len(k) - 1):
    if (k[ind] == 'a' and k[ind + 1] == 'd') or (k[ind] == 'd' and k[ind + 1] == 'a'):
        mx.append(count)
        count = 1
    else:
        count += 1
print(max(mx))