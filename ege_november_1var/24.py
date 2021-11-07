f = open('inf_22_10_20_24.txt','r')
A_count = 0
E_count = 0
count = 0
lines = f.readlines()
for line in lines:
    for element in line:
        if element == 'A':
            A_count += 1
        if element == 'E':
            E_count += 1
    if E_count > A_count:
        count += 1
    A_count = 0
    E_count = 0
    continue
f.close()
print(count)