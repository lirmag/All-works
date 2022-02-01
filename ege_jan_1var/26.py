c = open('26.txt','r')
f = c.readlines()
k = []
for el in f:
    k.append(int(el))
k = k[1::]

c = k


for number in c:
    number = str(number)
    if int(number[len(number) - 1]) % 2 != 0 or int(number[len(number) - 1]) != 0:
        c.remove(int(number))

count = 0
max_sum = []
for index in range(0,len(k) - 1):
    sum_1 = (k[index] + k[index + 1]) // 2
    for elem in c:
        if sum_1 == elem:
            count += 1
            max_sum.append(sum_1)
print(count,max_sum)