N = 43
number = N
num = N
ans = ''
number = hex(number)[2::]
if number[len(number) - 1] == 'b':
    while num > 0:
        ans = ans + str(num % 5)
        num //= 5
    ans = ans[::-1]
    if ans[len(ans) - 1] == '3':
        print(N)

# 43
# 91