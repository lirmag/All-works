k = (True,False)
print('w y x z')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if (((z <= w) or (y == w)) and ((x or z) == y)) is True:
                    print(int(w),int(y),int(x),int(z))
# 1 0 0 1
# 0 0 1 1