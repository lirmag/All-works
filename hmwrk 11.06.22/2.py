k = (True, False)
print('x y z')
for x in k:
    for y in k:
        for z in k:
            if ((x == z) or (x <= (y and z))) is False:
                print(int(y), int(z), int(x))
