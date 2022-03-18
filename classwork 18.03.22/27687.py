with open('24_demo.txt','r') as f:
    k = []
    for line in f.readlines():
        for elem in line:
            if elem != '\n':
                k.append(elem)
ans = []
count = 0
for index in range(0,len(k) - 1):
    if k[index] == 'Y':
        count += 1
        for ind in range(index + 1,len(k) - 1):
            if k[ind] != 'Y':
                ans.append(count)
                count = 0
                break
            else:
                count += 1
print(max(ans))