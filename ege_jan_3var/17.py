c = open('17 (1).txt','r')
lines = c.readlines()
k = []
for elem in lines:
    elem = int(elem)
    k.append(elem)

count = 0
sum_1 = []

for index in range(0,len(k) - 2):
    if (((k[index] * k[index]) + (k[index + 1] * k[index + 1])) ==
            (k[index + 2] * k[index + 2])) or (((k[index] * k[index]) + (k[index + 2] * k[index + 2])) ==
                                               (k[index + 1] * k[index + 1])) or (((k[index + 1] * k[index + 1]) + (k[index + 2] * k[index + 2])) ==
                                                                          (k[index] * k[index])):
        count += 1
        sum_1.append(k[index] + k[index + 1] + k[index + 2])

print(count,max(sum_1))