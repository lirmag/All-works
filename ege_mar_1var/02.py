k = (True,False)
print('z w y x')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if (((y <= z) or ((not x) and w)) == (w == z)) is True:
                    print(int(z),int(w),int(y),int(x))