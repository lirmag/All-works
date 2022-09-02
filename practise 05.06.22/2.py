k = (True,False)
print('x y z w')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if (((x <= y) == (z <= w)) or (x and w)) is False:
                    print(int(z),int(y),int(x),int(w))
