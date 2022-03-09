c = open('24 (1).txt','r')
count = 0
E_count = 0
ans = []
k = []
lines = c.readlines()
for line in lines:
    for elem in line:
        k.append(elem)
for index in range(0,len(k)):
    if k[index] == 'E':
        E_count += 1
    if (k[index] == 'A') and (E_count >= 3):
        ans.append(count)
        count = 0
    elif (k[index] == 'A') and (E_count < 3):
        count = 0
    else:
        count += 1
        
print(max(ans))