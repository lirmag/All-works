c = open('08', 'r')
lines = c.readlines()
k = []
count = 0
sum_3 = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
for index in range(0, len(k) - 1):
    sum_1 = 0
    sum_2 = 0
    for elem in bin(k[index])[2:]:
        sum_1 += int(elem)
    if sum_1 > 5 and sum_1 % 2 != 0:
        count += 1
        sum_3.append(k[index] + k[index + 1])
    else:
        for elem in bin(k[index + 1])[2:]:
            sum_2 += int(elem)
        if sum_2 > 5 and sum_2 % 2 != 0:
            count += 1
            sum_3.append(k[index] + k[index + 1])
print(count, max(sum_3))
