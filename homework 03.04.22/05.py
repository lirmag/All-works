string = str(1) * 81
while '1111' in string or '88888' in string:
    if '1111' in string:
        string = string.replace('1111','888',1)
    else:
        string = string.replace('88888','888',1)
print(string)