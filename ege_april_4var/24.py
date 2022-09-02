with open('24_demo (2).txt','r') as f:
    k = list(map(str,f.readline()))


count = 0
sm = []
for elem in k:
    if elem == 'Z':
        count += 1
    else:
        sm.append(count)
        count = 0
print(max(sm))