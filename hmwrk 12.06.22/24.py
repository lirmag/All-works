with open('zadanie24_1.txt', 'r') as f:
    k = list(map(str, f.readline()))

count = 0
sm = []
for index in range(0,len(k)):
    if (index == len(k) - 1) and (k[index] == 'B'):
        count += 1
        sm.append(count)
    if (index == len(k) - 1) and (k[index] != 'B'):
        sm.append(count)
    if k[index] == 'B':
        count += 1
    else:
        sm.append(count)
        count = 0
print(max(sm))
