ls = ['1', '2', '3', '4']
for ind in range(len(ls) - 1, -1, -1):
    ls.append(ls[ind])
    ls.remove(ls[ind])
print(ls)
# l = [1, 2, 3, 4]
# print(l[::-1])
