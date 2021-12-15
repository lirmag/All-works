for x in range(1,18):
    num = x
    ans = ''
    while num > 0:
        ans = ans + str(num % 3)
        num //= 3
    ans = ans[::-1]
    if len(ans) > 1 and (ans[len(ans) - 2] == ans[len(ans) - 1]):
        print(x,ans)