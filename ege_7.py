# k = (True,False)
# print('x y z f')
# for x in k:
#     for y in k:
#         for z in k:
#             f = (x == y) or ((y or z) >= x)
#             if f is False:
#                 print(int(x), int(y), int(z), int(f))

# print(bin(0))
# print(bin(1))
# print(bin(2))
# print(bin(3))
# print(bin(4))

# number = str(1110100000110010)
# answer = int(number,base=2)
# print(answer)
# count = ''
# while answer > 0:
#     count = count + str(answer % 16)
#     answer //= 16
# print(count)
# 59442
# print(59442 % 16)
# print(3715 % 16)
# print(232 % 16)
# print(232 // 16)

# sum_1 = 0
# sum_2 = 0
# for number in range(1000,9999):
#     number = str(number)
#     if (int(number[0]) % 2 != 0) and (int(number[1]) % 2 != 0) and (int(number[2]) % 2 != 0) and (int(number[3]) % 2 != 0):
#         sum_1 = int(number[0]) + int(number[1])
#         sum_2 = int(number[2]) + int(number[3])
#         if (int(str(sum_1) + str(sum_2)) == 414) or (int(str(sum_2) + str(sum_1)) == 414):
#             print(number)

# def f(number):
#     s = number
#     n = 3
#     while n <= 7:
#         s += n
#         n += 1
#     return s
# print(f(0))

# print(6 * 60 * 60)
# # print(4 * 60 * 60)
# # print(21600 * 512)
# # print(256 * 14400)
# # print(3686400 + 11059200)
# # print(14745600 // 8)
# # print(1843200 // 1024)

# for count in range(1,12):
#     number = 144
#     if number % count == 1:
#         print(count)

# k = []
# for A in range(1,1001):
#     flag = True
#     for x in range(1,1001):
#         for y in range(1,1001):
#             if ((y + 2*x != 48) or (A < x) or (A < y)) is False:
#                 flag = False
#                 break
#         if flag == False:
#             break
#     if flag == True:
#         print(A)

# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return f(n - 1) + n
# print(f(30))
