k = []
for number in range(174457, 174506):
    for dig in range(2, number):
        if number % dig == 0:
            k.append(dig)
        if len(k) > 2:
            k = []
            break
    if len(k) == 2:
        print(number, k)
        k = []
