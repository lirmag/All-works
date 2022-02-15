count = 0
for number in range(520001, 1000001):
    if count == 5:
        break
    k = []
    for dig in range(2, number):
        if number % dig == 0:
            k.append(dig)
    if (str(sum(k)) == str(sum(k))[::-1]) and (len(k) != 0):
        count += 1
        print(number, max(k))
