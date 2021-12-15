number = (36 ** 7) + (6**19) - 18
ans = ''
while number > 0:
    ans = ans + str(number % 6)
    number //= 6
print(ans)
print(ans.count('5'))