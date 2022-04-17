def f(number):
    ans = ''
    while number > 0:
        ans += str(number % 3)
        number //= 3
    return ans[::-1]


for num in range(0,18):
    if (len(f(num)) >= 2) and (f(num)[-1] == f(num)[-2]):
        print(num)