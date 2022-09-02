k = (True,False)
print('x y z w')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((x == (not y)) <=(z == (y or w))) is False:
                    print(int(z),int(w),int(y),int(x))