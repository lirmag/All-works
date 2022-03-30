with open('24 (4).txt','r') as f:
    k = list(map(str,f.readline()))
count = 1
ans = []
for index in range(0,len(k) - 1):
    if (k[index] == 'd' and k[index + 1] == 'a') or (k[index] == 'a' and k[index + 1] == 'd'):
        ans.append(count)
        count = 1
    else:
        count += 1
print(max(ans))