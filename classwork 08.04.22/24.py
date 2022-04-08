with open('24_demo (3).txt','r') as f:
    k = list(map(str,f.readline().strip()))
count = 1
ans = []
ind = 0
while ind != len(k) - 2:
    if (k[ind] > k[ind + 1]) and (k[ind + 1] > k[ind + 2]):
        ind += 3
        count += 3
        if k[ind] == 'X':
            ind += 1
            count += 1
        elif k[ind] + k[ind + 1] == 'XY':
            ind += 2
            count += 2
    else:
        ans.append(count)
        ind += 1
        count = 1
print(max(ans))

