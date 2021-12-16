number = (49**10) + (7**30) - 49
ans = ''
while number > 0:
    ans = ans + str(number % 7)
    number //= 7
ans = ans[::-1]
print(ans.count('6'))