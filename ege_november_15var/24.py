f = open('24 (6).txt','r')
lines = f.readlines()
ans = []
for line in lines:
    count = 0
    for ind in range(0,len(line) - 1):
        if (line[ind] == 'K') and (line[ind + 1] == 'L'):
            ans.append(count)
            break
        else:
            count += 1
print(max(ans))