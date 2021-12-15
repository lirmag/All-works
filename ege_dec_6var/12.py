number = (str(5) * 54) + str(7)
while '722' in number or '557' in number:
    if '722' in number:
        number = number.replace('722','57',1)
    else:
        number = number.replace('557','72',1)
print(number)