with open('24.txt','r') as f:
    k = list(map(str,f.readline()))
a_count = 0
count = 0
sm = []
for elem in k:
    if (elem == 'E') and (a_count > 2):
        sm.append(count)
        count = 0
        a_count = 0
        continue
    if (elem == 'E') and (a_count < 3):
        count = 0
        a_count = 0
        continue
    if elem == 'A':
        a_count += 1
        count += 1
    else:
        count += 1
print(max(sm))

