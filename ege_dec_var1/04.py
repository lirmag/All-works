number = int('010010001110010',base=2)
print(number)
ans = ''
while number > 0:
    ans = ans + str(number % 8)
    number //= 8
print(ans[::-1])