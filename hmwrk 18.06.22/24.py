with open('24 (1).txt','r') as f:
    k = list(map(str,f.readline()))
count = 0
e_c = 0
sm = []
for elem in k:
    if elem == 'E':
        e_c += 1
        count += 1
    elif (elem == 'A') and (e_c >= 3):
        sm.append(count)
        count = 0
        e_c = 0
    elif (elem == 'A') and (e_c < 3):
        count = 0
        e_c = 0
    else:
        count += 1
print(max(sm))
