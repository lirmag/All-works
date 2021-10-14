k = (True, False)
print('c', 'a', 'd', 'b', 'F')
for a in k:
    for b in k:
        for c in k:
            for d in k:
                F = a and not b or (a or b) and c or d
                if F is False:
                    print(int(c), int(a), int(d), int(b), int(F))