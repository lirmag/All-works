f = open('17 (1).txt','r')
lines = f.readlines()
k = []
for el in lines:
    el = int(el)
    k.append(el)
print(len(k))
count = 0
sum_1 = []
for ind in range(0,5541):
    if (((k[ind] % 5 == 0) or (k[ind + 1] % 5 == 0)) and ((k[ind] + k[ind + 1]) % 7 == 0)):
        count += 1
        sum_1.append(k[ind] + k[ind + 1])
print(count,max(sum_1))