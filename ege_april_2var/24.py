with open('zadanie24_1.txt','r') as f:
    k = list(map(str,f.readline()))[0:-1]
count = 0
mx = []
for ind in range(0,len(k)):
    if k[ind] == 'C':
        count += 1
    else:
        mx.append(count)
        count = 0
print(max(mx))
