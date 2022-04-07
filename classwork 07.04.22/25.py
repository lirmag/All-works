for m in range(0,31,2):
    for n in range(1,20,2):
        num = 2**m * 3**n
        if (num > 150000000) and (num < 300000000):
            print(num,m+n)