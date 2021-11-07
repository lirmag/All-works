number = str(9) * 127
while '333' in number or '999' in number:
    if '333' in number:
        number = number.replace('333','9',1)
    else:
        number = number.replace('999','3',1)
print(number)