number = 16**44 * 16**30 - (32**5 * (8**40 - 8**32) * (16**17 - 32**4))
print(number)
number = hex(number)[2:]
for el in number:
    if el == 'f':
        number = number.replace('f','0',1)
print(number)
number = number[20:len(number) -1]
print(number)
print(number.count('0'))
