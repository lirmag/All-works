k = (True,False)
print('x y z f')
for x in k:
    for y in k:
        for z in k:
            f = ((not z) and x)
            if ((f is True) or (f is False)):
                print(int(x),int(y),int(z),int(f))