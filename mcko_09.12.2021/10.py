number = (216**8) + (36**23) - 9
ans = ''
while number > 0:
    ans = ans + str(number % 6)
    number //= 6
ans = ans[::-1]
print(ans)
print(ans.count('5'))