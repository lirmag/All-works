sum_1 = 0
for x in range(1,1000):
    if (x % 3 == 0) or (x % 5 == 0):
        sum_1 += x
print(sum_1)