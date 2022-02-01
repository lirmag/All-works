number = 125 + 25**3 + 5**9
ans = ''
while number > 0:
    ans = ans + str(number % 5)
    number //= 5
ans = ans[::-1]
print(ans)
