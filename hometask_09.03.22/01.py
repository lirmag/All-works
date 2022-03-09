for m in range(0,30,2):
    for n in range(1,25,2):
        number = 2**m * 3**n
        if (number >= 200000000) and (number <= 400000000):
            print(number)