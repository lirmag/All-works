c = open('17 (2).txt','r')
lines = c.readlines()
k = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
s = 0
count = 0
sum_1 = []
for index in range(0,len(k) - 1):
    s += 1
    for ind in range(s,len(k)):
        if ((k[index] - k[ind]) % 80) == 0:
            count += 1
            sum_1.append(k[index] - k[ind])
print(count,max(sum_1))