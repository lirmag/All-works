res = set()
def f(x,k):
    global res
    if k == 10:
        res.add(x)
    else:
        f(x + 2, k + 1)
        f(x + 3, k + 1)
f(2,0)
print(res)
print(len(res))