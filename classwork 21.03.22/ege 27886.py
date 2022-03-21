# 5955 1939
with open('27886.txt','r') as f:
    s = sorted(list(map(int,f.readlines())))
d = dict()
for ind in range(0,len(s) - 1):
    count = 0
    sum_1 = 0
    for index in range(ind,len(s) - 1):
        if (sum_1 + s[index]) > 5955:
            d[sum_1] = count
            break
        else:
            count += 1
            sum_1 += s[index]
print(d)
print(max(d,key=d.get))
