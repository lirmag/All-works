k = (True,False)
print('y w x z')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((not(x and y)) and (y or z) or (not w)) is False:
                    print(int(y),int(w),int(x),int(z))
# ywxz