string = str(1) * 101
while '1111' in string:
    string = string.replace('1111','22',1)
    string = string.replace('222','1',1)
    print(string)