k = (True,False)
print('x w z y')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if (((x and y) or (y and z)) == ((x <= w) and (w <= z))) is True:
                    print(int(x),int(w),int(z),int(y))

