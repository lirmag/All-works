for dig in range(2,37):
    x = 0
    ans = ''
    number = 69
    if number % dig == 1:
        x = dig
        while number > 0:
            ans = ans + str(number % x)
            number //= x
        if len(ans) == 4:
            print(dig)
            break
        else:
            ans = ''
            number = 69
            x = 0