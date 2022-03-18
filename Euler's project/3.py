import math


def f(n):
    for d in range(2, number):
        if n % d == 0:
            return False
    return True


number = 600851475143
for dig in range(2,number):
    if dig <= round(number ** 0.5):
        if number % dig == 0:
            if f(dig) is True:
                print(dig)
                break



# def prime_number(number: int):
#     a = number
#     k = 0
#     for i in range(2, a // 2 + 1):
#         if (a % i == 0):
#             k = k + 1
#     if (k <= 0):
#         return True
#
#
# def high_prime_number_division(given_number: int):
#     list_num = []
#     for element in range(2, given_number):
#         if element <= round(given_number ** (0.5)):
#             if given_number % element == 0:
#                 if prime_number(element):
#                     list_num.append(element)
#         else:
#             return list_num[-1]
#
#
# print(high_prime_number_division(600851475143))