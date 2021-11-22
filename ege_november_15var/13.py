for dig in range(2,36):
    x = 23
    ans = ''
    while x > 0:
        ans = ans + str(x % dig)
        x //= dig
    if ans == '212':
        print(dig)