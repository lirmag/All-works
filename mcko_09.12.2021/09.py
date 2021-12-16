number = str(2) * 105
while ('222' in number) or ('555' in number):
    if '555' in number:
        number = number.replace('555', '2', 1)
    else:
        number = number.replace('2222', '5', 1)
print(number)
