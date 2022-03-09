c = open('17', 'r')
lines = c.readlines()
k = []
count = 0
sum_1 = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
for index in range(0, len(k) - 2):
    if (((k[index + 1] > 0) and (str(k[index + 1])[-1] == '9')) and (
            (k[index] < 0) or (str(k[index])[-1] != '9')) and (
            (k[index + 2] < 0) or (str(k[index + 2])[-1] != '9'))):
        count += 1
        sum_1.append(k[index] + k[index + 1] + k[index + 2])
print(count, max(sum_1))
