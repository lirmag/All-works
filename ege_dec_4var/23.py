res = set()
def f(x,k):
    global res
    if k == 4:
        res.add(x)
    else:
        f(x + 1,k + 1)
        f(x + 2,k + 1)
f(2,0)
print(len(res))