f = open('17 (1).txt','r')
k = []
answer = []
count = 0
s = 0
for element in f:
    k.append(element)
for index in range(len(k) - 1):
    if '\n' in k[index]:
        k[index] = k[index].replace('\n', '',1)
for i in range(len(k) - 1):
    number = k[i]
    s += 1
    for l in range(s,len(k)):
        number_1 = k[l]
        if (int(number) * int(number_1)) % 10 == 0:
            count += 1
            sum_1 = int(number) + int(number_1)
            answer.append(sum_1)
print(count)
print(max(answer))