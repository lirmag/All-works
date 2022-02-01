string = '1' * 84
while '11111' in string:
    string = string.replace('222','1',1)
    string = string.replace('111','2',1)
print(string)