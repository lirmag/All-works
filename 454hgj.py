k = []
def func_1(number):
    s = number
    n = 11
    while s < 224:
        s = s + 15
        n = n + 8
    return(n)
for i in range(1,1000):
    if func_1(i) == 115:
        k.append(i)
print(min(k))