k = (True,False)
print('x z y k')
for x in k:
    for z in k:
        for y in k:
            if (((not z) and x) is True) or (((not z) and x) is False):
                print(int(x),int(z),int(y))