string = '1'* 39 + '2'*39
while '111' in string:
    string = string.replace('111','2',1)
    string = string.replace('222','1',1)
print(string)