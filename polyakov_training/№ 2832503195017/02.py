k = (True,False)
print('c b a d')
for a in k:
    for b in k:
        for c in k:
            for d in k:
                if (((a and b) == (not c)) and (b <= d)) is True:
                    print(int(c),int(a),int(d),int(b))
