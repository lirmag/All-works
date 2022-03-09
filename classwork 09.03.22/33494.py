# with open('24.txt', 'r') as f:
#     c = f.readline()
#     l = []
#     for index in range(0, len(c) - 1):
#         if c[index] == 'E' and c[index + 1] != 'E':
#             for ind in range(0, len(l)):
#                 if c[index] in l[ind]:
#                     l[ind][1] += 1
#                 else:
#                     l.append((c[index + 1], 1))
# print(l)
c = 'EAEA'
l = [('0',0)]
for index in range(0, len(c) - 1):
    if c[index] == 'E' and c[index + 1] != 'E':
        for ind in range(0, len(l)):
            if c[index + 1] in l[ind]:
                l[ind][1] += 1
                break
            else:
                l.append((c[index + 1], 1))
                break
print(l)
