k = (True,False)
print('z w y x')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                f = ((y <= z) or ((not x) and w)) == (w == z)
                if f is True:
                    print(int(z),int(w),int(y),int(x))
# 1 1 0 0
# 0 0 0 1
# 0 1 1 1
# z w y x

