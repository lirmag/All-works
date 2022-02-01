c = open('17 (3).txt', 'r')
lines = c.readlines()
k = []
count = 0
sum_1 = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
for index in range(0,len(k) - 2):
    if ((k[index] * k[index] + k[index + 1] * k[index + 1] > k[index + 2] * k[index + 2]) and (
            k[index] * k[index] + k[index + 2] * k[index + 2] > k[index + 1] * k[index + 1]) and (
            k[index + 1] * k[index + 1] + k[index + 2] * k[index + 2] > k[index] * k[index])):
        count += 1
        sum_1.append(k[index] + k[index + 1] + k[index + 2])
print(count,max(sum_1))



