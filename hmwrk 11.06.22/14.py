def ctg(number,dig):
    ans = ''
    while number > 0:
        ans += str(number % dig)
        number //= dig
    return ans[0],len(ans)


for dig in range(2,10000):
    if (ctg(87,dig)[0] == '2') and (ctg(87,dig)[1] <= 2):
        print(dig)