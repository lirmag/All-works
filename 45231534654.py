k = (True, False)
print('c', 'a', 'b', 'd', 'F')
for a in k:
    for b in k:
        for c in k:
            for d in k:
                F = ((a and b) == (not (c))) and (b >= d)
                if F is True:
                    print(int(c), int(a), int(b), int(d), int(F))
