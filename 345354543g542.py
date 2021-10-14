k = []
def func_1(number):
    s = number
    n = 1
    while s < 28:
        s = s + 5
        n = n * 3
    return(n)
for i in range(1,10000):
    if func_1(i) == 81:
        k.append(i)
print(min(k))