def divisors(integer):
    b = []
    for i in range(2,10000,1):
        if integer % i == 0:
            b.append(i)
            if integer // i == 1:
                b.remove(i)
    if len(b) == 0:
        return(str(integer) + "is prime")
    else:
        return(b)
divisors(13)