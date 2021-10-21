n = 250
number = 3
c = (str(number)) * n
while '3333' in c or '7777' in c:
    if '3333' in c:
        c = c.replace('3333', '7', 1)
    else:
        c = c.replace('777', '3', 1)
print(c)