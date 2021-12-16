f = open('24 (1).txt','r')
s = f.read().split('D')
m = 0
print(s)
ans = []
for ind in range(0,len(s) - 1):
    if len(s[ind]) + len(s[ind + 1]) + 1 > m:
        m = len(s[ind]) + len(s[ind + 1]) + 1
print(m)
# lines = f.readlines()
# k = []
# for line in lines:
#     for elem in line:
#         k.append(elem)
# count = 0
# D_count = 0
# for el in k:
#     if D_count > 1:
#         ans.append(count)
#         count = 0
#         D_count = 0
#         continue
#     if el != 'D':
#         count += 1
#     if el == 'D':
#         count += 1
#         D_count += 1
# for ind in range(0,len(k) - 1):
#     if k[ind] != 'D':
#         count += 1
#     if k[ind] == 'D' and D_count <= 1:
#         count += 1
#         D_count += 1
#     if D_count > 1:
#         ans.append(count)
#         count = 0
#         D_count = 0
