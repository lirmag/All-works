k = (True,False)
print('x y z w')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((x == (w or y )) or ((w <= z) and (y <= w))) is False:
                    print(int(y),int(x),int(z),int(w))


# x y z w
# 1 0 0 1
# 0 0 0 1
# 1 0 1 0
# 1 0 0 0