number = 86
ans = ''
while number > 0:
    ans = ans + str(number % 5)
    number //= 5
print(ans)