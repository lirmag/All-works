k = (True,False)
print('x y z w')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if (((x <= y) and (y <= w)) or (z == (x or y))) is False:
                    print(int(y),int(w),int(z),int(x))


# 1 0 0 1
# 1 0 0 0
# 0 1 0 1
# 0 0 0 1

