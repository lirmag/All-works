# def dig(number):
#     for i in range(1,21):
#         if (number % i) != 0:
#             return False
#     return True
#
#
# for number in range(2520,1000000001):
#     if dig(number):
#         print(number)
#         break


k = list(range(1,21,1))
for number in range(2520,1000000001):
    if all(number % dig == 0 for dig in k):
        print(number)
        break