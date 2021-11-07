# k = (True,False)
# print('x y z f')
# for x in k:
#     for y in k:
#         for z in k:
#             f = (x >= y) and (y >= z)
#             if f is True:
#                 print(int(x), int(y), int(z), int(f))

# def f(number):
#     s = number
#     n = 4
#     while n <= 8:
#         s +=n
#         n += 1
#     return s
# print(f(0))

# print(1024 * 1024)
# print(512 * 1024 * 8)
# print()

# number = '1' + (str(8) * 80)
# while '18' in number or '288' in number or '3888' in number:
#     if '18' in number:
#         number = number.replace('18', '2', 1)
#     else:
#         if '288' in number:
#             number = number.replace('288','3',1)
#         else:
#             number = number.replace('3888','1',1)
# print(number)
# for count in range(2,101):
#     number = 31
#     answer = ''
#     while number > 0:
#         c = number % count
#         answer = answer + str(c)
#         number //= count
#     print(answer)

for A in range(1,1001):
    for x in range(1,1001):
        for y in range(1,1001):
            if not ((x < A)>= (x**2 < 81)) and ((y**2 <= 36) >= (y <= A)) is False:
                print(A)

# def f(n):
#     if n > 0:
#         f(n -3)
#         print(n)
#         f(n//3)
# print(f(9))

# def f(n):
#     x = n
#     L = 0
#     M = 0
#     while x > 0:
#         M =+ 1
#         if (x % 2) != 0:
#             L = L + x % 8
#         x = x // 8
#     return L,M
# for n in range(10000000,100000001):
#     if f(n) == (14,3):
#         print(n)
k = []
def f(number):
    if number == 9:
        return number
    elif number > 9:
        return
    else:
        print(f(number + 1)) or print(f(number + 3))
        return f(number + 1) or f(number + 3)
print(f(1))