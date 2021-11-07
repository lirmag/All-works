for i in range(200000000, 400000001):
    flag = False
    for m in range(2,31,2):
        for n in range(1,30,2):
            if i == ((2**m) * (3**n)):
                print(i)