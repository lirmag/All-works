def c(ln):
    k = []
    for ind, elem in enumerate(ln):
        for index in range(len(ln) - 1, 1, -1):
            if elem == line[index]:
                k.append(abs(index - ind))
    return max(k)


with open('inf_26_04_21_24.txt', 'r') as f:
    ans = []
    for line in f.readlines():
        if line.count('A') < 25:
            ans.append(c(line))
print(max(ans))
