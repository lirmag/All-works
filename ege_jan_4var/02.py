k = (True,False)
print('x y z w')
for x in k:
    for y in k:
        for z in k:
             for w in k:
                 if (((x and w) or (w and z)) == ((x <= y) and (y <= x))) is True:
                     print(int(x),int(y),int(z),int(w))