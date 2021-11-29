number = (64**9) + (8**25) - 9
ans = ''
while number > 0:
    ans = ans + str(number % 8)
    number //= 8
print(ans)
print(ans.count('7'))
# 17