number = str(1) * 40 + str(2) * 40
while '111' in number:
    number = number.replace('111','2',1)
    number = number.replace('222','1',1)
print(number)
