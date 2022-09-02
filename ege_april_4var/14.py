def d(num):
    ans = ''
    while num > 0:
        ans += str(num % 5)
        num //= 5
    return ans[::-1]


for number in range(1,31):
    if d(number)[0] == '3':
        print(number)