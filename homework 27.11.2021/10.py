number = (36 ** 8) + (6 ** 20) - 12
ans = ''
while number > 0:
    ans = ans + str(number % 6)
    number //= 6
print(ans)
print(ans.count('5'))
