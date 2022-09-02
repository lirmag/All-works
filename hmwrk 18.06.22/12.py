string = 77 * '1'
while '11' in string:
    if '222' in string:
        string = string.replace('222','1',1)
    else:
        string = string.replace('11','2',1)
print(string)