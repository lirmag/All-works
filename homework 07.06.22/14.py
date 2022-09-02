def f(number,c):
    ans = ''
    while number > 0:
        ans += str(number % c)
        number //= c
    return ans


for number in range(1,1001):
    if (len(f(number,6)) == 2) and (len(f(number,5)) == 3) and (f(number,11)[0] == '1'):
        print(number)