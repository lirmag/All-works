seq = list(map(int, input().split()))
min_1 = []
for el in seq:
    if el % 2 != 0:
        min_1.append(el)
print(min(min_1))