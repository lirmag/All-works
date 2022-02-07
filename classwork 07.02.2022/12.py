string = '323232323232323232323232323232' + '2' * 5 + '4' * 10
while ('42' in string) or ('32' in string):
    if '42' in string:
        string = string.replace('42','51',1)
    else:
        string = string.replace('32','61',1)
sum_1 = 0
for el in string:
    el = int(el)
    sum_1 += el
print(sum_1)