def f(n,m):
    if n % m == 0:
        return 1
    else:
        return 0
for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        if (f(A,34) and (f(283,x) <= (not(f(A,x) <= (not(f(120,x))))))) is False:
            flag = False
            break
        if flag == False:
            break
    if flag == True:
        print(A)
        break
