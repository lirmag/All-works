with open('inf_22_10_20_24.txt') as f:
    count = 0
    for line in f.readlines():
        E_c = 0
        A_c = 0
        for index in range(0,len(line) - 1):
            if line[index] == 'E':
                E_c += 1
            if line[index] == 'A':
                A_c += 1
        if E_c > A_c:
            count += 1
print(count)