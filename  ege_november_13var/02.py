k = (True,False)
print('x y z')
for x in k:
    for y in k:
        for z in k:
            if ((not z) and ((not x) or y)) is True:
                print(int(x),int(y),int(z))