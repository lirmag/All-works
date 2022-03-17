count = 0
for number in range(520001,10000000000):
    if count == 5:
        break
    k = []
    for dig in range(2,number):
        if number % dig == 0:
            k.append(dig)
    if (len(k) != 0) and (str(sum(k)) == str(sum(k))[::-1]):
        print(number,max(k))
        count += 1