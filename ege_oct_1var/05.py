number = 91
ans = ''
while number > 0:
    ans = ans + str(number % 2)
    number //= 2
ans = ans[::-1]
print(ans)

num = int('0100110',base=2)
print(num)