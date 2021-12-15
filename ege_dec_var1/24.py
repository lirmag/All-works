# f = open('24.txt','r')
# lines = f.readlines()
# k = []
# for line in lines:
#     for el in line:
#         k.append(el)
# print(len(k))
# m = []
# count = 1
# for ind in range(0,len(k) - 1):
#     if (k[ind] != 'a' and k[ind + 1] != 'd') or (k[ind] != 'd' and k[ind + 1] != 'd'):
#         count += 1
#     else:
#         m.append(count)
#         count = 1
# print(max(m))
f = open('24.txt')
s = f.readline()
c = 1
m = 0
for i in range(1,len(s)):
    if s[i-1:i+1] not in ['da','ad']:
        c += 1
    else:
        c = 1
    m = max(m,c)
print(m)