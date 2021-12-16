number = '8' * 1000
while '999' in number or '888' in number:
    if '888' in number:
        number = number.replace('888','9',1)
    else:
        number = number.replace('999','8',1)
print(number)