f = open('inf_22_10_20_24 (2).txt','r')
lines = f.readlines()
count = 0
for line in lines:
    E_count = 0
    A_count = 0
    for elem in line:
        if elem == 'A':
            A_count += 1
        if elem == 'E':
            E_count += 1
    if A_count > E_count:
        count += 1
print(count)

