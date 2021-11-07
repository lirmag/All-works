number = 357
a = ''
while number > 0:
    a = a + str(number % 7)
    number //= 7
print(a[::-1])
print(len(a))