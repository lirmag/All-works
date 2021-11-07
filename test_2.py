a = [10,20,30,40]
count = 0
m = 19999
s = 0
for i in range(len(a) - 1):
    number = a[i]
    s += 1
    # while i < len(a):
    for k in range(s,len(a)):
        number_1 = a[k]
        if (int(number) * int(number_1)) % 10 == 0:
            count += 1
            m = max(m, int(number) + int(number_1))
        # k += 1
        # if i >= len(a):
        #     k = p
        #     p += 1
print(count)
print(m)