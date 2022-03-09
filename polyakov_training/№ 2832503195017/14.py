number = (64**25 + 4**10) - (16**20 + 32**3)
ans = ''
while number > 0:
    ans = ans + str(number % 4)
    number //= 4
print(ans)
