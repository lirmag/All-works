k = (True,False)
print('x y z')
for x in k:
    for y in k:
        for z in k:
            if ((x and (not z)) or (x and y and z)) is True:
                print(int(x),int(y),int(z))