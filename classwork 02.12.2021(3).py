# n = float(input())
# n = str(n)
# count = 0
# if len(n) < 8:
#     while len(n) != 8:
#         n = n + '0'
# if len(n) > 8:
#     n = n[0:8]
# print(n)
# for ind in range(2,8):
#     if int(n[ind]) % 2 != 0:
#         print('No')
#         break
#     else:
#         count += 1
# if count > 1:
#     print('Yes')
count = 1
n = input()
for el in n:
    if el == '.':
        n = n[count:count + 6]
    else:
        count += 1
k = 0
flag = True
for ind in range(0, 7):
    if int(n[ind]) % 2 != 0:
        print('No')
        flag = False
        break
    else:
        k += 1
if k > 1 and flag == True:
    print('Yes')
