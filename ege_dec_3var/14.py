for dig in range(16,3,-1):
    number = 338
    ans = ''
    while number > 0:
        ans = ans + str(number % dig)
        number //= dig
    ans = ans[::-1]
    if len(ans) == 3 and ans[len(ans) - 1] == '2':
        print(dig)
