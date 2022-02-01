k = (True,False)
print('x y z w')
for x in k:
    for y in k:
        for z in k:
             for w in k:
                 if (((x and (not y)) or (w <= z)) == (z == x)) is True:
                     print(int(z),int(y),int(w),int(x))