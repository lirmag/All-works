f = open('12.txt','r')
k = []
ans = []
lines = f.readlines()
for elem in lines:
    elem = int(elem)
    k.append(elem)
count = 0
for ind in range(0,len(k) - 1):
    if (k[ind] % 5 == 0) or (k[ind + 1] % 5 == 0):
        count += 1
        ans.append(k[ind] + k[ind+1])
print(count,min(ans))