with open('26','r') as f:
    number = []
    count = []
    lines = f.readlines()
    for line in lines:
        ap = ''
        for el in line:
            if el != ' ':
                ap += el
            else:
                number.append(int(ap))
                break
    for line in lines:
        ap = ''
        for elem in line[::-1]:
            if elem != ' ':
                ap += elem
            else:
                count.append(int(ap[::-1]))
print(number)
print(count)
index = -1
ans = []
s = 0
for index in range(0,len(number) - 1):
    s += 1
    for ind in range(s,len(number) - 1):
        if number[index] == number[ind]:
            if (max(count[index],count[ind]) - min(count[index],count[ind])) == 2:
                ans.append(str(number[index]) + ' ' + str(max(count[index],count[ind]) - min(count[index],count[ind])))
for elem in ans
