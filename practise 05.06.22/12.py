string = '9' * 1000
while '999' in string or '888' in string:
    if '888' in string:
        string = string.replace('888','9',1)
    else:
        string = string.replace('999','8',1)
print(string)