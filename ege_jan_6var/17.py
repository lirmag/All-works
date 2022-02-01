c = open('17 (4).txt','r')
lines = c.readlines()
k = []
count = 0
sum_1 = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
s = 0
for index in range(0,len(k) - 1):
    s += 1
    for ind in range(s,len(k)):
        if (k[ind] - k[index]) % 60 == 0:
            count += 1
            sum_1.append(k[ind] - k[index])

print(count,max(sum_1))