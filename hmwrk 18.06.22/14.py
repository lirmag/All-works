def c(dig):
    ans = ''
    number = 31
    while number > 0:
        ans += str(number % dig)
        number //= dig
    return ans[0]


for dig in range(2,101):
    if c(dig) == '4':
        print(dig,end='')