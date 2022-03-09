for dig in range(2,101):
    number = 87
    ans = ''
    while number > 0:
        ans = ans + str(number % dig)
        number //= dig
    if (len(ans) <= 2) and (ans[0] == '2'):
        print(dig)