number = str(2 * 216**6  + 3 * 36**9 - 432)
ans = ''
while number > 0:
    ans = ans + str(number % 6)
    number //= 6
print(ans.count('5'))