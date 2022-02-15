k = []
stop = []
for number in range(452022, 100000000):
    k = []
    if len(stop) == 5:
        break
    for dig in range(2, number):
        if number % dig == 0:
            k.append(dig)
    if len(k) == 0:
        M = 0
    else:
        M = max(k) + min(k)
    if M % 7 == 3:
        print(number, M)
        stop.append(number)
        k = []
