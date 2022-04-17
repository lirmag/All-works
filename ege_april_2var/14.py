def counting(dig,num=225):
    ans = ''
    while num > 0:
        ans += str(num % dig)
        num //= dig
    return ans[::-1]


for digit in range(2,101):
    if counting(225) == '405':
        print(digit)
        break