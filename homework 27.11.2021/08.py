for x in range(1,1001):
    number = (216 ** 5) + (6 ** 3) - 1 - x
    ans = ''
    while number > 0:
        ans = ans + str(number % 6)
        number //= 6
    if ans.count('5') == 12:
        print(x)
        break