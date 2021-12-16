k = (True,False)
print('x y z')
for x in k:
    for y in k:
        for z in k:
            if (((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))) is True:
                print(int(x),int(y),int(z))