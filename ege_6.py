# k = (True,False)
# print('x y z f')
# for x in k:
#     for y in k:
#         for z in k:
#             f = (not y) or (x and (not z))
#             if f is True:
#                 print(int(x), int(y), int(z), int(f))

# sum_1 = 0
# sum_2 = 0
# for number in range(1,101):
#     l = number
#     number = int(bin(number)[2:])
#     c = number
#     while int(c) > 0:
#         count = int(c) % 10
#         sum_1 += int(count)
#         c = int(c) // 10
#     new_number = str(number) + str(sum_1 % 2)
#     p = int(new_number)
#     while int(p) > 0:
#         k = int(p) % 10
#         sum_2 += int(k)
#         p = int(p) // 10
#     answer = str(new_number) + str(sum_2 % 2)
#     answer = int(answer, base=2)
#     if int(answer) >= 43:
#         print(l)

# def f(number):
#     s = number
#     n = 1
#     while n <= 100:
#         s = s + 30
#         n = n * 3
#     return s
# print(f(0))

x = 0
y = 0
for n in range(1,101):
    for a in range(-100,101):
        for b in range(-100,101):
            x = x + 30
            y = y + 30
            while n != 0:
                x = x + a
                y = y + b
                x = x + 15
                y = y - 9
                n = n - 1
            x = x + 2
            y = y - 10
    if (x == 0) and (y == 0):
        print(n)
