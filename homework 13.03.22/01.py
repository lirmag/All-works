for number in range(489421,489441):
    k = []
    for dig in range(1,number + 1):
        if number % dig == 0:
            k.append(dig)
    if len(k) == 4:
        # k.append(number)
        # k.append(1)
        print(*sorted(k))