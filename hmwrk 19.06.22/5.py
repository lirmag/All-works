def f(n):
    ans = 0
    for elem in n:
        elem = int(elem)
        ans += elem
    return ans % 2


for number in range(1,1001):
    n = bin(number)[2::]
    n += str(f(n))
    n += str(f(n))
    if int(n,base=2) > 43:
        print(number,int(n,base=2))
        break