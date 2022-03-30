with open('1.txt','r') as f:
    k = list(map(str,f.readline()))
ans = []
c = 0
for ind in range(0,len(k) - 1):
    if (k[ind] == 'P') and (k[ind + 1] == 'P'):
        ans.append(c)
        c = 0
    else:
        c += 1
print(max(ans))