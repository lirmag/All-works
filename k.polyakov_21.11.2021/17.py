f = open('17-204.txt','r')
lines = f.readlines()
k = []
ans = []
for el in lines:
    k.append(el)
count = 0
for ind in range(0,len(k) - 2):
    if (int(k[ind + 1]) > 0) and (k[ind + 1][len(k[ind + 1]) - 1] == '9') and (int(k[ind]) < 0) and (int(k[ind+2]) < 0):
        ans.append(int(k[ind]) + int(k[ind + 1]) + int(k[ind + 2]))
        count += 1
print(count,max(ans))