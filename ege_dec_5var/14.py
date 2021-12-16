number = (9**8) + (3**5) - 9
ans = ''
while number > 0:
    ans = ans + str(number % 3)
    number //= 3
ans = ans[::-1]
print(ans)
print(ans.count('2'))