number = 9**11 * 3**20 - 3**9 - 27
ans = ''
while number > 0:
    ans = ans + str(number % 3)
    number //= 3
print(ans.count('2'))