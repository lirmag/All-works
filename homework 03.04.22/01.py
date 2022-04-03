def f(string):
    while '111' in string or '222' in string:
        string = string.replace('111','22',1)
        string = string.replace('222','1',1)
    return string


for number in range(200,100001):
    string = str(1) * number
    if '1' not in f(string):
        print(f(string),number)
        break

