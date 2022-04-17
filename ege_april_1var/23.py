res = set()
def f(x,k):
    global res
    if k == 7:
        return res.add(x)
    else:
        f(x + 4,k + 1)
        f(x - 3,k + 1)


f(1,0)
print(len(res))