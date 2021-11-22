line = ['GKPJFDSGSDFKL']
ans = []
count = 0

if 'KL' in line:
    for ind in range(0, len(line) - 1):
        if (line[ind] + line[ind + 1] == 'KL'):
            ans.append(count)
            count = 0
            break
        else:
            count += 1
else:
    ans.append(len(line))
    count = 0
    # for ind in range(0,len(line) - 1):
    #     if (line[ind] + line[ind + 1] == 'KL'):
    #         ans.append(count)
    #         break
    #     else:
    #         count += 1
print(max(ans))