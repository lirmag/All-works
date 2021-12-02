move_zeros =([1, 0, 1, 2, 0, 1, 3])
for el in move_zeros:
    if el == 0:
        move_zeros.append(el)
        move_zeros.remove(el)
print(move_zeros)