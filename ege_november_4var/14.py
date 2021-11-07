number = (36**7) + (6**19) - 18
print(number)
answer = ''
while number > 0:
    answer = answer + str(number % 6)
    number //= 6
print(answer)