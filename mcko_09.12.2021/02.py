for n in range(1,1001):
    num = bin(n)[2:]
    ans = ''
    if num.count('1') % 2 == 0:
        ans = num + '0'
    if num.count('1') % 2 != 0:
        ans = num + '1'
    if ans.count('1') % 2 == 0:
        ans = ans + '0'
    if ans.count('1') % 2 != 0:
        ans = ans + '1'
    ans = int(ans,base=2)
    if ans < 93:
        print(n)