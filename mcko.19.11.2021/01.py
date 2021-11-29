k = (True, False)
print('x y z w')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                if ((not (x and y)) and (y or z) or (not w)) is False:
                    print(int(x), int(y), int(z), int(w))
# ywxz