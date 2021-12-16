number = '35'
number = int(number,base=7)
print(number)
n_2 = '35'
n_2 = int(n_2,base=6)
print(n_2)
x = 0
while n_2 != number:
    n_2 += 1
    x += 1
print(x)