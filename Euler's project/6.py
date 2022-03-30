k = list(range(1, 101))
a = sum(k) ** 2
for num in k:
    a = (a - (lambda x: x * x)(num))
print(a)
