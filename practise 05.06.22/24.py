with open('24 (5).txt','r') as f:
    k = list(map(str,f.readline()))
ans = []
count = 0
for ind in range(0,len(k) - 3):
    a = k[ind] + k[ind + 1] + k[ind + 2] + k[ind + 3]
    if a == 'XZZY':
        ans.append(count + 3)
        count = 0
    else:
        count += 1
print(ans)
print(max(ans))
