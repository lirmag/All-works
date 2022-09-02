def dig(number):
    i = 2
    k = []
    while i ** 2 < number:
        if number % i == 0:
            k.append(i)
            k.append(number // i)
        i += 1
    try:
        return min(k) + max(k)
    except:
        return 0


count = 0
for number in range(452022,1000000000000000):
    if count == 5:
        break
    if dig(number) % 7 == 3:
        print(number,dig(number))
        count += 1

