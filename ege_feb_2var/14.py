def f_6(N):
    ans = ''
    while N > 0:
        ans = ans + str(N % 6)
        N //= 6
    return len(ans)
def f_5(N):
    ans = ''
    while N > 0:
        ans = ans + str(N % 5)
        N //= 5
    return len(ans)
def f_11(N):
    ans = ''
    while N > 0:
        ans = ans + str(N % 11)
        N //= 11
    return ans[0]



for N in range(1,10001):
    if (f_6(N) == 2) and (f_5(N) == 3) and (f_11(N) == '1'):
        print(N)
        break