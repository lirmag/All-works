with open('2.txt','r') as f:
     k = list(map(str,f.readline()))
c = 0
ans = []
for ind in range(0,len(k) - 1):
    if ((k[ind] == 'a') and (k[ind + 1] == 'd')) or ((k[ind] == 'd') and (k[ind + 1] == 'a')):
        ans.append(c)
        c = 0
    else:
        c += 1
print(max(ans))
