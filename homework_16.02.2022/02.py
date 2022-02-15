count = 0
for number in range(800001,10000000001):
    if count == 5:
        break
    k = []
    for dig in range(2,number):
        if number % dig == 0:
            k.append(dig)
    if (len(k) != 0) and ((max(k) + min(k)) % 138 == 0):
        count += 1
        print(number,(max(k) + min(k)))