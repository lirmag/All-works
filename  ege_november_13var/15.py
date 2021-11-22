def f(x,y):
    x = bin(x)[2:]
    y = bin(y)[2:]
    answer = ''
    if len(x) > len(y):
        while len(y) != len(x):
            y = '0' + str(y)
    if len(x) < len(y):
        while len(x) != len(y):
            x = '0' + str(x)
    for i in range(0,len(x)):
        answer += str(int(x[i]) * int(y[i]))
    return int(answer,base=2)
for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        if (((f(x,28) != 0) or (f(x,45) != 0)) <= ((f(x,17) == 0) <= (f(x,A) != 0))) is False:
            flag = False
            break
        if flag == False:
            break
    if flag == True:
        print(A)
        break
# print(f(14,5))