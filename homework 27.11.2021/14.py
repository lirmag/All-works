def delenie(number,dig):
    ans = ''
    while number > 0:
        ans = ans + str(number % dig)
        number //= dig
    return len(ans)
for number in range(2,1001):
    if (number % 11 == 2) and (delenie(number,6) == 3) and (delenie(number,7) == 2):
        print(number)
        break
