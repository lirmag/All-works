k = []
def f(x,y):
    if y == 3:
        k.append(x)
        return
    elif y > 3:
        return
    else:
        return f(x * 2,y + 1) or f(x * 3, y + 1)
f(2,0)
print(len(set(k)))