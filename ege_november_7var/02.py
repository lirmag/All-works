k = (True,False)
print('x y z')
for x in k:
    for y in k:
        for z in k:
            if (((not x) and y) or (y and z)) is True:
                print(int(x),int(y),int(z))