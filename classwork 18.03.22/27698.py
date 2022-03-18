with open('zadanie24_2.txt','r')  as f:
    k = []
    for line in f.readlines():
        for elem in line:
            if elem != '\n':
                k.append(elem)
count = 0
ans = []
for index in range(0,len(k) - 1):
    if k[index] == 'R':
        count += 1
        for ind in range(index + 1,len(k) - 1):
            if k[ind] != 'R':
                ans.append(count)
                count = 0
                break
            else:
                count += 1
print(max(ans))