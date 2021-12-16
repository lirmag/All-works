number = str(3) * 250
while '3333' in number or '7777' in number:
    if '3333' in number:
        number = number.replace('3333','7',1)
    else:
        number = number.replace('777','3',1)
print(number)