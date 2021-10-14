# ¬(y → (x ≡ w)) /\ (z → x)
a = (True, False)
print('x', 'y', 'z', 'w', 'F')
for x in a:
    for y in a:
        for z in a:
            for w in a:
                F = not(y <= (x == w)) and (z <= x)
                if F is True:
                    print(int(x), int(y), int(z), int(w), int(F))

