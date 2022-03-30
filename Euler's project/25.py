count = 0
l = 0
n = 1
while len(str(l + n)) != 1000:
    c = n
    n = l + n
    l = c
    count += 1
    if len(str(l + n)) == 1000:
        print(n)
        print(count)

