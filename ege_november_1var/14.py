print(((2 * (216**6))+ (3 * (36**9))) - 432)
number = 507799783341648
answer = ''
while number > 0:
    answer = answer + str(number % 6)
    number //= 6
print(answer)