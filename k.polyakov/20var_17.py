c = open('04', 'r')
lines = c.readlines()
k = []
count = 0
sum_1 = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
for index in range(0, len(k) - 1):
    if (str(k[index])[-1] == '7') or (str(k[index + 1])[-1] == '7'):
        count += 1
        sum_1.append(k[index] + k[index + 1])
print(count, max(sum_1))
