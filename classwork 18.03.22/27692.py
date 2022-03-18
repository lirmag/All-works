with open('zadanie24_1.txt','r') as f:
    k = []
    for line in f.readlines():
        for elem in line:
            if elem != '\n':
                k.append(elem)
count = 0
ans = []
for index in range(0,len(k) - 1):
    if k[index] == 'B':
        count += 1
        for ind in range(index + 1,len(k) - 1):
            if k[ind] != 'B':
                ans.append(count)
                count = 0
                break
            else:
                count += 1
print(max(ans))