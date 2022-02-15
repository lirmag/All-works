c = open('09', 'r')
lines = c.readlines()
k = []
count = 0
sum_3 = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
for index in k:
    sum_1 = 0
    for elem in str(index):
        sum_1 += int(elem)
    if sum_1 % 3 == 0:
        count += 1
        sum_3.append(index)
print(count, max(sum_3))
