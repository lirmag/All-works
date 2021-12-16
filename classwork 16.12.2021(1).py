length = int(input())
maximum = 0
minimum = 0
# all = ''
index = 1
count = 1
res = set()
for k in range(1,length + 1):
    num = int(input())
    res.add(num)
    # a = str(num)
    # all += a + ' '
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
for elem in res:
    if elem == minimum:
        a = index
    else:
        index += 1
for ind in res:
    if ind == maximum:
        b = count
    else:
        count += 1

print(minimum,maximum)
print(a,b)
# print(all)
# for index in range(0,len(all) - 1):
#     if all[index] == str(minimum):
#         print(index)
#     if all[index] == str(maximum):
#         print(index)