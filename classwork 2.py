number = int(input())
number = str(number)
sum_1 = 0
mult = 1
for i in range(0, len(number)):
    sum_1 += int(number[i])
    mult *= int(number[i])
print(sum_1, mult)
