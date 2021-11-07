k = (True,False)
print('x w z y')
for x in k:
    for y in k:
         for z in k:
            for w in k:
                f = (x and (not y)) or (y == z) or (not w)
                if f is False:
                    print(int(x),int(w),int(z),int(y))