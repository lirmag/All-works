c = open('17.txt', 'r')
k = []
count = 0
sum_1 = []
lines = c.readlines()

for elem in lines:
    elem = int(elem)
    k.append(elem)

for index in range(0,len(k) - 1):
    if (((k[index] * k[index + 1]) % 15 == 0) and ((k[index] + k[index + 1]) % 7 == 0)):
        count += 1
        sum_1.append(k[index] + k[index + 1])
print(count,max(sum_1))