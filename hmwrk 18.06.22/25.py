def f(number):
    k = []
    i = 2
    while i ** 2 < number:
        if number % i == 0:
            k.append(i)
            k.append(number // i)
        i += 1
        if i ** 2 == number:
            k.append(i)
    return k



for number in range(174457,174506):
    if len(f(number)) == 2:
        print(number,f(number))