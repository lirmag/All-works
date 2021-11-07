# k = (True,False)
# print('x y z F')
# for x in k:
#     for y in k:
#         for z in k:
#             F = (x == z) or (x >= (y and z))
#             if F is False:
#                 print(int(x),int(y),int(z),int(F))
#             # (x ≡ z) ∨ (x → (y ∧ z)).

# k = []
# def f(x):
#     number = bin(x)
#     number = str(number)[2:]
#     number = number[1:]
#     if number.count("0") == len(number):
#         return x - 0
#     while number[0] == '0':
#         number = number[1:]
#     return x - int(number, base=2)
# for x in range(100,3001):
#     k.append(f(x))
# print(len(set(k)))
#
# def f(s):
#     k = 0
#     while k < 30:
#         k += 3
#         s += k
#     return s
# print(f(47))

# number = str(1) * 77
# while '11' in number:
#     if '222' in number:
#         number = number.replace('222', '1',1)
#     else:
#         number = number.replace('11', '2',1)
# print(number)
# answer = ''
# for number in range(1,11):
#     while number > 0:
#         answer = str(number % 8) + answer
#         number //= 8
#     answer = answer + '00'
#     c = int(answer,base=8)
#     print(c)
# def f(n):
#     if n > 0:
#         f(n -3)
#         f(n // 3)
#         print(n)
# print(f(9))
# def f(number):
#     x = number
#     L = 1
#     M = 0
#     while number > 0:
#         M = M + 1
#         if number % 2 != 0:
#             L = L * (number % 8)
#         number = number // 8
#     return L, M
# for number in range(1,10001):
#     if f(number) == (21,3):
#         print(number)
k = []
def f(number, count):
    if count == 3:
        k.append(number)
        return
    elif count > 3:
        return
    else:
        return f(number + 2, count + 1) or f(number * 3, count + 1)
f(2,0)
print(len(set(k)))