with open('24_demo (1).txt','r') as f:
    k = []
    for line in f.readlines():
        for elem in line:
            if elem != '\n':
                k.append(elem)
count = 1
ans = []
for index in range(0,len(k) - 1):
    if k[index] != k[index + 1]:
        count += 1
    else:
        ans.append(count)
        count = 1
print(max(ans))