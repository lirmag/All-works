k = (True,False)
print('c b d a')
for a in k:
    for b in k:
        for c in k:
            for d in k:
                if (((a and b) == (not c)) and (b <= d)) is True:
                    print(int(c),int(b),int(d),int(a))
# c  a/b d a/b

# cadb