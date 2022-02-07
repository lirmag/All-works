# for dig in range(2, 37):
#     ans = ''
#     number = 50
#     while number > 0:
#         ans = ans + str(number % dig)
#         number //= dig
#
#     if len(ans) == 3:
#         print(dig)
#         break

# count = 0
# for number in range(1073741825,4290000000,10):
#     count += 1
# print(count)
print(len(hex(7000000000)[2:]))
# for number in range(9999999990,2,-1):
#     if len(hex(number)[2:]) <= 8:
#         print(number)
#         break