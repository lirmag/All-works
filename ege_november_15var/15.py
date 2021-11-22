def f(x,y):
    if x % y == 0:
        return 1
for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        if ((f(120,A)) and ((not(f(x,A))) <= (f(x,18)) <= (not(f(x,24))))) is False:
            flag = False
            break
    if flag == True:
        print(A)

