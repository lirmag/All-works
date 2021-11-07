k = (True,False)
print('x y z')
for x in k:
    for y in k:
        for z in k:
            f = (((not x) and z) or ((not x) and (not y) and (not z)))
            if f is True:
                print(int(x),int(y),int(z))