def cnt(dig):
    ans = ''
    a = 338
    while a > 0:
        ans += str(a % dig)
        a //= dig
    return ans[::-1]


for dig in range(2,19):
    if (len(cnt(dig)) == 3) and (cnt(dig)[-1] == '2'):
        print(dig,cnt(dig))