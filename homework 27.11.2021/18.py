for dig in range(2,1001):
    number = 27
    ans = ''
    while number > 0:
        ans = ans + str(number % dig)
        number //= dig
    if ans == '30' or ans == '03':
        print(dig)