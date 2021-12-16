k = (True,False)
print('x y w z')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((x or y) and (y == (not w)) and z) is True:
                    print(int(y),int(x),int(w),int(z))
# wzyx