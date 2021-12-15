number = (729**6) - (3 ** 20) + 90
ans = ''
while number > 0:
    ans = ans + str(number % 9)
    number //= 9
print(ans)
print(ans.count('0'))