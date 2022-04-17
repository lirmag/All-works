with open('24 (4).txt','r') as f:
    k = list(map(str,f.readline()))
dc = 0
count = 1
sm = []
for ind in range(0,len(k)):
    if k[ind] == 'D' and dc == 0:
        count += 1
        dc += 1
    elif k[ind] == 'D' and dc == 1:
        sm.append(count)
        count = 0
        dc = 0
    else:
        count += 1
print(max(sm))