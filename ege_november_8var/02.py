k = (True,False)
print('x y z w')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((not w) and z and (y <= x)) is True:
                    print(int(x),int(y),int(z),int(w))