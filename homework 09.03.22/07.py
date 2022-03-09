for number in range(4234679,10157812):
    k = []
    for dig in range(2,number):
        if len(k) > 3:
            break
        if number % dig == 0:
            k.append(dig)
    if len(k) == 3:
        print(number,max(k))
