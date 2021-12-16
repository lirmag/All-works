number = (9**8) + (3**8) - 2
ans = ''
while number > 0:
    ans = ans + str(number % 3)
    number //= 3
print(ans.count('2'))