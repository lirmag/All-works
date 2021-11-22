s = (str(2) * 20) + (str(3) * 15) + (str(4) * 10)
while ('42' in s) or ('32' in s):
    if '42' in s:
        s = s.replace('42','51',1)
    else:
        s = s.replace('32','61',1)
print(s)
sum_1 = 0
for el in s:
    el = int(el)
    sum_1 += el
print(sum_1)