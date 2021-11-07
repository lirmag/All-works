k = (True,False)
print('x y z')
for x in k:
    for y in k:
        for z in k:
            f = ((not z) or ((not x) and y))
            if f is True:
                print(int(x),int(y),int(z))