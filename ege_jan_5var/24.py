c = open('24_demo (1).txt','r')
lines = c.readlines()
k = []
count = 0
ans = []
for line in lines:
    for elem in line:
        k.append(elem)

for index in range(0,len(k) - 1):
    count = 0
    if k[index] == 'X':
        count += 1
        for ind in range(index + 1,len(k) - 1):
            if k[ind] == 'X':
                count += 1
            else:
                break
    if count != 0:
        ans.append(count)

print(max(ans))