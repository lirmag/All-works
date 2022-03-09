sum_1 = 0
string = '32323232323232323232323232424242424244444'
string = '323232323232323232323232323232424242424244444'
while ('42' in string) or ('32' in string):
    if '42' in string:
        string = string.replace('42','51',1)
    else:
        string = string.replace('32','61',1)
for elem in string:
    elem = int(elem)
    sum_1 += elem
print(sum_1)