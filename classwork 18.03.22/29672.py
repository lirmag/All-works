with open('inf_22_10_20_24.txt','r') as f:
    k = []
    for line in f.readlines():
        k.append(line)
count = 0
for line in k:
    E_count = 0
    A_count = 0
    for el in line:
        if el == 'A':
            A_count += 1
        if el == 'E':
            E_count += 1
    if E_count > A_count:
        count += 1
print(count)