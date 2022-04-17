def dl(a,b):
    if a % b == 0:
        return True
    else:
        return False


for A in range(1,1001):
    flag = True
    for x in range(1,1001):
        if ((dl(x,A) is False) <= (dl(x,6) <= (dl(x,4) is False))) is False:
            flag = False
            break
    if flag is True:
        print(A)