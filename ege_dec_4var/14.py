for number in range(1,31):
    ans = ''
    n = number
    while n > 0:
        ans = ans + str(n % 5)
        n //= 5
    ans = ans[::-1]
    if ans[0] == '3':
        print(number)