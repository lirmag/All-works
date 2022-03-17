with open('17 (2).txt', 'r') as f:
    k = list(map(int, f.readlines()))
count = 0
sum_1 = []
for index in range(0, len(k) - 2):
    flag = ((k[index] ** 2 + k[index + 1] ** 2) > k[index + 2] ** 2) and (
            (k[index] ** 2 + k[index + 2] ** 2) > k[index + 1] ** 2) and (
            (k[index + 1] ** 2 + k[index + 2] ** 2) > k[index] ** 2)
    if flag:
        count += 1
        sum_1.append(k[index] + k[index + 1] + k[index + 2])
print(count, max(sum_1))
