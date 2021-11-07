number = 3 * (216 ** 4) + 2 * (36**6) - 648
answer = ''
while number > 0:
    answer = answer + str(number % 6)
    number //= 6
print(answer)