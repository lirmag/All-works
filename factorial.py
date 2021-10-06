
def factorial_1(number):
    f = 1
    while number != 1:
        f *= number
        number -= 1
    return f
number = int(input())
sum = 0
for i in range(1,number+1):
    sum += factorial_1(i)
print(sum)