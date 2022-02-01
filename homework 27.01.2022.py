number = 7**1003 + 6 * 7**1104 - 3 * 7**57 + 293
ans = ''
while number > 0:
    ans = ans + str(number % 7)
    number//= 7
sum_1 = 0
for elem in ans:
    elem = int(elem)
    sum_1 += elem
print(ans)
print(sum_1)