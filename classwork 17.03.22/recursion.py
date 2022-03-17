def f(a,n):
    if n == 0:
        return a
    else:
        return f(a + 1,n - 1)
print(f(200,500))