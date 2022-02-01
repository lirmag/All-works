for dig in range(2,37):
    number = 50
    ans = ''
    while number > 0:
        ans = ans + str(number % dig)
        number //= dig
    if len(ans) == 3:
        print(dig)