def make_readable(seconds):
    hh = 0
    mm = 0
    ss = seconds
    while ss > 59:
        mm += 1
        ss -= 60
    while mm > 59:
        hh += 1
        mm -= 60
    if len(str(ss)) == 1:
        ss = '0' + str(ss)
    if len(str(mm)) == 1:
        mm = '0' + str(mm)
    if len(str(hh)) == 1:
        hh = '0' + str(hh)
    if seconds == 0:
        return str(hh) + ':' + str(mm) + ':' + str(ss)
    return str(hh) + ':' + str(mm) + ':' + str(ss)
print(make_readable(60))