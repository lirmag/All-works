c = open('17-202.txt', 'r')
k = list(map(int, c.readlines()))
count = 0
sum_1 = []
for index in range(0, len(k) - 2):
    if (k[index + 1] > 0) and (len(str(k[index + 1])) == 3) and (k[index + 1] % 100 == 12) and (
            (k[index] < 0) or (len(str(k[index])) != 3) or (k[index] % 100 != 12) or (k[index + 2] % 100 != 12) or (
            k[index + 2] < 0) or (len(str(k[index + 2] != 3)))):
        count += 1
        sum_1.append(k[index] + k[index + 1] + k[index + 2])
print(count,max(sum_1))
# a = '1234'
# print(a[len(a) - 2: len(a)])
# (str(k[index + 1])[len(str(k[index + 1])) - 2:len(str(k[index + 1]))] == '12')