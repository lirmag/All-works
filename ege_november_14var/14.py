for dig in range(2,37):
    if 93 % dig == 2:
        print(dig)
a = 13
number = 93
answer = ''
while number > 0:
    answer = answer + str(number % a)
    number //= 13
print(answer)
a = 7
number = 93
answer = ''
while number > 0:
    answer = answer + str(number % a)
    number //= 7
print(answer)