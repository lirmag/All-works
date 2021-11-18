seq = list(map(int, input().split()))
max_1 = 0
ind = 0
for el in range(0, len(seq)):
    if seq[el] > max_1:
        max_1 = seq[el]
        ind = el
    else:
        continue
print(max_1, ind)
