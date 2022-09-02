res = set()
def f(x,k):
    global res
    if k == 8:
        res.add(x)
    else:
        f(x * 8,k + 1)
        f(x // 2,k + 1)


f(512,0)
print(len(res))