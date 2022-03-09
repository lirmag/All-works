k = []
s = 0
count = 0
sum_1 = []
c = open('17 (6).txt','r')
lines = c.readlines()
for elem in lines:
    elem = int(elem)
    k.append(elem)
for index in range(0,len(k) - 1):
    s += 1
    for ind in range(s,len(k)):
        if ((k[ind] - k[index]) % 2 == 0) and ((k[index] % 31 == 0) or (k[ind] % 31 == 0)):
            count += 1
            sum_1.append(k[index] + k[ind])
print(count,max(sum_1))