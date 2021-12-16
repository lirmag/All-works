number = (64**9) + (8**25) - 9
ans = ''
while number > 0:
    ans = ans + str(number % 8)
    number //= 8
ans = ans[::-1]
print(ans.count('7'))