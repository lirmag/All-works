k = (True,False)
print('x y z w')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((x and (not y )) or (y == z) or (not w)) is False:
                    print(int(w),int(z),int(y),int(x))