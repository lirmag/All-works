print((36 ** 7) + (6 ** 19) - 18)
number = 609438104174574
answer = ''
while number > 0:
    answer = answer + str(number % 6)
    number //= 6
print(answer)