number = 16**44 + 16**30 - (32**5 * (8**40 - 8**32) * (16**17 - 32**4))
number = hex(number)[2:]
print(number)
number = number.replace(number[1],'',1)
print(number)
for el in number:
    if el == 'e':
        number = number.replace('e','1',1)
print(number.count('1'))
