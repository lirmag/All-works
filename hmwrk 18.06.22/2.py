k = (True, False)
print('x y z')
for x in k:
    for y in k:
        for z in k:
            if ((x >= y) and (y <= z)) is True:
                print(int(x), int(z), int(y))