length = int(input())
t = tuple()
for a in range(1,length + 1):
    num = int(input())
    num = tuple(str(num))
    t += num
print(t)
maximum = 0
minimum = 0
for ind in range(0,len(t) - 1):
    if t[ind] == '-':
        a = '-' + t[ind + 1]
        if ind == 0:
            minimum = int(a)
            maximum = int(a)
        if int(a) > maximum:
            maximum = int(a)
        if int(a) < minimum:
            minimum = int(a)
        continue
    if ind == 0:
        minimum = int(t[ind])
        maximum = int(t[ind])
    if int(t[ind]) > maximum:
        maximum = int(t[ind])
    if int(t[ind]) < minimum:
        minimum = int(t[ind])
count = 0
if str(maximum) in t:
    for elem in t:
        if elem == str(maximum):
            print(count)
        else:
            count += 1
index = 0
if str(minimum) in t:
    for el in t:
        if el == str(minimum):
            print(index)
        else:
            index += 1
