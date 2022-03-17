c = open('17 (5).txt','r')
k = []
sr = 0
a = 0
count = 0
sum_1 = []
lines = c.readlines()
for elem in lines:
    elem = int(elem)
    k.append(elem)
for elem in k:
    if elem % 2 != 0:
        a += 1
        sr += elem
ar = sr // a
for index in range(0,len(k) - 1):
    if ((k[index] % 5 == 0) or (k[index + 1] % 5 == 0)) and ((k[index] < ar) or (k[index + 1] < ar)):
        count += 1
        sum_1.append(k[index] + k[index + 1])
print(count,max(sum_1))