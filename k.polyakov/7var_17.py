c = open('07', 'r')
lines = c.readlines()
k = []
count = 0
sum_3 = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
for index in range(0, len(k) - 1):
    ans = ''
    sum_1 = k[index] + k[index + 1]
    while sum_1 > 0:
        ans = ans + str(sum_1 % 7)
        sum_1 //= 7
    if ans == ans[::-1]:
        count += 1
        sum_3.append(int(ans))
print(count,max(sum_3))
