number = 49**7 + 7**20 - 28
ans = ''
while number > 0:
    ans = ans + str(number % 7)
    number //= 7
print(ans.count('6'))