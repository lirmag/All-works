k = (True,False)
print('x y z w')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((x and (y or (not z)) and w) == (x <= (not z) and z)) is True:
                    print(int(y),int(x),int(z),int(w))
# yxzw