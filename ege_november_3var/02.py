k = (True,False)
print('x y z')
for x in k:
    for y in k:
         for z in k:
             f = (x and (not y)) or (x and z)
             if f is True:
                 print(int(x),int(y),int(z))