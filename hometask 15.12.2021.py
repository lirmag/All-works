num = input()
count = 0
ind = 1
flag = True
for x in num:
    if x != '.' or x == ',':
        ind += 1
    if x == '.' or x == ',':
        for el in range(ind,ind + 6):
            count += 1
            if int(num[el]) == 0:
                flag = True
                continue
            else:
                flag = False
                print('No')
                break
if flag == True:
    print('Yes')
