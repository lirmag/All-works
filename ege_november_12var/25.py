answer = []
digs = []
for num in range(500000,1000000):
    for dig in range(18,(num // 2),10):
        if (num // dig == 0) and (str(dig)[len(str(dig)) - 1] == '8'):
            answer.append(num)
            digs.append(dig)
        if len(answer) == 5:
            print(answer,digs)
            break