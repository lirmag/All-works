string = str(1) * 99
while '11' in string:
    string = string.replace('11','2',1)
    string = string.replace('22','1',1)
print(string)