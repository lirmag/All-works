k = (True, False)
print('a b c d F')
for a in k:
    for b in k:
        for c in k:
            for d in k:
                F = ((a and b) == (not c)) and (b >= d)
                if F is True:
                    print(int(a),int(b),int(c),int(d),int(F))
                # ((a ∧ b) ≡ ¬c) ∧ (b → d)