def f(n,m):
    return n % m
for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        if ((not(f(x,A))) <= (f(x,6) <= (not(f(x,4))))) is False:
            flag = False
            break
        if flag == False:
            break
    if flag == True:
        print(A)
