c = open('24.txt','r')
lines = c.readlines()
k = []
for line in lines:
    for elem in line:
        k.append(elem)
count = 0
ans = []
for index in range(0,len(k) - 1):
    if k[index] != 'P':
        count += 1
        a = index
        while (k[a] != 'P') and (k[a + 1] != 'P') and (a != len(k) - 1):
            count += 1
            a += 1
        else:
            ans.append(count)
            count = 0
print(max(ans))