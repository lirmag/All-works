sum_1 = 0
for number in range(19,34):
    ans = ''
    while number > 0:
        ans = ans + str(number % 6)
        number //= 6
    sum_1 += ans.count('3')
    ans = ''
print(sum_1)