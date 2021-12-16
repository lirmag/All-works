def delenie(number,dig):
    ans = ''
    while number > 0:
        ans = ans + str(number % dig)
        number //= dig
    return len(ans)
for dig in range(2,37):
    if 87 % dig == 2 and delenie(87,dig) >= 3:
        print(dig)