inp = input()
k = list(map(int,inp.split(' ')))
ans = []
a = k[0]
b = k[1]
while a != b + 1:
    ans.append(a)
    a += 1
sum_1 = 0
for elem in ans:
    sum_1 += elem ** 2
print(sum_1)