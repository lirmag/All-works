# print(bin(0)[2:])
# print(bin(1)[2:])
# print(bin(2)[2:])
# print(bin(3)[2:])
# print(bin(4)[2:])
# print(int('011110111001100',base=2))
number = 15820
ans = ''
while number > 0:
    ans = ans + str(number % 8)
    number //= 8
print(ans[::-1])