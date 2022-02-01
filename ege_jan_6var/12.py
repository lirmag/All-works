string = '1' * 99
while '111' in string:
    if '222' in string:
        string = string.replace('222','1',1)
    else:
        string = string.replace('111','2',1)
print(string)