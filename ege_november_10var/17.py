f = open('17 (10).txt','r')
lines = f.readlines()
k = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
s = 0
count = 0
sum_1 = []
for i in range(0,len(k) - 1):
    s += 1
    for j in range(s,len(k)):
        if (k[i] - k[j]) % 60 == 0:
            count += 1
            sum_1.append(k[i] - k[j])
print(count,max(sum_1))