number = 3 * (4 ** 38) + 2 * (4** 23) + (4**20) + 3 * (4**5) + 2 * (4**4) + 1
ans = ''
while number > 0:
    ans = ans + str(number % 16)
    number //= 16
print(ans)
print(ans.count('0'))